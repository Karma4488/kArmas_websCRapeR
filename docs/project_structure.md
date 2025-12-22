# Project Structure Documentation

## Overview

This document describes the organization and structure of the kArmas_websCRapeR project.

## Directory Structure

```
kArmas_websCRapeR/
├── src/
│   └── karmas_scraper/
│       ├── __init__.py          # Package initialization
│       └── scraper.py           # Main scraper implementation
├── tests/
│   └── test_scraper.py          # Unit tests
├── docs/
│   ├── project_structure.md     # This file
│   └── usage_examples.md        # Detailed usage examples
├── .gitignore                   # Git ignore rules
├── CODE_OF_CONDUCT.md           # Community guidelines
├── CONTRIBUTING.md              # Contribution guidelines
├── LICENSE                      # MIT License
├── README.md                    # Main documentation
├── requirements.txt             # Python dependencies
├── setup.py                     # Installation script
├── karmas_scraper.py           # Legacy script (kept for compatibility)
├── test_scraper.py             # Legacy test (kept for compatibility)
└── examples.md                 # Legacy examples (kept for compatibility)
```

## Component Descriptions

### Core Source (`src/karmas_scraper/`)

**`__init__.py`**
- Package initialization file
- Exports main classes and functions
- Defines version and metadata

**`scraper.py`**
- Main KarmasScraper class
- Information extraction methods:
  - `extract_emails()` - Email address extraction
  - `extract_phone_numbers()` - Phone number extraction
  - `extract_social_media()` - Social media link discovery
  - `extract_crypto_wallets()` - Cryptocurrency wallet detection
  - `extract_subdomains()` - Subdomain enumeration
  - `extract_links()` - Link crawling
- Vulnerability scanning methods:
  - `check_xss_vulnerable()` - XSS detection
  - `check_sql_injection()` - SQL injection testing
- Utility methods:
  - `make_request()` - HTTP request handling with stealth
  - `scan_target()` - Main scanning orchestration
  - `print_results()` - Formatted output display

### Tests (`tests/`)

**`test_scraper.py`**
- Unit tests for all extraction methods
- Tests cover:
  - Email extraction
  - Phone number extraction (multiple formats)
  - Social media link discovery
  - Cryptocurrency wallet detection
  - Subdomain enumeration
  - Link extraction

### Documentation (`docs/`)

**`project_structure.md`**
- This file - explains project organization

**`usage_examples.md`**
- Comprehensive usage examples
- Red team operation scenarios
- OSINT gathering techniques
- Security testing workflows

### Configuration Files

**`.gitignore`**
- Excludes Python cache files
- Excludes virtual environments
- Excludes IDE-specific files

**`requirements.txt`**
- Lists all Python dependencies
- Currently: `requests>=2.31.0`

**`setup.py`**
- Installation configuration
- Package metadata
- Entry points for console scripts

### Documentation Files

**`README.md`**
- Main project documentation
- Features overview
- Installation instructions
- Usage examples
- Ethical guidelines

**`CONTRIBUTING.md`**
- Contribution guidelines
- Development setup
- Code style guidelines
- PR submission process

**`CODE_OF_CONDUCT.md`**
- Community standards
- Ethical use guidelines
- Enforcement policies

**`LICENSE`**
- MIT License
- Usage rights and restrictions

## Installation

### Development Installation

```bash
# Clone the repository
git clone https://github.com/Karma4488/kArmas_websCRapeR.git
cd kArmas_websCRapeR

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate  # Windows

# Install in development mode
pip install -e .
```

### User Installation

```bash
pip install git+https://github.com/Karma4488/kArmas_websCRapeR.git
```

## Usage

### As a command-line tool

```bash
# After installation
karmas-scraper -u https://target.com -v --check-vulns
```

### As a Python module

```python
from karmas_scraper import KarmasScraper

scraper = KarmasScraper("https://target.com", verbose=True, stealth=True)
results = scraper.scan_target(check_vulns=True)
scraper.print_results()
```

### Running tests

```bash
# From project root
python tests/test_scraper.py

# Or using the legacy location
python test_scraper.py
```

## Development Workflow

1. **Fork and Clone**
   ```bash
   git clone https://github.com/YOUR_USERNAME/kArmas_websCRapeR.git
   ```

2. **Create Feature Branch**
   ```bash
   git checkout -b feature/your-feature
   ```

3. **Make Changes**
   - Edit files in `src/karmas_scraper/`
   - Add tests to `tests/test_scraper.py`
   - Update documentation as needed

4. **Test Changes**
   ```bash
   python tests/test_scraper.py
   ```

5. **Commit and Push**
   ```bash
   git add .
   git commit -m "Add your feature"
   git push origin feature/your-feature
   ```

6. **Create Pull Request**
   - Go to GitHub
   - Create PR from your feature branch
   - Describe your changes

## Backward Compatibility

The following files are kept at the root level for backward compatibility:
- `karmas_scraper.py` - Original script location
- `test_scraper.py` - Original test location
- `examples.md` - Original examples location

These work as before, but the recommended approach is to use the new structure with `pip install -e .` and the `karmas-scraper` command.

## Future Enhancements

Potential improvements to the project structure:

- [ ] Add CI/CD with GitHub Actions
- [ ] Add more comprehensive test suite
- [ ] Add API documentation with Sphinx
- [ ] Add Docker support
- [ ] Add configuration file support
- [ ] Add plugin system for custom extractors

---

#weareLegion #keepITsimple 🚀👽🏴‍☠️

**by kArmaSec**
