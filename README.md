# kArmas_websCRapeR 🚀🏴‍☠️

**A badass web scraping tool for red teamers**

Quick script in Python - made it a repo/tool for the community.
Easy to install and use!

## Features 💪

- **Information Gathering**
  - 📧 Email extraction
  - 📞 Phone number extraction
  - 📱 Social media link discovery (Twitter, LinkedIn, Facebook, GitHub, Instagram)
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

**by kArmaSec**

---

*Remember: With great power comes great responsibility. Be a badass, but be ethical.* 👽
