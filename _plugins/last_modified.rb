# frozen_string_literal: true

require "open3"
require "time"

# Sitemap <lastmod> dates. Each page's date is the newest of:
#   - the last git commit touching the files that make up that page
#   - the publish date of the Cue2 release it links to
# Exposed as site.page_lastmod["/"] and site.page_lastmod["/about/"] (YYYY-MM-DD).
# The Pages workflow checks out full history (fetch-depth: 0) so git dates are real;
# without git it falls back to the build time.
module Cue2LastModified
  SHARED = %w[_layouts _includes _data/i18n _plugins _config.yml].freeze
  PAGES = {
    "/" => %w[index.md assets/css assets/js assets/img],
    "/about/" => %w[about.md]
  }.freeze

  module_function

  def apply(site)
    @cache ||= compute(site)
    site.config["page_lastmod"] = @cache
  end

  def compute(site)
    release = parse_time(site.config.dig("cue2_release", "published_at"))
    PAGES.each_with_object({}) do |(url, paths), out|
      dates = [git_time(site.source, paths + SHARED), release].compact
      out[url] = (dates.max || site.time).utc.strftime("%Y-%m-%d")
    end
  end

  def git_time(root, paths)
    stdout, status = Open3.capture2("git", "-C", root, "log", "-1", "--format=%cI", "--", *paths)
    status.success? ? parse_time(stdout.strip) : nil
  rescue StandardError
    nil
  end

  def parse_time(value)
    value.to_s.empty? ? nil : Time.parse(value.to_s)
  rescue ArgumentError
    nil
  end
end

Jekyll::Hooks.register :site, :post_read do |site|
  Cue2LastModified.apply(site)
end
