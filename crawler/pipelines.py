#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import requests
import re

from md5 import md5
from crawler.db import mongo
from datetime import datetime
#from crawler.settings import 

class RssPipeline(object):
    def process_item(self, item, spider):
        return item

class track_storage(object):
    def __init__(self):
        self.date = datetime.now().strftime("%Y-%m-%d")
    def process_item(self, item, spider):
        if 'UserItem' is item.__class__.__name__:
            self.process_user_item(item)

        elif 'StatusItem' is item.__class__.__name__:
            self.process_status_item(item)

        elif 'RssItem' is item.__class__.__name__:
            self.process_rss_item(item)

        return item

    def process_user_item(self, item):
        if mongo.getdb().user.find({"userid":item['userid']}).count() is 0:
            mongo.getdb().user.insert(dict(item))

    def process_status_item(self, item): 

        if mongo.getdb().status.find({"statusid":item['statusid']}).count() is 0:
            mongo.getdb().status.insert(dict(item))
            mongo.getdb().user.update({"userid":item['statusuid']}, {"$inc":{'statistic.'+self.date:1}})
            self.datacore(item)

    def process_rss_item(self, item):
        if mongo.getdb().rss.find({"md5":item['md5']}).count() is 0:
            if item['title'] is '' or item['content'] is '':
                pass
            else:
                re_l = re.compile("<!\[CDATA\[")
                item['title'] = re.sub(ur'<[^>]*>','',re.sub(ur'\]\]>','',re.sub(ur'<!\[CDATA\[','',item['title'])))
                item['content'] = re.sub(ur'<[^>]*>','',re.sub(ur'\]\]>','',re.sub(ur'<!\[CDATA\[','',item['content'])))
                if item.get('date') is None:
                    item['date'] = self.date
                mongo.getdb().rss.insert(dict(item))

    def datacore(self, item):
        #DATAAPI = {'app_key':476991604, 'app_secret':'315bd254d9d56da49e47261a278379cc'}
        data = {}
        data['__API__[charset]'] = 'utf-8'
        data['__API__[output]'] = 'json' 
        data['__API__[app_key]'] = 1446517087#476991604  
        data['__API__[app_secret]'] = '610f11361c3f3b7e83a69b8ff3f9ebfd'#'315bd254d9d56da49e47261a278379cc' 
        data['__API__[username]'] = 'admin' 
        data['__API__[password]'] = md5('admin'+md5('admin').hexdigest()).hexdigest()
        #  true    string      网站用户密码的加密字串，生成格式为：md5(用户名.md5(密码))
        data['mod'] = 'topic'
        data['code'] = 'add'
        data['content'] = item['statusuname'] + ' ' + item['content']

        APIURL = "http://localhost/yqweibo/api.php"
        r = requests.post(APIURL,params=data)
        #print r.url
        print r.json()['result']
