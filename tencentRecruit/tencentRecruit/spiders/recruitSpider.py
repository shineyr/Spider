 # -*- coding: UTF-8 -*-
############################################################################
#程序：腾讯招聘网站爬虫
#功能：抓取腾讯社招官网的所有职位信息
#时间：2016/05/31
#作者：yr
#############################################################################

import scrapy,re,json,sys
from scrapy.selector import Selector

#导入框架内置基本类class scrapy.spider.Spider
try:
	from scrapy.spider import Spider
except:
	from scrapy.spider import BaseSpider as Spider

#导入爬取一般网站常用类class scrapy.contrib.spiders.CrawlSpider和规则类Rule
from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.contrib.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy.utils.response import get_base_url
from scrapy.utils.url import urljoin_rfc

from tencentRecruit.items import PositionItem

#自定义
from scrapy import log

def warn(msg):
    log.msg(str(msg), level=log.WARNING)


def info(msg):
    log.msg(str(msg), level=log.INFO)


def debug(msg):
    log.msg(str(msg), level=log.DEBUG)

#设置编码格式
reload(sys) 
sys.setdefaultencoding('gbk')

#自定义爬虫类
class recruitSpider(CrawlSpider):
	name = "tencentRecruitSpider"
	allowed_domains = ["tencent.com"]
	#爬虫的入口网页url
	start_urls = ["http://hr.tencent.com/position.php"]
	#根据任意一页职位url自定义爬取规则（http://hr.tencent.com/position.php?&start=1370#a）
	rules = [
		Rule(LxmlLinkExtractor(allow=('/position.php\?&start=\d{,4}#a')),follow=True,callback='parseItem')	
	]

	#定义提取网页数据到Items中的实现函数
	def parseItem(self,response):
		items = []
		sel = Selector(response)
		base_url = get_base_url(response)
		sites_even = sel.css('table.tablelist tr.even')
		for site in sites_even:
			item = PositionItem()
			item['name'] = site.css('.l.square a').xpath('text()').extract()[0].encode('gbk')
			relative_url = site.css('.l.square a').xpath('@href').extract()[0]
			item['positionLink'] = urljoin_rfc(base_url, relative_url)
			item['catalog'] = site.css('tr > td:nth-child(2)::text').extract()
			item['workPlace'] = site.css('tr > td:nth-child(4)::text').extract()[0]
			item['number'] = site.css('tr > td:nth-child(3)::text').extract()[0]
			item['releaseTime'] = site.css('tr > td:nth-child(5)::text').extract()[0]
			items.append(item)
		
		sites_odd = sel.css('table.tablelist tr.odd')
		for site in sites_odd:
			item = PositionItem()
			item['name'] = site.css('.l.square a').xpath('text()').extract()[0]
			relative_url = site.css('.l.square a').xpath('@href').extract()[0]
			item['positionLink'] = urljoin_rfc(base_url, relative_url)
			item['catalog'] = site.css('tr > td:nth-child(2)::text').extract()
			item['workPlace'] = site.css('tr > td:nth-child(4)::text').extract()[0]
			item['number'] = site.css('tr > td:nth-child(3)::text').extract()[0] 
			item['releaseTime'] = site.css('tr > td:nth-child(5)::text').extract()[0]
			items.append(item)
		info('parsed '+str(response))
		return items

	def _process_request(self,request):
		info('process '+str(request))
		return request
	
