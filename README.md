# kArmas_websCRapeR 🚀🏴‍☠️

**A badass web scraping tool for red teamers**

Quick script in Python - made it a repo/tool for the community 👽🚀🫂🏴‍☠️🎩
Easy to install and use!

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

#keepITsimpel

Remember to run it in a venv environment!

```bash
# Create virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate  # Windows

# Upgrade pip
pip install --upgrade pip

# Install requirements
pip install -r requirements.txt
```

## Usage

```bash
# Basic scan
python karmas_scraper.py -u https://example.com

# Verbose mode with vulnerability checks
python karmas_scraper.py -u https://example.com -v --check-vulns

# Fast scan without stealth
python karmas_scraper.py -u https://example.com --no-stealth
```

### Command Line Options

- `-u, --url` : Target URL to scrape (required)
- `-v, --verbose` : Enable verbose output
- `--check-vulns` : Enable vulnerability checking (XSS, SQLi)
- `--no-stealth` : Disable stealth mode (faster but less opsec)

## Example Output

```
🚀 kArma's Web Scraper - Red Team Edition 🏴‍☠️
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

## Disclaimer ⚠️

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

Find the funny links 🚀

#weareLegion #keepITsimpel

for my Anonymous & Lulzsec friends 

made in l0v3 

yea code is more 'sprog' : D -------(-_-)----

**by kArmaSec**

from one redhat tp another 🎩

RedTeamer


---

*Remember: With great power comes great responsibility.be a badass, but be ethical.* 👽
