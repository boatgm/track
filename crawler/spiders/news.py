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
from crawler.items import *

class Spider(CrawlSpider):
    name = 'news'
    start_urls =[
            'http://m.sohu.com/',
            ]
    def parse(self,response):
        hxs = HtmlXPathSelector(response)
        for url in list(set(hxs.select("//a/@href").re("/n/.*/"))):
            yield Request("http://m.sohu.com"+url+"?show_rest_pages=1",callback=self.parse_content)

    def return_item(self,item):
        return items

    def parse_content(self,response):
        item = NewsItem()
        hxs = HtmlXPathSelector(response)
        item['url'] = response.url
        item['md5'] = md5(item['url']).hexdigest()
        item['title'] = hxs.select("//h2[@class=\"a3\"]/text()").extract()[0].strip()
        item['date'] = hxs.select("//p[@class=\"a3 f12 c2 pb1\"]/text()").extract()[0].strip()
        item['content'] = hxs.select("//div[@class=\"w1 Text\"]/div").extract()[0].strip()
        #item['tags'] = hxs.select("//meta[@name=\"keywords\"]/@content").extract()[0].split()
        item['images'] = hxs.select("//img/@src").re(ur"/[^/]*\.jpg")
        return item

    def parse__comment(self,response):
        pass
