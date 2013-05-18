#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import re
import urlparse
import json
import requests
from md5 import md5

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.conf import settings
from scrapy.http import Request
from tracker.items import *

class Spider(CrawlSpider):
    name = 'blog'
    start_urls =[
            'http://blog.sina.com.cn/',
            ]
    def parse(self,response):
        hxs = HtmlXPathSelector(response)
        for url in list(set(hxs.select("//a/@href").re("http://blog.sina.com.cn/s/blog_.*\.html"))):
            yield Request(url, callback=self.parse_content)

    def return_item(self,item):
        return items

    def parse_content(self,response):
        hxs = HtmlXPathSelector(response)
        item = BlogItem()
        item['url'] = response.url
        item['md5'] = md5(item['url']).hexdigest()
        item['title'] = hxs.select("//title/text()").extract()[0].strip()
        item['content'] = re.sub("<[^>]*>","",hxs.select("//div[@class=\"articalContent  \"]").extract()[0])
        item['images'] = hxs.select("//div[@class=\"articalContent  \"]").re(ur"/[^/]*\.jpg")
        return item
