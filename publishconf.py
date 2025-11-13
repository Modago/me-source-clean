#!/usr/bin/env python
# -*- coding: utf-8 -*- #
"""
Production configuration for Pelican — used when deploying to GitHub Pages.
This builds the fully rendered site with absolute URLs, minified assets, and
custom domain integration.
"""

from __future__ import unicode_literals
import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *

# --- Site URL and Domain ---
SITEURL = "https://mattersearthly.co" 
RELATIVE_URLS = False # absolute paths for production

# --- Basic Output & Paths ---
OUTPUT_PATH = "output_prod/"
DELETE_OUTPUT_DIRECTORY = True

# ---- Feed generation ----
FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Following items are often useful when publishing

# DISQUS_SITENAME = ""
# GOOGLE_ANALYTICS = ""

# --- Final output message ---
print(f"✅ Building production site for {SITEURL} into '{OUTPUT_PATH}'")