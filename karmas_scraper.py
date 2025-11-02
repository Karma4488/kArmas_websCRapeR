#!/usr/bin/env python3
"""
kArma's Web Scraper - Red Team Edition
A badass web scraping tool for red teamers
by kArmaSec
"""

import requests
import re
import argparse
import time
import sys
import random
from urllib.parse import urljoin, urlparse
from collections import defaultdict
from datetime import datetime

class KarmasScraper:
    """Main scraper class with red team capabilities"""
    
    def __init__(self, target_url, verbose=False, stealth=True):
        self.target_url = target_url
        self.verbose = verbose
        self.stealth = stealth
        self.session = requests.Session()
        self.visited_urls = set()
        self.results = defaultdict(list)
        
        # User agents for stealth
        self.user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Safari/605.1.15'
        ]
        
    def log(self, message, level="INFO"):
        """Log messages with timestamp"""
        if self.verbose or level == "ERROR":
            timestamp = datetime.now().strftime("%H:%M:%S")
            print(f"[{timestamp}] [{level}] {message}")
    
    def get_random_user_agent(self):
        """Return random user agent for stealth"""
        return random.choice(self.user_agents)
    
    def make_request(self, url, timeout=10):
        """Make HTTP request with error handling"""
        try:
            headers = {}
            if self.stealth:
                headers['User-Agent'] = self.get_random_user_agent()
                time.sleep(random.uniform(0.5, 2.0))  # Rate limiting
            
            response = self.session.get(url, headers=headers, timeout=timeout, verify=True)
            self.log(f"Request to {url} - Status: {response.status_code}")
            return response
        except requests.RequestException as e:
            self.log(f"Request failed for {url}: {str(e)}", "ERROR")
            return None
    
    def extract_emails(self, text):
        """Extract email addresses from text"""
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        return list(set(re.findall(email_pattern, text)))
    
    def extract_phone_numbers(self, text):
        """Extract phone numbers from text"""
        # Multiple patterns for different formats
        patterns = [
            r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b',  # US format
            r'\(\d{3}\)\s*\d{3}[-.]?\d{4}',     # (555) 123-4567
            r'\+\d{1,3}[-.\s]?\d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{1,9}',  # International
        ]
        
        phones = []
        for pattern in patterns:
            phones.extend(re.findall(pattern, text))
        return list(set(phones))
    
    def extract_social_media(self, text):
        """Extract social media links"""
        social_patterns = {
            'twitter': r'twitter\.com/[a-zA-Z0-9_]+',
            'linkedin': r'linkedin\.com/in/[a-zA-Z0-9_-]+',
            'facebook': r'facebook\.com/[a-zA-Z0-9.]+',
            'github': r'github\.com/[a-zA-Z0-9_-]+',
            'instagram': r'instagram\.com/[a-zA-Z0-9_.]+',
        }
        
        social_links = {}
        for platform, pattern in social_patterns.items():
            matches = re.findall(pattern, text)
            if matches:
                social_links[platform] = list(set(matches))
        return social_links
    
    def extract_subdomains(self, text, domain):
        """Extract subdomains from text"""
        subdomain_pattern = rf'\b[a-zA-Z0-9][-a-zA-Z0-9]*\.{re.escape(domain)}\b'
        return list(set(re.findall(subdomain_pattern, text)))
    
    def extract_links(self, html, base_url):
        """Extract all links from HTML"""
        link_pattern = r'href=["\']([^"\']+)["\']'
        links = re.findall(link_pattern, html)
        
        absolute_links = []
        for link in links:
            absolute_url = urljoin(base_url, link)
            absolute_links.append(absolute_url)
        
        return list(set(absolute_links))
    
    def check_xss_vulnerable(self, url):
        """Basic XSS vulnerability check"""
        from urllib.parse import urlencode, urlparse, parse_qs, urlunparse
        
        xss_payloads = [
            '<script>alert(1)</script>',
            '"><script>alert(1)</script>',
            "'\"><script>alert(1)</script>"
        ]
        
        vulnerabilities = []
        parsed = urlparse(url)
        
        for payload in xss_payloads:
            # Handle existing query parameters
            params = parse_qs(parsed.query)
            params['test'] = payload
            
            new_query = urlencode(params, doseq=True)
            test_url = urlunparse((
                parsed.scheme, parsed.netloc, parsed.path,
                parsed.params, new_query, parsed.fragment
            ))
            
            response = self.make_request(test_url)
            
            if response and payload in response.text:
                # Check if payload is in executable context (basic check)
                if '<script>' in response.text and 'alert(1)' in response.text:
                    vulnerabilities.append({
                        'type': 'Potential XSS',
                        'payload': payload,
                        'url': test_url
                    })
                    self.log(f"Potential XSS found with payload: {payload}", "WARNING")
        
        return vulnerabilities
    
    def check_sql_injection(self, url):
        """Basic SQL injection check"""
        from urllib.parse import urlencode, urlparse, parse_qs, urlunparse
        
        sql_payloads = ["'", "' OR '1'='1", "1' OR '1'='1"]
        
        vulnerabilities = []
        parsed = urlparse(url)
        
        for payload in sql_payloads:
            # Handle existing query parameters
            params = parse_qs(parsed.query)
            params['id'] = payload
            
            new_query = urlencode(params, doseq=True)
            test_url = urlunparse((
                parsed.scheme, parsed.netloc, parsed.path,
                parsed.params, new_query, parsed.fragment
            ))
            
            response = self.make_request(test_url)
            
            if response:
                sql_errors = [
                    'SQL syntax',
                    'mysql_fetch',
                    'ORA-',
                    'PostgreSQL',
                    'SQLite',
                ]
                
                for error in sql_errors:
                    if error.lower() in response.text.lower():
                        vulnerabilities.append({
                            'type': 'Potential SQL Injection',
                            'payload': payload,
                            'url': test_url,
                            'error': error
                        })
                        self.log(f"Potential SQLi found with payload: {payload}", "WARNING")
                        break
        
        return vulnerabilities
    
    def scan_target(self, check_vulns=False):
        """Perform comprehensive scan on target"""
        self.log(f"Starting scan on: {self.target_url}")
        
        response = self.make_request(self.target_url)
        if not response:
            self.log("Failed to reach target", "ERROR")
            return None
        
        html = response.text
        parsed_url = urlparse(self.target_url)
        domain = parsed_url.netloc
        
        # Extract information
        self.log("Extracting emails...")
        self.results['emails'] = self.extract_emails(html)
        
        self.log("Extracting phone numbers...")
        self.results['phone_numbers'] = self.extract_phone_numbers(html)
        
        self.log("Extracting social media links...")
        self.results['social_media'] = self.extract_social_media(html)
        
        self.log("Extracting subdomains...")
        self.results['subdomains'] = self.extract_subdomains(html, domain)
        
        self.log("Extracting links...")
        self.results['links'] = self.extract_links(html, self.target_url)
        
        # Vulnerability checks
        if check_vulns:
            self.log("Running vulnerability checks...")
            self.results['xss_vulns'] = self.check_xss_vulnerable(self.target_url)
            self.results['sql_vulns'] = self.check_sql_injection(self.target_url)
        
        return self.results
    
    def print_results(self):
        """Print formatted results"""
        print("\n" + "="*60)
        print(f"🚀 kArma's Web Scraper - Red Team Edition 🏴‍☠️")
        print("="*60)
        print(f"\nTarget: {self.target_url}")
        print(f"Scan Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("="*60)
        
        if self.results['emails']:
            print(f"\n📧 Emails Found ({len(self.results['emails'])}):")
            for email in self.results['emails']:
                print(f"  - {email}")
        
        if self.results['phone_numbers']:
            print(f"\n📞 Phone Numbers Found ({len(self.results['phone_numbers'])}):")
            for phone in self.results['phone_numbers']:
                print(f"  - {phone}")
        
        if self.results['social_media']:
            print(f"\n📱 Social Media Links Found:")
            for platform, links in self.results['social_media'].items():
                print(f"  {platform.upper()}:")
                for link in links:
                    print(f"    - {link}")
        
        if self.results['subdomains']:
            print(f"\n🌐 Subdomains Found ({len(self.results['subdomains'])}):")
            for subdomain in self.results['subdomains']:
                print(f"  - {subdomain}")
        
        if self.results['links']:
            print(f"\n🔗 Links Found ({len(self.results['links'])}):")
            for link in self.results['links'][:20]:  # Show first 20
                print(f"  - {link}")
            if len(self.results['links']) > 20:
                print(f"  ... and {len(self.results['links']) - 20} more")
        
        if 'xss_vulns' in self.results and self.results['xss_vulns']:
            print(f"\n⚠️  Potential XSS Vulnerabilities Found:")
            for vuln in self.results['xss_vulns']:
                print(f"  - Payload: {vuln['payload']}")
                print(f"    URL: {vuln['url']}")
        
        if 'sql_vulns' in self.results and self.results['sql_vulns']:
            print(f"\n⚠️  Potential SQL Injection Vulnerabilities Found:")
            for vuln in self.results['sql_vulns']:
                print(f"  - Payload: {vuln['payload']}")
                print(f"    Error: {vuln['error']}")
                print(f"    URL: {vuln['url']}")
        
        print("\n" + "="*60)
        print("Scan complete! #weareLegion 🚀👽🏴‍☠️")
        print("by kArmaSec")
        print("="*60 + "\n")


def main():
    """Main CLI interface"""
    parser = argparse.ArgumentParser(
        description='kArma\'s Web Scraper - Red Team Edition 🚀🏴‍☠️',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  python karmas_scraper.py -u https://example.com
  python karmas_scraper.py -u https://example.com -v --check-vulns
  python karmas_scraper.py -u https://example.com --no-stealth

#weareLegion - by kArmaSec
        '''
    )
    
    parser.add_argument(
        '-u', '--url',
        required=True,
        help='Target URL to scrape'
    )
    
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Enable verbose output'
    )
    
    parser.add_argument(
        '--no-stealth',
        action='store_true',
        help='Disable stealth mode (no user-agent rotation or rate limiting)'
    )
    
    parser.add_argument(
        '--check-vulns',
        action='store_true',
        help='Enable vulnerability checking (XSS, SQLi)'
    )
    
    args = parser.parse_args()
    
    # Banner
    print("\n" + "="*60)
    print("🚀 kArma's Web Scraper - Red Team Edition 🏴‍☠️")
    print("="*60)
    print("A badass tool for red teamers")
    print("#keepITsimpel #weareLegion")
    print("="*60 + "\n")
    
    try:
        scraper = KarmasScraper(
            target_url=args.url,
            verbose=args.verbose,
            stealth=not args.no_stealth
        )
        
        results = scraper.scan_target(check_vulns=args.check_vulns)
        
        if results:
            scraper.print_results()
        else:
            print("Scan failed. Check your target URL and try again.")
            sys.exit(1)
            
    except KeyboardInterrupt:
        print("\n\n[!] Scan interrupted by user. Exiting...")
        sys.exit(0)
    except Exception as e:
        print(f"\n[ERROR] An error occurred: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
