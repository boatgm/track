#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from scrapy.item import Item, Field

class SearchItem(Item):
    url = Field()
    title = Field()
    content = Field()
    date = Field()
    def __str__(self):
        return ("SearchItem:%s"%(self['title']))

class RssItem(Item):
    md5 = Field()
    url = Field()
    title = Field()
    content = Field()
    date = Field()
    refer = Field()
    def __str__(self):
        return ("RssItem:%s"%(self['title']))

class NewsItem(Item):
    md5 = Field()
    url = Field()
    title = Field()
    date = Field()
    content = Field()
    tags = Field()
    images = Field()
    def __str__(self):
        return ("NewsItem:%s"%(self['title']))

class BlogItem(Item):
    md5 = Field()
    url = Field()
    title = Field()
    date = Field()
    content = Field()
    tags = Field()
    images = Field()
    def __str__(self):
        return ("BlogItem:%s"%(self['title']))
 
class UserItem(Item):
    #info = Field()
    userid = Field()
    platform = Field()
    name = Field()
    description = Field()
    image = Field()#"profile_image_url": "http://tp1.sinaimg.cn/1404376560/50/0/1",
    #"avatar_large": "http://tp1.sinaimg.cn/1404376560/180/0/1",
    province = Field() # "11",
    city = Field() # "5",
    location = Field() # "北京 朝阳区",
    gender = Field() # "m",
    url = Field() #"url": "http://blog.sina.com.cn/zaku",
    followers_count = Field()
    friends_count = Field()
    statuses_count = Field()
    favourites_count = Field()
    verified_reason = Field()

    def __str__(self):
        return ("UserItem:%s"%(self['userid']))

class PhoneItem(Item):
    userid = Field()
    platform = Field()
    name = Field()
    description = Field()
    image = Field()

    def __str__(self):
        return ("PhoneItem:%s"%(self['userid']))

class StatusItem(Item):
    statusid = Field()
    statusmid = Field()
    statusuid = Field()
    statusuname = Field()
    platform = Field()
    content  = Field()
    timestamp= Field()
    reposts_count = Field()
    comments_count = Field()

    def __str__(self):
        return ("StatusItem:%s"%(self['content']))
