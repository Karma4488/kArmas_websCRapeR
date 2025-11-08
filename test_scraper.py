#!/usr/bin/env python3
"""
Test script for kArma's Web Scraper
Tests the core functionality without requiring network access
"""

import sys
from karmas_scraper import KarmasScraper

def test_email_extraction():
    """Test email extraction"""
    scraper = KarmasScraper("https://example.com", verbose=False)
    
    test_text = """
    Contact us at support@example.com or admin@test.org
    You can also reach sales@company.net for business inquiries.
    """
    
    emails = scraper.extract_emails(test_text)
    print("Testing email extraction...")
    print(f"  Found {len(emails)} emails: {emails}")
    assert len(emails) == 3
    assert "support@example.com" in emails
    print("  ✓ Email extraction working!")
    

def test_phone_extraction():
    """Test phone number extraction"""
    scraper = KarmasScraper("https://example.com", verbose=False)
    
    test_text = """
    Call us at 555-123-4567 or 555.987.6543
    Alternative: 5551112222
    International: +1-555-123-4567
    US Format: (555) 123-4567
    """
    
    phones = scraper.extract_phone_numbers(test_text)
    print("\nTesting phone extraction...")
    print(f"  Found {len(phones)} phone numbers: {phones}")
    assert len(phones) >= 3
    print("  ✓ Phone extraction working!")


def test_social_media_extraction():
    """Test social media link extraction"""
    scraper = KarmasScraper("https://example.com", verbose=False)
    
    test_text = """
    Follow us on twitter.com/example
    Connect on linkedin.com/in/johndoe
    Like us on facebook.com/ourpage
    Check our code at github.com/karmaSec
    Photos on instagram.com/ourphotos
    """
    
    social = scraper.extract_social_media(test_text)
    print("\nTesting social media extraction...")
    print(f"  Found {len(social)} platforms: {list(social.keys())}")
    assert 'twitter' in social
    assert 'linkedin' in social
    assert 'github' in social
    print("  ✓ Social media extraction working!")


def test_subdomain_extraction():
    """Test subdomain extraction"""
    scraper = KarmasScraper("https://example.com", verbose=False)
    
    test_text = """
    Visit api.example.com for API docs
    Check mail.example.com for email
    See blog.example.com for updates
    """
    
    subdomains = scraper.extract_subdomains(test_text, "example.com")
    print("\nTesting subdomain extraction...")
    print(f"  Found {len(subdomains)} subdomains: {subdomains}")
    assert len(subdomains) == 3
    # Test assertion: checking if extracted subdomain matches expected value
    assert "api.example.com" in subdomains
    print("  ✓ Subdomain extraction working!")


def test_link_extraction():
    """Test link extraction"""
    scraper = KarmasScraper("https://example.com", verbose=False)
    
    test_html = """
    <html>
    <a href="/about">About</a>
    <a href="/contact">Contact</a>
    <a href="https://external.com">External</a>
    <a href="/page">Page</a>
    </html>
    """
    
    links = scraper.extract_links(test_html, "https://example.com")
    print("\nTesting link extraction...")
    print(f"  Found {len(links)} links: {links}")
    assert len(links) >= 3
    print("  ✓ Link extraction working!")


def main():
    """Run all tests"""
    print("="*60)
    print("🚀 Testing kArma's Web Scraper - Red Team Edition 🏴‍☠️")
    print("="*60)
    
    try:
        test_email_extraction()
        test_phone_extraction()
        test_social_media_extraction()
        test_subdomain_extraction()
        test_link_extraction()
        
        print("\n" + "="*60)
        print("✓ All tests passed! The scraper is badass and ready! 💪")
        print("#weareLegion #keepITsimpel")
        print("by kArmaSec")
        print("="*60)
        
        return 0
    except AssertionError as e:
        print(f"\n✗ Test failed: {str(e)}")
        return 1
    except Exception as e:
        print(f"\n✗ Error during testing: {str(e)}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
