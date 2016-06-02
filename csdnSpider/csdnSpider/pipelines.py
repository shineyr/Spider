# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


import scrapy
from scrapy import signals
import json, codecs


class CsdnspiderPipeline(object):
    def process_item(self, item, spider):
        return item

class JsonWithEncodingCSDNPipeline(object):
    def __init__(self):
        self.file = codecs.open('papers.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        writeTime = json.dumps("日期："+str(item['writeTime']),ensure_ascii=False) + "\n"
        title = json.dumps("标题："+str(item['title']),ensure_ascii=False)+ "\n"
        link = json.dumps("链接："+str(item['link']),ensure_ascii=False)+ "\n"
        readers = json.dumps("阅读次数："+str(item['readers']),ensure_ascii=False)+ "\t"
        comments = json.dumps("评论数量："+str(item['comments']),ensure_ascii=False)+ "\n\n"
        line = writeTime + title + link + readers + comments
        self.file.write(line)
        return item

    def spider_closed(self, spider):
        self.file.close()

