# kArma's Web Scraper - Usage Examples 🚀

## Basic Usage

### Quick Scan
Get basic information from a website:
```bash
python karmas_scraper.py -u https://target.com
```

### Verbose Mode
See detailed logs of what the scraper is doing:
```bash
python karmas_scraper.py -u https://target.com -v
```

### Fast Scan (No Stealth)
Disable stealth features for faster scanning (use in controlled environments):
```bash
python karmas_scraper.py -u https://target.com --no-stealth
```

## Red Team Operations

### Full Reconnaissance
Get all information including vulnerability checks:
```bash
python karmas_scraper.py -u https://target.com -v --check-vulns
```

### OSINT Gathering
Focus on information gathering with stealth:
```bash
python karmas_scraper.py -u https://target.com -v
```

## What It Finds

### Information Gathering
- 📧 **Email Addresses**: Extracts all email addresses from the page
- 📞 **Phone Numbers**: Finds phone numbers in various formats
- 📱 **Social Media**: Discovers Twitter, LinkedIn, Facebook, GitHub, Instagram links
- 💰 **Cryptocurrency Wallets**: Detects Bitcoin, Ethereum, Litecoin, Dogecoin, Monero, and Ripple wallet addresses
- 🌐 **Subdomains**: Identifies subdomains mentioned on the page
- 🔗 **Links**: Crawls and lists all links found

### Security Testing (with --check-vulns)
- ⚠️ **XSS Detection**: Tests for potential Cross-Site Scripting vulnerabilities
- 💉 **SQL Injection**: Checks for potential SQL injection points

## Red Teaming Tips 🎯

### 1. Information Gathering Phase
Start with basic reconnaissance:
```bash
python karmas_scraper.py -u https://target.com -v > recon.txt
```

### 2. Identify Attack Surface
Look for:
- Contact emails for phishing campaigns
- Social media accounts for OSINT
- Cryptocurrency wallets for financial intelligence
- Subdomains for expanded attack surface
- Links to other properties

### 3. Initial Vulnerability Assessment
```bash
python karmas_scraper.py -u https://target.com --check-vulns -v
```

### 4. Stealth Considerations
- Always use stealth mode for real engagements (default)
- Space out your scans
- Use through proxy if needed
- Respect robots.txt unless explicitly authorized

## Combining with Other Tools

### With curl for specific checks:
```bash
python karmas_scraper.py -u https://target.com -v
curl -I https://target.com
```

### With nmap for full recon:
```bash
python karmas_scraper.py -u https://target.com
nmap -A target.com
```

### With whois for domain info:
```bash
python karmas_scraper.py -u https://target.com
whois target.com
```

## Output Interpretation

### Email Findings
Use discovered emails for:
- Phishing simulations (authorized only!)
- User enumeration
- Password reset attacks
- Social engineering campaigns

### Social Media Links
Use for:
- OSINT gathering
- Employee profiling
- Company culture research
- Attack vector identification

### Cryptocurrency Wallets
Use for:
- Financial intelligence gathering
- Tracking payment flows
- Identifying funding sources
- Transaction analysis on blockchain explorers

### Subdomain Discovery
Use for:
- Expanding attack surface
- Finding forgotten/unmaintained systems
- Identifying development/staging servers

### Vulnerability Findings
- **XSS**: Potential injection points for client-side attacks
- **SQLi**: Database interaction points to test further

## Safety and Ethics ⚠️

**IMPORTANT**: Only use on systems you own or have explicit written permission to test!

### Legal Usage:
- ✅ Your own websites
- ✅ Bug bounty programs
- ✅ Authorized penetration tests
- ✅ Educational labs and CTFs

### Illegal Usage:
- ❌ Unauthorized scanning
- ❌ Any system without permission
- ❌ Attacking based on findings without authorization

## Troubleshooting

### Connection Issues
```bash
# Test basic connectivity first
curl -I https://target.com

# Then try the scraper
python karmas_scraper.py -u https://target.com -v
```

### No Results Found
- Verify the URL is correct and accessible
- Check if the site requires authentication
- Some sites may block scraping - respect their wishes
- Try with verbose mode to see what's happening

### Too Slow
```bash
# Use --no-stealth for faster scanning in controlled environments
python karmas_scraper.py -u https://target.com --no-stealth
```

## Remember 🏴‍☠️

> "With great power comes great responsibility"

- Always get authorization
- Document your findings properly
- Report vulnerabilities responsibly
- Be ethical in your red teaming

#weareLegion #keepITsimpel

**by kArmaSec**
