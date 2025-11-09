#!/usr/bin/env python3
"""
Professionelt scraper-script (requests + BeautifulSoup).
 scape.robots.txt 
"""
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import time
import logging
import sys
import os

# Konfiguration
BASE_URL = "https://btc-net.bg"
OUTPUT_DIR = "index.html"
USER_AGENT = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
              "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
RATE_DELAY_SECONDS = 1.5   # respekter siden ved at rate-limit
MAX_PAGES = 20             # sikkerhedsgrænse: maks antal sider der hentes

# Logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s: %(message)s")

session = requests.Session()
session.headers.update({"User-Agent": USER_AGENT, "Accept": "text/html,application/xhtml+xml"})

def allowed_by_robots(base_url, path="/"):
    try:
        r = session.get(urljoin(base_url, "/robots.txt"), timeout=10)
        if r.status_code != 200:
            logging.info("robots.txt ikke fundet (status %s). Fortsætter—vær forsigtig.", r.status_code)
            return True
        txt = r.text.lower()
        # Meget simpel robots-parser: afvis hvis "disallow: /" eller disallow rules for "*"
        if "disallow: /" in txt:
            logging.warning("robots.txt indeholder 'Disallow: /' — scraping ikke tilladt.")
            return False
        return True
    except Exception as e:
        logging.warning("Fejl ved hentning af robots.txt: %s — antager tilladt (men bekræft selv).", e)
        return True

def fetch(url):
    try:
        r = session.get(url, timeout=20)
        r.raise_for_status()
        return r.text
    except requests.HTTPError as e:
        logging.error("HTTP error for %s : %s", url, e)
    except requests.RequestException as e:
        logging.error("Request error for %s : %s", url, e)
    return None

def save_html(url, html):
    parsed = urlparse(url)
    path = parsed.path.strip("/") or "index.html"
    # sanitize path to filesystem
    filename = path.replace("/", "_")
    if not filename.endswith(".html"):
        filename += ".html"
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    outpath = os.path.join(OUTPUT_DIR, filename)
    with open(outpath, "w", encoding="utf-8") as f:
        f.write(html)
    logging.info("Gemte %s -> %s", url, outpath)

def extract_links(base_url, html):
    soup = BeautifulSoup(html, "html.parser")
    links = set()
    for a in soup.find_all("a", href=True):
        href = a["href"].strip()
        # ignore mailto, tel osv.
        if href.startswith("mailto:") or href.startswith("tel:") or href.startswith("javascript:"):
            continue
        full = urljoin(base_url, href)
        if urlparse(full).netloc == urlparse(base_url).netloc:
            links.add(full.split("#")[0])
    return links

def main():
    if not allowed_by_robots(BASE_URL):
        logging.error("robots.txt forhindrer crawling. Afslutter.")
        sys.exit(1)

    to_visit = [BASE_URL]
    visited = set()
    count = 0

    while to_visit and count < MAX_PAGES:
        url = to_visit.pop(0)
        if url in visited:
            continue
        logging.info("Henter %s", url)
        html = fetch(url)
        if html is None:
            visited.add(url)
            continue
        save_html(url, html)
        visited.add(url)
        count += 1

        # udtræk links internt
        links = extract_links(BASE_URL, html)
        for l in sorted(links):
            if l not in visited and l not in to_visit and len(to_visit) + count < MAX_PAGES:
                to_visit.append(l)

        logging.debug("Queue størrelse: %d", len(to_visit))
        time.sleep(RATE_DELAY_SECONDS)

    logging.info("Færdig. Hentede %d sider. Output i '%s'.", count, OUTPUT_DIR)

if __name__ == "__main__":
    main()


#!/usr/bin/env python3
"""
Professionelt scraper-script (requests + BeautifulSoup).
Respekter robots.txt og kør med ansvar.
Made by kArmasec
"""
import requests
from requests.auth import HTTPBasicAuth
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import time
import logging
import sys
import os

# Metadata
MADE_BY = "kArmasec"
SCRIPT_NAME = "kArmasec_ultimative_webzSCraper.py"
SCRIPT_VERSION = "1.1"

# Konfigurationu
BASE_URL = "https://target.com"
OUTPUT_DIR = "index.html"
USER_AGENT = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
              "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
RATE_DELAY_SECONDS = 1.5
MAX_PAGES = 20
MAX_RETRIES = 2
RETRY_BACKOFF = 2  # multiplicativ backoff i sekunder

# Mulighed for legitime credentials (sæt som miljøvariable hvis påkrævet)
SCRAPE_USER = os.getenv("SCRAPE_USER")
SCRAPE_PASS = os.getenv("SCRAPE_PASS")
SCRAPE_BEARER = os.getenv("SCRAPE_BEARER")

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s: %(message)s")
logging.info("%s v%s - startet. Udviklet af %s.", SCRIPT_NAME, SCRIPT_VERSION, MADE_BY)

