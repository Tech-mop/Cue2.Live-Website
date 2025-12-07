# Cue2.Live

Welcome to the official website for Cue2, an open-source media playback solution for events.

## About

This website is built using Jekyll, a static site generator.

## Development

### Prerequisites

- Ruby 3.2+
- Bundler
- Jekyll

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

3. Serve the site locally:
   ```bash
   bundle exec jekyll serve
   ```

   The site will be available at `http://localhost:4000`.

### Building

To build the site for production:
```bash
bundle exec jekyll build
```

The built site will be in the `_site` directory.

## Deployment

The site is automatically built and deployed to GitHub Pages on push to the master branch via GitHub Actions.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.