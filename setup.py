#!/usr/bin/env python3
"""
Setup script for kArma's Web Scraper - Red Team Edition
"""

from setuptools import setup, find_packages
import os

# Read the README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Read requirements
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="karmas-webscraper",
    version="1.0.0",
    author="kArmaSec",
    description="A badass web scraping tool for red teamers with OSINT and vulnerability scanning capabilities",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Karma4488/kArmas_websCRapeR",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Information Technology",
        "Intended Audience :: System Administrators",
        "Topic :: Security",
        "Topic :: Internet :: WWW/HTTP",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.7",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "karmas-scraper=karmas_scraper.scraper:main",
        ],
    },
    keywords="red-team osint reconnaissance web-scraper security pentesting crypto-wallet vulnerability-scanner",
    project_urls={
        "Bug Reports": "https://github.com/Karma4488/kArmas_websCRapeR/issues",
        "Source": "https://github.com/Karma4488/kArmas_websCRapeR",
    },
)
