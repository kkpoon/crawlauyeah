# -*- coding: utf-8 -*-
import scrapy
from wikipedia.items import WikipediaWikiLinkItem, WikipediaWikiCatItem

class WikiLinkSpider(scrapy.Spider):
    name = "wikilink"
    allowed_domains = ["wikipedia.org"]

    def __init__(self, startpage="Wikipedia:首页", language="en", locale="wiki"):
        self.start_urls = (
            'https://%s.wikipedia.org/%s/%s' % (language, locale, startpage),
        )

    def parse(self, response):
        title = response.xpath("//h1[@class='firstHeading']/text()").extract()[0]
        for sel in response.xpath('//a[@class="mw-redirect"]'):
            item = WikipediaWikiLinkItem()
            path = sel.xpath("@href").extract()[0]
            link = response.urljoin(path)
            item["refer"] = title
            item["title"] = sel.xpath("@title").extract()[0]
            item["link"] = link
            yield item
        for sel in response.xpath('//div[@class="catlinks"]//ul/li/a'):
            item2 = WikipediaWikiCatItem()
            item2["category"] = sel.xpath("text()").extract()[0]
            item2["title"] = title
            yield item2
        for sel in response.xpath('//a[@class="mw-redirect"]'):
            link = sel.xpath("@href").extract()[0]
            url = response.urljoin(link)
            yield scrapy.Request(url, callback=self.parse)
