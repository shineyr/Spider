# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item,Field


class CsdnspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class PaperItem(Item):
	title = Field() #博文标题
	link = Field() #博文链接
	writeTime = Field() #日志编写时间
	readers = Field() #阅读次数
	comments = Field() #评论数


