# -*- coding: utf-8 -*-

# Scrapy settings for scrapy_visions project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#
 
BOT_NAME = 'scrapy_visions'

SPIDER_MODULES = ['scrapy_visions.spiders']
NEWSPIDER_MODULE = 'scrapy_visions.spiders'

ITEM_PIPELINES = {
    'scrapy_visions.pipelines.ScrapyVisionsPipeline': 300,
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'scrapy_visions (+http://www.yourdomain.com)'