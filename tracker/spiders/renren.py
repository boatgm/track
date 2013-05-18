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
    name = 'renren'
    start_urls = [
            "http://3g.renren.com/home.do?sid=Ai7aWGlKpWAWvdrMYIif2K&bm=300619604_cb39eac15261bb8e1d91ee8a48b9191c_1366941599215&f=1&w=1&",
            #"http://3g.renren.com/stories.do?htf=470&sid=Ai7aWGlKpWAWvdrMYIif2K&92ax4e",
            #"http://3g.renren.com/home.do?htf=1&sid=Ai7aWGlKpWAWvdrMYIif2K&d9suoy",
            ]
    is_start = True

    def parse(self, response):
        items = []
        hxs=HtmlXPathSelector(response)

        for p in hxs.select("//div[@class=\"list\"]/div"):
            try:
                item = SnsItem()
                item['platform'] = 'renren'
                item['uid'] = p.select("a/@name").extract()[0]
                item['author'] = p.select("a/text()").extract()[0]
                item['content'] = p.select("text()").extract()[0]
                items.append(item)
            except :
                pass
        return items

