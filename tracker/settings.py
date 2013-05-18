#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import os
BOT_NAME = 'tracker'
PROJECT_PATH = os.path.realpath(os.path.dirname(__file__) + '/../../')
#微博APPKEY
#requests.get("http://172.31.159.7/yqweibo/api.php?mod=test&code=test&__API__[app_key]=476991604&__API__[app_secret]=315bd254d9d56da49e47261a278379cc&__API__[output]=json").text

DATACORE ={
        "WB"   :("WBCHANNEL",  "c29be50da6659d0706280f20a77aaba5"),
        "Blog" :("BLOGCHANNEL","6952f306b1416af041a2b49675a45c73"),
        "RSS"  :("RSSCHANNEL", "e61378bc1ddbcf92b19baca174f124c0"),
        "News" :("NEWSCHANNEL","3453674fae5d46d04d0f22eb1253a7f3"),
        }

DATAAPI = {'app_key':476991604, 'app_secret':'315bd254d9d56da49e47261a278379cc'}

SNWB = {'app_key':3036448412,'app_secret':'c6cfd0d95b66f91ab070fe212880f418'}    #微意见
QQWB = {''}
WECHAR = {}
RENREN = {}

FACEBOOK = {}
TWITTER  = {}
STOKEN = [
"2.00qeXEHC0mqijW049bacef460bbjJV",#人脉网络分析
"2.00qeXEHC55ZoOC033523ae3a0OUvkZ",#人脉分析器
"2.00qeXEHC5wcU_Dc5e1cf3ffcBuQFEE",#微意见
"2.00qeXEHC0f8IZX0c4c99e571tBfTXE",#火烧云
]

SPIDER_MODULES = ['tracker.spiders']
NEWSPIDER_MODULE = 'tracker.spiders'

USER_AGENT = ''
USER_AGENT_LIST = [
    "Googlebot/2.1 (+http://www.google.com/bot.html)",
    "Googlebot/2.2 (+http://www.google.com/bot.html)",
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.19 (KHTML, like Gecko) Ubuntu/11.10 Chromium/18.0.1025.168 Chrome/18.0.1025.168 Safari/535.19',
    'Mozilla/5.0 (iPad; U; CPU iPhone OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B314 Safari/531.21.10'
    ]

#DEFAULT_ITEM_CLASS = 'tracker.items.RssItem
ITEM_PIPELINES = ['tracker.pipelines.track_storage',]
EXTENSIONS = {
    'scrapy.contrib.corestats.CoreStats': 500,
    'tracker.statstodb.StatsToMongo': 1000,
    }

DOWNLOADER_MIDDLEWARES = {
#    'tracker.middlewares.UMDownloadMiddleware': 400,
#    'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None,
    }
REDIRECT_ENABLED = False
REDIRECT_MAX_TIMES =0 
MONGODB = {'host':'datacore.com','port':27017,'name':'track'}
MYSQLDB = {'host':'localhost','port':27017,'name':'track','user':'root','pwd':'root'}


MAIL_DEBUG = False
MAIL_HOST = 'mail.google.com'
MAIL_PORT = 25
MAIL_FROM = 'gongming@umeng.com'
MAIL_PASS = 'umeng123'
MAIL_USER = 'gongming@umeng.com'

COOKIES_ENABLED = True
DNSCACHE_ENABLED = True

DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'cn',
}

PROXIES = [{'ip_port': 'xx.xx.xx.xx:xxxx', 'user_pass': 'foo:bar'},
           {'ip_port': 'PROXY2_IP:PORT_NUMBER', 'user_pass': 'username:password'},
          {'ip_port': 'PROXY3_IP:PORT_NUMBER', 'user_pass': ''},]
