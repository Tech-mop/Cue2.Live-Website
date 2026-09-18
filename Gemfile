source 'https://rubygems.org'

# Match GitHub Actions (.github/workflows/jekyll.yml). macOS system Ruby 2.6 will not work.
ruby '>= 3.2'

gem 'jekyll', '~> 4.4'
# Required on Ruby 3.4+ / 4, where logger left the default gems.
gem 'logger'
group :jekyll_plugins do
  gem 'jekyll-polyglot', '~> 1.9'
end
