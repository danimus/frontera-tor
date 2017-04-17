from frontera.settings.default_settings import MIDDLEWARES

BOT_NAME = 'tor'

SPIDER_MODULES = ['tor.spiders']
NEWSPIDER_MODULE = 'tor.spiders'

USER_AGENT = 'TorCrawler (+http://crawl.danimus.io)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

BACKEND = 'frontera.contrib.backends.sqlalchemy.SQLAlchemyBackend'

SQLALCHEMYBACKEND_ENGINE = 'mysql+mysqldb://root:root@localhost:3306/frontera'
SQLALCHEMYBACKEND_ENGINE_ECHO = False
SQLALCHEMYBACKEND_DROP_ALL_TABLES = False
SQLALCHEMYBACKEND_CLEAR_CONTENT = False

from datetime import timedelta

SQLALCHEMYBACKEND_REVISIT_INTERVAL = timedelta(days=1)

SPIDER_MIDDLEWARES = {
    'frontera.contrib.scrapy.middlewares.seeds.file.FileSeedLoader': 1,
    'frontera.contrib.scrapy.middlewares.schedulers.SchedulerSpiderMiddleware': 1000,
    'scrapy.spidermiddlewares.depth.DepthMiddleware': 1
}

DOWNLOADER_MIDDLEWARES = {
    'frontera.contrib.scrapy.middlewares.schedulers.SchedulerDownloaderMiddleware': 1000,
}

SCHEDULER = 'frontera.contrib.scrapy.schedulers.frontier.FronteraScheduler'

MIDDLEWARES.extend([
    'frontera.contrib.middlewares.domain.DomainMiddleware',
    'frontera.contrib.middlewares.fingerprint.DomainFingerprintMiddleware'
])

ITEM_PIPELINES = {
    'tor.pipelines.DBPipeline': 300,
}

DB_HOST='localhost'
DB_USER='root'
DB_PASSWD='root'
DB_PORT=3306
DB_DB='tor'

#--------------------------------------------------------
# Logging
#--------------------------------------------------------
LOGGING_CONFIG = 'logging.conf'
LOGGING_ENABLED = True
LOGGING_EVENTS_ENABLED = False
LOGGING_MANAGER_ENABLED = False
LOGGING_BACKEND_ENABLED = False
LOGGING_DEBUGGING_ENABLED = False

HTTPERROR_ALLOW_ALL=True
HTTPCACHE_ENABLED = False
REDIRECT_ENABLED = True
COOKIES_ENABLED = False
DOWNLOAD_TIMEOUT = 240
RETRY_ENABLED = False
DOWNLOAD_MAXSIZE = 1 * 1024 * 1024

# auto throttling
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_DEBUG = False
AUTOTHROTTLE_MAX_DELAY = 3.0
AUTOTHROTTLE_START_DELAY = 0.25
RANDOMIZE_DOWNLOAD_DELAY = True

# concurrency
CONCURRENT_REQUESTS = 50
CONCURRENT_REQUESTS_PER_DOMAIN = 3
DOWNLOAD_DELAY = 0.0

LOG_LEVEL = 'INFO'

REACTOR_THREADPOOL_MAXSIZE = 32
DNS_TIMEOUT = 180

# download only base url
DEPTH_LIMIT = 1