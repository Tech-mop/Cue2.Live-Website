# {% t home.hero_h1 %} — looks up _data/i18n/<active_lang>.yml with English fallback.
# Placeholders filled from site.cue2_release (set by _plugins/cue2_release.rb):
#   {version} -> 0.1.1   {tag} -> v0.1.1   {release} -> 0.1.1 StripyHat
module Cue2I18n
  class TTag < Liquid::Tag
    def initialize(tag_name, key, tokens)
      super
      @key = key.strip
    end

    def render(context)
      site = context.registers[:site]
      lang = if site.respond_to?(:active_lang)
               site.active_lang
             else
               site.config['active_lang'] || site.config['default_lang'] || 'en'
             end
      keys = @key.split('.')
      value = dig(site.data.dig('i18n', lang), keys)
      value = dig(site.data.dig('i18n', 'en'), keys) if value.nil? || value == ''
      value.nil? ? @key : fill(value.to_s, site.config['cue2_release'] || {})
    end

    def fill(text, release)
      return text unless text.include?('{')

      version = release['version'].to_s
      label = [version, release['codename'].to_s].reject(&:empty?).join(' ')
      text.gsub('{version}', version)
          .gsub('{tag}', release['tag'].to_s)
          .gsub('{release}', label)
    end

    def dig(node, keys)
      keys.each do |k|
        return nil unless node.is_a?(Hash)
        node = node[k]
      end
      node
    end
  end
end

Liquid::Template.register_tag('t', Cue2I18n::TTag)
