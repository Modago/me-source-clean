AUTHOR = 'Michael O'
SITENAME = 'MattersEarthly'
SITEURL = ''

DEFAULT_DATE_FORMAT = ('%-d/%-m/%Y')  # '%B %d, %Y'

PATH = 'content/'
TIMEZONE = 'Europe/Helsinki'
DEFAULT_LANG = 'en'

ARTICLE_PATHS = ['posts']
PAGE_PATHS = ['pages']

# ---- Static files ----
STATIC_PATHS = ['images', 'extra', 'static']
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
}

CUSTOM_CSS = 'static/custom.css'
CUSTOM_JS = 'static/custom.js'

# --- Development settings ---
RELATIVE_URLS = True       # Use relative URLs for local preview
DELETE_OUTPUT_DIRECTORY = False  # Keep output folder in dev
OUTPUT_PATH = "output/"    # Local dev output folder

# ---- Theme and layout ----
# Options: cerulean, cosmo, flatly, journal, lumen, readable, simplex, spacelab, united, yeti
THEME = 'themes/pelican-bootstrap3'
BOOTSTRAP_THEME = 'flatly'
HIDE_SIDEBAR = True
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False
PAGE_ORDER_BY = 'order'
DEFAULT_PAGINATION = 5
PAGINATION_PATTERNS = (
    (1, '{base_name}/index.html', '{base_name}/index.html'),
    (2, '{base_name}/page/{number}/index.html', '{base_name}/page/{number}/index.html'),
)

# Banner configuration (blog only)
BANNER = 'images/banner.jpg'
BANNER_SUBTITLE = 'Musings on Research, Technology, and Life'
BANNER_ALL_PAGES = False

# Logo and favicon
#SITELOGO = 'images/logo.png'
#SITELOGO_SIZE = 32
FAVICON = 'images/favicon.png'

# ==========================================
#  PLUGINS
# ==========================================
PLUGIN_PATHS = ['plugins']
PLUGINS = [
    'i18n_subsites',
    'series',
    'tag_cloud',
    'liquid_tags.youtube',
    'render_math',
]

# Plugin-specific settings
#---- Internationalization ----
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
I18N_TEMPLATES_LANG = 'en'

# For render_math (if using MathJax)
MATH_JAX = {'align': 'center', 'indent': '0em'}

# For tag_cloud (optional)
TAG_CLOUD_MAX_ITEMS = 100
TAG_CLOUD_SORTING = 'alphabetically'

# ---- Social ----
SOCIAL = (('linkedin', 'https://www.linkedin.com/in/michaeloduor'),)

# ==========================================
#  FOOTER
# ==========================================
import datetime
CURRENT_YEAR = datetime.date.today().year

FOOTER_TEXT = f"""
<p>© {CURRENT_YEAR} MattersEarthly. Content licensed under a 
<a href="https://creativecommons.org/licenses/by-nc-sa/4.0/" target="_blank">
Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>,
except where indicated otherwise.</p>
"""

# ---- URLs / Permalinks ----
ARTICLE_URL = 'posts/{slug}.html'
ARTICLE_SAVE_AS = 'posts/{slug}.html'
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'

"""
# TYPOGRIFY = True

# DIRECT_TEMPLATES = ('index','tags', 'categories', 'authors', 'archives')

# Menu
MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),)


NOTEBOOK_DIR = 'notebooks'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# ---- Feed generation ----
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'

 # ---- Article / page layout ----
# SUMMARY_MAX_LENGTH = 50
"""