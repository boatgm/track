#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import re
import json

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request,FormRequest
from crawler.items import *

class Spider(CrawlSpider):
    name = 'qzone'
    start_urls = [
            "http://info60.z.qq.com/feeds_friends.jsp?B_UID=502348587&sid=Aejr0WVmNW87oQy6fnwOzf0D&type=taotao",
            ]
    is_start = True

    def parse(self, response):
        items = []
        hxs=HtmlXPathSelector(response)

        for p in hxs.select("//div[@class=\"spacing-5 border-btm bg-alter\"]/p[1]"):
            try:
                p.select("a/@href").re("B_UID=\d+")[0][6:]
                p.select("a/text()").extract()[0]
                print p.select("text()").extract()[0]
            except :
                pass

        for p in hxs.select("//div[@class=\"spacing-5 border-btm\"]/p[1]"):
            try:
                p.select("a/@href").re("B_UID=\d+")[0][6:]
                p.select("a/text()").extract()[0]
                print p.select("text()").extract()[0]
            except:
                pass

