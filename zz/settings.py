# -*- coding: utf-8 -*-

# Scrapy settings for zz project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'zz'

SPIDER_MODULES = ['zz.spiders']
NEWSPIDER_MODULE = 'zz.spiders'

ITEM_PIPELINES = {'scrapy.contrib.pipeline.images.ImagesPipeline': 1}
IMAGES_STORE = '/dir'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'zz (+http://www.yourdomain.com)'
