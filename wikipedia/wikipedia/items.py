# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WikipediaWikiLinkItem(scrapy.Item):
    refer = scrapy.Field()
    title = scrapy.Field()
    link = scrapy.Field()


class WikipediaWikiCatItem(scrapy.Item):
    title = scrapy.Field()
    category = scrapy.Field()
