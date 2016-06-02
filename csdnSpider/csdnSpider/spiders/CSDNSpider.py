# -*- coding: UTF-8 -*-
############################################################################
# 程序：CSDN博客爬虫
# 功能：抓取我的CSDN全部博文
# 时间：2016/06/01
# 作者：yr
#############################################################################

import scrapy, re, json, sys

# 导入框架内置基本类class scrapy.spider.Spider
try:
    from scrapy.spider import Spider
except:
    from scrapy.spider import BaseSpider as Spider

# 导入爬取一般网站常用类class scrapy.contrib.spiders.CrawlSpider和规则类Rule
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.lxmlhtml import LxmlLinkExtractor

from bs4 import BeautifulSoup
from csdnSpider.items import PaperItem

# 设置编码格式
reload(sys)
sys.setdefaultencoding('utf-8')

add = 0
class CSDNPaperSpider(CrawlSpider):
    name = "csdnSpider"
    allowed_domains = ["csdn.net"]
    # 定义爬虫的入口网页
    start_urls = ["http://blog.csdn.net/fly_yr/article/list/1"]
    # 自定义规则
    rules = [Rule(LxmlLinkExtractor(allow=('/article/list/\d{,2}')), follow=True, callback='parseItem')]

    # 定义提取网页数据到Items中的实现函数
    def parseItem(self, response):
        global add
        items = []
        data = response.body
        soup = BeautifulSoup(data, "html5lib")
        # 找到所有的博文代码模块
        sites = soup.find_all('div', "list_item article_item")
        for site in sites:
            item = PaperItem()
            # 标题、链接、日期、阅读次数、评论个数
            item['title'] = site.find('span', "link_title").a.get_text()
            item['link']= site.find('span', "link_title").a.get('href')
            item['writeTime'] = site.find('span', "link_postdate").get_text()
            item['readers'] = re.findall(re.compile(r'\((.*?)\)'), site.find('span', "link_view").get_text())[0]
            item['comments'] = re.findall(re.compile(r'\((.*?)\)'), site.find('span', "link_comments").get_text())[0]
            add += 1
            items.append(item)
        print("The total number:",add)
        return items

