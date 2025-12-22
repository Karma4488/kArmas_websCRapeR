# kArmas_websCRapeR 

**A badass web scraping tool for red teamers**

Quick script in Python - made it a proper repo/tool for the community!  
Easy to install and use with a professional project structure.

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)

## Features 💪 

- **Information Gathering**
  - 📧 Email extraction
  - 📞 Phone number extraction
  - 📱 Social media link discovery (Twitter, LinkedIn, Facebook, GitHub, Instagram)
  - 💰 Cryptocurrency wallet detection (Bitcoin, Ethereum, Litecoin, Dogecoin, Monero, Ripple)
  - 🌐 Subdomain enumeration
  - 🔗 Link crawling

- **Red Team Capabilities**
  - ⚠️ Basic XSS vulnerability detection
  - 💉 Basic SQL injection testing
  - 🥷 Stealth mode with user-agent rotation
  - ⏱️ Rate limiting for opsec
  - 🎯 Targeted reconnaissance

## Installation

### Quick Install (Recommended)

```bash
# Install directly from GitHub
pip install git+https://github.com/Karma4488/kArmas_websCRapeR.git
```

### Development Install

#keepITsimple

Remember to run it in a venv environment!

```bash
# Clone the repository
git clone https://github.com/Karma4488/kArmas_websCRapeR.git
cd kArmas_websCRapeR

# Create virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate  # Windows

# Upgrade pip
pip install --upgrade pip

# Install in development mode
pip install -e .
```

### Legacy Method (Also Works)

```bash
# Install requirements manually
pip install -r requirements.txt

# Run directly
python karmas_scraper.py -u https://target.com
```

## Usage

### As a Command-Line Tool

```bash
# After pip installation
karmas-scraper -u https://example.com -v --check-vulns
```

### Legacy Script Method

```bash
# Basic scan
python karmas_scraper.py -u https://example.com

# Verbose mode with vulnerability checks
python karmas_scraper.py -u https://example.com -v --check-vulns

# Fast scan without stealth
python karmas_scraper.py -u https://example.com --no-stealth
```

### As a Python Module

```python
from karmas_scraper import KarmasScraper

# Create scraper instance
scraper = KarmasScraper(
    target_url="https://example.com",
    verbose=True,
    stealth=True
)

# Run scan
results = scraper.scan_target(check_vulns=True)

# Display results
scraper.print_results()
```

### Command Line Options

- `-u, --url` : Target URL to scrape (required)
- `-v, --verbose` : Enable verbose output
- `--check-vulns` : Enable vulnerability checking (XSS, SQLi)
- `--no-stealth` : Disable stealth mode (faster but less opsec)

## Project Structure

```
kArmas_websCRapeR/
├── src/karmas_scraper/      # Main package
│   ├── __init__.py          # Package init
│   └── scraper.py           # Core scraper
├── tests/                   # Unit tests
├── docs/                    # Documentation
├── LICENSE                  # MIT License
├── CONTRIBUTING.md          # How to contribute
├── CODE_OF_CONDUCT.md       # Community guidelines
└── setup.py                 # Installation script
```

See [docs/project_structure.md](docs/project_structure.md) for detailed information.

## Example Output

```
 kArma's Web Scraper - Red Team Edition 🏴‍☠️
============================================================

📧 Emails Found (3):
  - contact@example.com
  - info@example.com
  - admin@example.com

📱 Social Media Links Found:
  TWITTER:
    - twitter.com/example
  LINKEDIN:
    - linkedin.com/in/example

💰 Cryptocurrency Wallets Found:
  BITCOIN:
    - 1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa
  ETHEREUM:
    - 0x742d35Cc6634C0532925a3b844Bc9e7595f0bEbA

🔗 Links Found (42):
  - https://example.com/about
  - https://example.com/contact
  ...
```

## Disclaimer 

This tool is for **educational and authorized security testing purposes only**. 
Always obtain proper authorization before scanning any target.

- Only test on systems you own or have explicit permission to test
- Respect robots.txt and terms of service
- Be responsible with the information you discover
- Know and follow your local laws

## Red Team Tips 🎯

- Use stealth mode when conducting OSINT
- Combine with other recon tools for maximum effectiveness
- Document your findings properly
- Always maintain opsec

For detailed usage examples and red team scenarios, see [docs/usage_examples.md](docs/usage_examples.md)

## Contributing 🤝

We welcome contributions from red teamers, security researchers, and developers!

- Read [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines
- Check [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) for community standards
- Submit issues for bugs or feature requests
- Create pull requests for improvements

Find the funny links 🚀

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

#weareLegion #keepITsimple

for my Anonymous & Lulzsec friends 

made in l0v3 by kArmasec

from one redhat to another 🎩

RedTeamer


---

*Remember: With great power comes great responsibility. Be a badass, but be ethical.* 👽 
