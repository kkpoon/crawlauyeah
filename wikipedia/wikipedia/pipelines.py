# -*- coding: utf-8 -*-

import codecs
from wikipedia.items import WikipediaWikiLinkItem, WikipediaWikiCatItem


class WikipediaLinkCSVPipeline(object):
    def __init__(self):
        self.file = codecs.open("links.csv", "w", "utf-8")

    def process_item(self, item, spider):
        if isinstance(item, WikipediaWikiLinkItem):
            self.file.write(u",".join(dict(item).values()) + "\n")
        return item

class WikipediaCatCSVPipeline(object):
    def __init__(self):
        self.file = codecs.open("cats.csv", "w", "utf-8")

    def process_item(self, item, spider):
        if isinstance(item, WikipediaWikiCatItem):
            self.file.write(u",".join(dict(item).values()) + "\n")
        return item
