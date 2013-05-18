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
    name = 'sns'
    start_urls = [
            'http://3g.renren.com/?guid='
            #'http://rss.sina.com.cn/blog/astro/xz.xml'
            ]

    def parse(self, response):

        return item
