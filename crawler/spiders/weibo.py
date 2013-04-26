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
    name = 'weibo'
    start_urls = [
            'https://api.weibo.com/2/statuses/friends_timeline.json?access_token=2.00qeXEHC5wcU_Dc5e1cf3ffcBuQFEE&count=99&page=1',
            'https://api.weibo.com/2/statuses/friends_timeline.json?access_token=2.00qeXEHC5wcU_Dc5e1cf3ffcBuQFEE&count=99&page=2',
            'https://api.weibo.com/2/statuses/friends_timeline.json?access_token=2.00qeXEHC5wcU_Dc5e1cf3ffcBuQFEE&count=99&page=3',
            'https://api.weibo.com/2/statuses/friends_timeline.json?access_token=2.00qeXEHC5wcU_Dc5e1cf3ffcBuQFEE&count=99&page=4',
            'https://api.weibo.com/2/statuses/friends_timeline.json?access_token=2.00qeXEHC5wcU_Dc5e1cf3ffcBuQFEE&count=99&page=5',
            #'https://api.weibo.com/2/statuses/public_timeline.json?access_token=2.00qeXEHC5wcU_Dc5e1cf3ffcBuQFEE&count=199',
            ]
    is_start = True

    def parse(self, response):
        items = []
        statuses = json.loads(response.body)['statuses']
        for s in statuses:
            u = s['user']
            items.append(self.user(u))
            items.append(self.status(s))
        return items

    def user(self, user):
        item = UserItem()
        #item['info'] = user.get('info','')
        item['userid'] = user.get('id','')
        item['platform'] = 'swb'
        item['description'] = user.get('description','')
        item['image'] = user.get('avatar_large','')
        item['name'] = user.get('name','')
        #item['image'] = user.get('profile_image_url','')
        item['province'] = user.get('province','') #数字需要转化
        item['city'] = user.get('city','') # 数字 需要转化
        item['location'] = user.get('location','')
        item['gender'] = user.get('gender','') # 字母需要转化
        item['url'] = user.get('url','')
        item['followers_count'] = user.get('followers_count',None)
        item['friends_count'] = user.get('friends_count',None)
        item['statuses_count'] = user.get('statuses_count',None)
        item['favourites_count'] = user.get('favourites_count',None)
        return item


    def status(self, status):
        item = StatusItem()
        item['statusid'] = status.get('id','')
        item['statusmid'] = status.get('mid','')
        item['statusuid'] = status['user']['id']
        item['statusuname'] = status['user']['name']
        item['platform'] = 'swb'
        item['content'] = status.get('text','')+status.get('retweeted_status',{}).get('text','')
        item['timestamp'] = status.get('created_at','')
        item['reposts_count'] = status.get('reposts_count')
        item['comments_count'] = status.get('comments_count')
        return item
