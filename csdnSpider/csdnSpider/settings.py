# -*- coding: utf-8 -*-

# Scrapy settings for csdnSpider project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'csdnSpider'

SPIDER_MODULES = ['csdnSpider.spiders']
NEWSPIDER_MODULE = 'csdnSpider.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'csdnSpider (+http://www.yourdomain.com)'
ITEM_PIPELINES = {
    'csdnSpider.pipelines.JsonWithEncodingCSDNPipeline': 300,
}

LOG_LEVEL = 'INFO'

