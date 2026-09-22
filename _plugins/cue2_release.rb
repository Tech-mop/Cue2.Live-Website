# frozen_string_literal: true

require "json"
require "net/http"
require "uri"

# Replaces site.cue2_release with the latest GitHub release at build time.
# Filename versions change every release, so assets are matched by platform
# suffix. _config.yml is used when the API cannot be reached.
module Cue2Release
  API = "https://api.github.com/repos/Tech-mop/Cue2/releases/latest"
  REPO = "Tech-mop/Cue2"
  PAGE = "https://github.com/#{REPO}/releases"

  PLATFORMS = {
    "windows_x86_64" => /-windows-x86_64\.zip\z/i,
    "windows_arm64" => /-windows-arm64\.zip\z/i,
    "macos_arm64" => /-macos-arm64\.zip\z/i,
    "linux_x86_64" => /-linux-x86_64\.tar\.gz\z/i,
    "linux_arm64" => /-linux-arm64\.tar\.gz\z/i
  }.freeze

  module_function

  def apply(site)
    fallback = site.config["cue2_release"] || {}
    resolved = from_github || from_config(fallback)
    resolved["assets"] = assets_for(resolved)
    source = resolved.delete("source")
    resolved.delete("github_assets")
    site.config["cue2_release"] = resolved
    Jekyll.logger.info("Cue2 release:", "#{resolved["tag"]} (#{source})")
  end

  def from_github
    payload = get_json(API)
    raise "latest release response did not include a tag" unless payload.is_a?(Hash)

    tag = payload["tag_name"].to_s
    raise "latest release response did not include a tag" if tag.empty?

    {
      "version" => tag.sub(/\Av/, ""),
      "tag" => tag,
      "page" => PAGE,
      "source" => "GitHub latest release",
      "github_assets" => Array(payload["assets"])
    }
  rescue StandardError => e
    # A failed scheduled build must leave the last good Pages deploy in place.
    # Falling back here would republish the stale version from _config.yml.
    message = "GitHub API unavailable (#{e.class}: #{e.message})"
    if ENV["GITHUB_ACTIONS"] == "true"
      Jekyll.logger.error("Cue2 release:", message)
      raise
    end

    Jekyll.logger.warn("Cue2 release:", message)
    nil
  end

  def from_config(config)
    version = config["version"].to_s
    version = "0.1.1" if version.empty?
    tag = config["tag"].to_s
    tag = "v#{version}" if tag.empty?
    page = config["page"].to_s
    page = PAGE if page.empty?
    {
      "version" => version,
      "tag" => tag,
      "page" => page,
      "source" => "_config.yml fallback",
      "github_assets" => []
    }
  end

  def assets_for(release)
    prefix = "https://github.com/#{REPO}/releases/download/#{release["tag"]}/"
    matched = {}
    Array(release["github_assets"]).each do |asset|
      name = asset["name"].to_s
      url = asset["browser_download_url"].to_s
      next unless url.start_with?(prefix)

      PLATFORMS.each do |key, pattern|
        matched[key] = url if pattern.match?(name)
      end
    end

    missing = PLATFORMS.keys - matched.keys
    if !Array(release["github_assets"]).empty? && !missing.empty?
      Jekyll.logger.warn("Cue2 release:", "no asset for #{missing.join(', ')}; using the filename convention")
    end

    constructed = constructed_assets(release["tag"], release["version"])
    PLATFORMS.each_key { |key| matched[key] ||= constructed[key] }
    matched
  end

  def constructed_assets(tag, version)
    base = "https://github.com/#{REPO}/releases/download/#{tag}/Cue2-#{version}"
    {
      "windows_x86_64" => "#{base}-windows-x86_64.zip",
      "windows_arm64" => "#{base}-windows-arm64.zip",
      "macos_arm64" => "#{base}-macos-arm64.zip",
      "linux_x86_64" => "#{base}-linux-x86_64.tar.gz",
      "linux_arm64" => "#{base}-linux-arm64.tar.gz"
    }
  end

  def get_json(url)
    uri = URI(url)
    redirects = 0
    loop do
      raise "too many redirects" if redirects > 3

      response = request(uri)
      if response.is_a?(Net::HTTPRedirection)
        location = response["location"].to_s
        raise "redirect without location" if location.empty?

        uri = URI.join("#{uri.scheme}://#{uri.host}", location)
        raise "refusing non-https redirect" unless uri.scheme == "https"

        redirects += 1
        next
      end

      raise "HTTP #{response.code}" unless response.is_a?(Net::HTTPSuccess)

      return JSON.parse(response.body)
    end
  end

  def request(uri)
    Net::HTTP.start(
      uri.host,
      uri.port,
      use_ssl: uri.scheme == "https",
      open_timeout: 5,
      read_timeout: 8
    ) do |http|
      req = Net::HTTP::Get.new(uri)
      req["User-Agent"] = "Cue2-Website"
      req["Accept"] = "application/vnd.github+json"
      req["X-GitHub-Api-Version"] = "2022-11-28"
      token = ENV["GITHUB_TOKEN"] || ENV["GH_TOKEN"]
      req["Authorization"] = "Bearer #{token}" unless token.to_s.empty?
      http.request(req)
    end
  end
end

Jekyll::Hooks.register :site, :after_init do |site|
  Cue2Release.apply(site)
end