session = requests.Session()
session.headers.update({"User-Agent": USER_AGENT, "Accept": "text/html,application/xhtml+xml"})

# Hvis basic-auth oplysninger er sat, tilføj dem til session (legitim brug)
if SCRAPE_USER and SCRAPE_PASS:
    session.auth = HTTPBasicAuth(SCRAPE_USER, SCRAPE_PASS)
    logging.info("Basic auth konfigureret via miljøvariable.")

# Hvis bearer token er sat, sæt Authorization header
if SCRAPE_BEARER:
    session.headers.update({"Authorization": f"Bearer {SCRAPE_BEARER}"})
    logging.info("Bearer token konfigureret via miljøvariable.")

def allowed_by_robots(base_url, path="/"):
    try:
        r = session.get(urljoin(base_url, "/robots.txt"), timeout=10)
        if r.status_code != 200:
            logging.info("robots.txt ikke fundet (status %s). Fortsætter—vær forsigtig.", r.status_code)
            return True
        txt = r.text.lower()
        if "disallow: /" in txt:
            logging.warning("robots.txt indeholder 'Disallow: /' — scraping ikke tilladt.")
            return False
        return True
    except Exception as e:
        logging.warning("Fejl ved hentning af robots.txt: %s — antager tilladt (men bekræft selv).", e)
        return True

def fetch(url):
    """Hent URL med simpel retry og korrekt håndtering af 401/403."""
    last_exc = None
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            r = session.get(url, timeout=20, allow_redirects=True)
            if r.status_code == 401:
                logging.error("401 Unauthorized for %s. Ingen gyldige credentials eller token. (WWW-Authenticate: %s)",
                              url, r.headers.get("WWW-Authenticate"))
                return None
            if r.status_code == 403:
                logging.error("403 Forbidden for %s. Adgang nægtet. Respekter sidens politik eller få adgang via officielle kanaler.", url)
                return None
            if 400 <= r.status_code < 500:
                logging.error("Client error %s for %s. Afslutter hentning af denne URL.", r.status_code, url)
                return None
            if 500 <= r.status_code < 600:
                logging.warning("Server error %s for %s — attempt %d/%d.", r.status_code, url, attempt, MAX_RETRIES)
                time.sleep(RETRY_BACKOFF ** attempt)
                continue

            r.raise_for_status()
            return r.text
        except requests.HTTPError as e:
            logging.error("HTTP error for %s : %s", url, e)
            last_exc = e
            break
        except requests.RequestException as e:
            logging.warning("RequestException for %s: %s — attempt %d/%d", url, e, attempt, MAX_RETRIES)
            last_exc = e
            time.sleep(RETRY_BACKOFF ** attempt)
    logging.error("Kunne ikke hente %s efter %d forsøg. Sidste fejl: %s", url, MAX_RETRIES, last_exc)
    return None

def save_html(url, html):
    parsed = urlparse(url)
    path = parsed.path.strip("/") or "index.html"
    filename = path.replace("/", "_")
    if not filename.endswith(".html"):
        filename += ".html"
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    outpath = os.path.join(OUTPUT_DIR, filename)
    # Indsæt en sporbar HTML-kommentar øverst i gemt fil
    header_comment = f"<!-- Scraped by {MADE_BY} using {SCRIPT_NAME} v{SCRIPT_VERSION} -->\n"
    with open(outpath, "w", encoding="utf-8") as f:
        f.write(header_comment)
        f.write(html)
    logging.info("Gemte %s -> %s", url, outpath)

def extract_links(base_url, html):
    soup = BeautifulSoup(html, "html.parser")
    links = set()
    for a in soup.find_all("a", href=True):
        href = a["href"].strip()
        if href.startswith("mailto:") or href.startswith("tel:") or href.startswith("javascript:"):
            continue
        full = urljoin(base_url, href)
        if urlparse(full).netloc == urlparse(base_url).netloc:
            links.add(full.split("#")[0])
    return links

def main():
    if not allowed_by_robots(BASE_URL):
        logging.error("robots.txt forhindrer crawling. Afslutter.")
        sys.exit(1)

    to_visit = [BASE_URL]
    visited = set()
    count = 0

    while to_visit and count < MAX_PAGES:
        url = to_visit.pop(0)
        if url in visited:
            continue
        logging.info("Henter %s", url)
        html = fetch(url)
        if html is None:
            visited.add(url)
            continue
        save_html(url, html)
        visited.add(url)
        count += 1

        links = extract_links(BASE_URL, html)
        for l in sorted(links):
            if l not in visited and l not in to_visit and len(to_visit) + count < MAX_PAGES:
                to_visit.append(l)

        logging.debug("Queue størrelse: %d", len(to_visit))
        time.sleep(RATE_DELAY_SECONDS)

    logging.info("Færdig. Hentede %d sider. Output i '%s'. Udviklet af %s.", count, OUTPUT_DIR, MADE_BY)

if __name__ == "__main__":
    main()
