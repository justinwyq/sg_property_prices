# -*- coding: utf-8 -*-

# Scrapy settings for demo_project project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'propertyguru'

SPIDER_MODULES = ['propertyguru.spiders']
NEWSPIDER_MODULE = 'propertyguru.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'demo_project (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#'Accept': '*/*',
'Authority': 'www.propertyguru.com.sg',
'cookie':'__cfduid=d38814a138894d1132e7bec103e3d568a1586193858; Visitor=179169de-757d-4b64-ae98-40fdea494ae9; D_ZID=B7A1599E-43D6-3117-BE65-110E760E8DD6; D_ZUID=F814041E-7584-3FA4-9F8E-784D2317EC86; D_HID=A674805C-4FEC-3936-86AC-0316610A7755; D_SID=49.245.118.179:N2M67QgaOIc343KpYMfwwJDao9f1M6gA2JP0DsKgb8U; sixpack_client_id=32923C6B-9D33-C208-7E99-366E18E0273E; ajs_user_id=null; ajs_group_id=null; ajs_anonymous_id=%226d336f52-7f0a-416c-b1df-97b653d26e1d%22; PHPSESSID2=jir3oa3g4po0i5r4ol3o3tu4l4; D_IID=97582CB3-CB05-3AF6-B309-D22D1190626C; D_UID=A999C936-C8C4-3C15-9664-E60E8486FC0A',
'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
#'cookie': '__cfduid=d38814a138894d1132e7bec103e3d568a1586193858; Visitor=179169de-757d-4b64-ae98-40fdea494ae9; D_ZID=B7A1599E-43D6-3117-BE65-110E760E8DD6; D_ZUID=F814041E-7584-3FA4-9F8E-784D2317EC86; D_HID=A674805C-4FEC-3936-86AC-0316610A7755; D_SID=49.245.118.179:N2M67QgaOIc343KpYMfwwJDao9f1M6gA2JP0DsKgb8U; sixpack_client_id=32923C6B-9D33-C208-7E99-366E18E0273E; ajs_user_id=null; ajs_group_id=null; ajs_anonymous_id=%226d336f52-7f0a-416c-b1df-97b653d26e1d%22; PHPSESSID2=jir3oa3g4po0i5r4ol3o3tu4l4; D_IID=97582CB3-CB05-3AF6-B309-D22D1190626C; D_UID=A999C936-C8C4-3C15-9664-E60E8486FC0A',
'referrer': 'https://www.propertyguru.com.sg/property-for-sale',
#'user-agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36",
'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'demo_project.middlewares.DemoProjectSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'demo_project.middlewares.DemoProjectDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'demo_project.pipelines.DemoProjectPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
