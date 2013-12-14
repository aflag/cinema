# Scrapy settings for cinema project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'cinema'

SPIDER_MODULES = ['cinema.spiders']
NEWSPIDER_MODULE = 'cinema.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'cinema (+http://www.yourdomain.com)'

ITEM_PIPELINES = {
    'cinema.pipelines.NormalizePipeline': 250,
    'cinema.pipelines.CinemaPipeline': 500,
}
