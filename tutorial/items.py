# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field  


class TutorialItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class DmozItem(Item):
	title = scrapy.Field()
	link = scrapy.Field()
	desc = scrapy.Field()


