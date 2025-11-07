AUTHOR = 'Michael O'
SITENAME = 'MattersEarthly'
SITEURL = "http://localhost:8000'"

PATH = "content"
TIMEZONE = 'Europe/Helsinki'
DEFAULT_LANG = 'en'

ARTICLE_PATHS = ['posts']
PAGE_PATHS = ['pages']
STATIC_PATHS = ['images', 'extra', 'static']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}}

# ----OUTPUT for local testing ----
OUTPUT_PATH = 'output/'

# ---- Theme and layout ----
# Options: cerulean, cosmo, flatly, journal, lumen, readable, simplex, spacelab, united, yeti
THEME = 'themes/pelican-bootstrap3'
BOOTSTRAP_THEME = 'flatly'
HIDE_SIDEBAR = True
DISPLAY_PAGES_ON_MENU = True
PAGE_ORDER_BY = 'order'
DEFAULT_PAGINATION = 5
PAGINATION PATTERNS = (
    (1, '{base_name}/index.html', '{base_name}/index.html'),
    (2, '{base_name}/page/{number}/index.html', '{base_name}/page/{number}/index.html'),
)


TYPOGRIFY = True

 # ---- Article / page layout ----
SUMMARY_MAX_LENGTH = 50

DEFAULT_DATE_FORMAT = '%B %d, %Y' # ('%-d/%-m/%Y')

# ---- Navbar / Header ----
SITETITLE = 'MattersEarthly'
#SITESUBTITLE = 'Your tagline or research area'
#SITESUBTEXT = 'Digital Health · ICT4D · Data Science'
#SITELOGO = 'images/profile.png'  # Optional — must exist in content/images/
SITELOGO_SIZE = 50
BANNER = 'images/banner.jpg'  # Optional banner at top

# ---- Static files ----
STATIC_PATHS = ['extra', 'images']
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    'extra/robots.txt': {'path': 'robots.txt'}
}

# ---- Plugins ----
PLUGIN_PATHS = ['plugins']
PLUGINS = ['i18n_subsites', 'series', 'tag_cloud', 'liquid_tags.youtube', 'render_math']


DIRECT_TEMPLATES = ('index','tags', 'categories', 'authors', 'archives')

 #---- Internationalization ----
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
I18N_TEMPLATES_LANG = 'en'


CUSTOM_CSS = 'static/custom.css'
CUSTOM_JS = 'static/custom.js'

# ---- Footer / Social ----
SOCIAL = (('linkedin', 'https://www.linkedin.com/in/michaeloduor'),)

# ---- Feed generation ----
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

"""
# ---- URLs / Permalinks ----
ARTICLE_URL = 'posts/{slug}.html'
ARTICLE_SAVE_AS = 'posts/{slug}.html'
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'

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

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
"""