# {% t home.hero_h1 %} — looks up _data/i18n/<active_lang>.yml with English fallback.
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
      value.nil? ? @key : value.to_s
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
