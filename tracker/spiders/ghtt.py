#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import re
import json

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request,FormRequest
from tracker.items import *

class Spider(CrawlSpider):
    name = 'ghtt'
    start_urls = [
            #"http://bbs.ghtt.net/archiver/",
            "http://bbs.ghtt.net/archiver/fid-1.html",
            #"http://bbs.ghtt.net/forum.php",
            ]
    is_start = True

    def parse(self, response):
        hxs=HtmlXPathSelector(response)
        #for urlid in hxs.select("//a/@href").re("thread-\d+"):
        #    yield Request("http://bbs.ghtt.net/archiver/tid-"+urlid[7::]+".html",callback=self.parse_page)
        for url in hxs.select("//a/@href").re(ur"fid-\d+.html.*"):
            print url
            #yield Request("http://bbs.ghtt.net/archiver/"+url,callback=self.parse)
        for url in hxs.select("//a/@href").re(ur"tid-\d+.html.*"):
            print url
            yield Request("http://bbs.ghtt.net/archiver/"+url,callback=self.parse_page)

    def parse_page(self,response):
        item = LongItem()
        hxs=HtmlXPathSelector(response)
        item['title'] = hxs.select("//title/text()").extract()[0]
        item['url'] = response.url
        item['username'] = hxs.select("//div[@id=\"content\"]/p[@class=\"author\"]/text()").extract()[0]
        item['content'] = "".join(hxs.select("//div[@id='content']/text()").extract())
        item['tags'] = hxs.select("//meta[@name=\"keywords\"]/@content").extract()[0]
        return item

        #print response.url

