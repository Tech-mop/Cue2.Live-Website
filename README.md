# Cue2.Live

Welcome to the official website for Cue2, an open-source media playback solution for events.

## About

This website is built using Jekyll, a static site generator.

## Development

### Prerequisites

- Ruby 3.2 or newer (**not** macOS system Ruby 2.6)
- Bundler

On a Mac, `bundle` is often `/usr/bin/bundle` from Apple’s Ruby 2.6. That cannot install this site (`Gemfile.lock` needs Bundler 4 / Ruby 3.2+). Use Homebrew Ruby instead:

```bash
brew install ruby
echo 'export PATH="/opt/homebrew/opt/ruby/bin:/opt/homebrew/bin:$PATH"' >> ~/.zprofile
export PATH="/opt/homebrew/opt/ruby/bin:/opt/homebrew/bin:$PATH"
```

Check you left system Ruby behind:

```bash
which ruby    # /opt/homebrew/opt/ruby/bin/ruby  (or another Homebrew path)
which bundle  # must NOT be /usr/bin/bundle
ruby -v       # 3.2 or newer
```

To match GitHub Actions exactly: `brew install ruby@3.2` and put `$(brew --prefix ruby@3.2)/bin` first on `PATH`.

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/Tech-mop/Cue2.Live-Website.git
   cd Cue2.Live-Website
   ```

2. Install dependencies:
   ```bash
   bundle install
   ```

   If `gem install` hits a permissions error, keep gems in the repo (already gitignored):

   ```bash
   bundle config set --local path vendor/bundle
   bundle install
   ```

3. Serve the site locally:
   ```bash
   bundle exec jekyll serve
   ```

   The site will be available at [http://localhost:4000](http://localhost:4000). Language prefixes: `/es/`, `/de/`, `/mi/`, `/ru/`, `/ja/`, `/ar/`, `/hi/`.

### Translations

See [tools/i18n/README.md](tools/i18n/README.md). Short version: edit `_data/i18n/en.yml`, then `python3 tools/i18n/update_catalog.py`.

### Building

To build the site for production:
```bash
bundle exec jekyll build
```

The built site will be in the `_site` directory.

## Deployment

The site is automatically built and deployed to GitHub Pages on push to the `main` branch via GitHub Actions.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.