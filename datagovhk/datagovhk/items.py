# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FehdLicenseItem(scrapy.Item):
    updatedAt = scrapy.Field()
    department = scrapy.Field()
    licenseType = scrapy.Field()
    district = scrapy.Field()
    licenseNo = scrapy.Field()
    owner = scrapy.Field()
    address= scrapy.Field()
    info = scrapy.Field()
    expireDate = scrapy.Field()
