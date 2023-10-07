from fake_useragent import UserAgent

BOT_NAME = "ad_scraper"

SPIDER_MODULES = ["ad_scraper.spiders"]
NEWSPIDER_MODULE = "ad_scraper.spiders"

# User-Agent setup
USER_AGENT = UserAgent().random

# Download delay setup
DOWNLOAD_DELAY = 1

# Randomize the download delay
RANDOMIZE_DOWNLOAD_DELAY = True

# Obey robots.txt rules (Change based on your needs and the website's terms)
ROBOTSTXT_OBEY = False

# Database configuration
MONGO_URI = 'mongodb://localhost:27017/'
MONGO_DATABASE = 'e-nekretnine'

# Pipelines
ITEM_PIPELINES = {
    'ad_scraper.pipelines.MongoPipeline': 300,
}

# Concurrent requests
CONCURRENT_REQUESTS = 16

# Disable cookies
COOKIES_ENABLED = False

# AutoThrottle setup
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 5
AUTOTHROTTLE_MAX_DELAY = 60
AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0

# HTTP Cache setup
HTTPCACHE_ENABLED = True
HTTPCACHE_EXPIRATION_SECS = 3600  # Cache for 1 hour
HTTPCACHE_DIR = "httpcache"

# Retry Middleware
RETRY_ENABLED = True
RETRY_TIMES = 3  # Total number of retries for a failed request
RETRY_HTTP_CODES = [500, 502, 503, 504, 408]  # Retry on these HTTP codes

# Future-proof settings
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"

# Logging
LOG_ENABLED = True
LOG_LEVEL = 'INFO'
