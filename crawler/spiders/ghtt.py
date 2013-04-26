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
    name = 'ghtt'
    start_urls = [
            "http://bbs.ghtt.net/forum.php",
            ]
    is_start = True

    def parse(self, response):
        hxs=HtmlXPathSelector(response)
        for urlid in hxs.select("//a/@href").re("thread-\d+"):
            yield Request("http://bbs.ghtt.net/archiver/tid-"+urlid[7::]+".html",callback=self.parse_page)

    def parse_page(self,response):
        items = []
        hxs=HtmlXPathSelector(response)
        title = hxs.select("//title/text()").extract()[0]
        url = response.url
        auther = hxs.select("//div[@id=\"content\"]/p[@class=\"author\"]/text()").extract()[0]
        content = "".join(hxs.select("//div[@id='content']/text()").extract())
        print content



        #print response.url

