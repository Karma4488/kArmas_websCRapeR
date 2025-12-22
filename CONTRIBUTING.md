# Contributing to kArmas_websCRapeR 🏴‍☠️

Thanks for your interest in contributing! We welcome contributions from red teamers, security researchers, and developers.

## Code of Conduct

This project follows a simple code of conduct: Be respectful, be ethical, and #keepITsimple.

## How to Contribute

### Reporting Issues

- Use the GitHub issue tracker
- Describe the issue clearly
- Include steps to reproduce
- Mention your Python version and OS

### Submitting Pull Requests

1. **Fork the repository**
   ```bash
   git clone https://github.com/Karma4488/kArmas_websCRapeR.git
   cd kArmas_websCRapeR
   ```

2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make your changes**
   - Follow the existing code style
   - Keep it simple (#keepITsimple)
   - Add tests for new features
   - Update documentation

4. **Test your changes**
   ```bash
   python test_scraper.py
   ```

5. **Commit your changes**
   ```bash
   git add .
   git commit -m "Add your feature description"
   ```

6. **Push and create PR**
   ```bash
   git push origin feature/your-feature-name
   ```

## Development Guidelines

### Code Style

- Follow PEP 8 guidelines
- Use meaningful variable names
- Add docstrings to functions
- Keep functions focused and simple

### Adding New Features

When adding new extraction capabilities:

1. Add the extraction function to `src/karmas_scraper/scraper.py`
2. Add tests to `tests/test_scraper.py`
3. Update the README with usage examples
4. Update `examples.md` with red team use cases

### Testing

- Run all tests before submitting: `python test_scraper.py`
- Add tests for new functionality
- Ensure existing tests still pass

### Documentation

- Update README.md for user-facing changes
- Update examples.md for new red team use cases
- Add inline comments for complex logic

## Feature Requests

We're always looking for new features! Ideas we're interested in:

- New cryptocurrency wallet patterns
- Additional OSINT data extraction
- Enhanced stealth capabilities
- Better vulnerability detection
- Performance improvements

## Security

If you discover a security vulnerability, please email the details privately rather than opening a public issue.

## Questions?

Feel free to open an issue with your question or reach out to the community.

#weareLegion #keepITsimple

**by kArmaSec** 🚀👽🏴‍☠️
