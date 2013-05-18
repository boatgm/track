from scrapy.xlib.pydispatch import dispatcher
from scrapy import signals
from scrapy import log
#from tracker import stats
from scrapy.stats import stats
import datetime
import os
from tracker.db import mongo

class StatsToMongo(object):
    def __init__(self):
        dispatcher.connect(self.stats_spider_closed, signal=signals.stats_spider_closed)
        #dispatcher.connect(self.check_new_task, signal=signals.engine_stopped)

    def stats_spider_closed(self, spider, spider_stats):
        statsinfo = {}
        statsinfo['name'] = spider.name
        #statsinfo['created_at'] = unicode(datetime.datetime.now().replace(microsecond=0))
        #statsinfo['updated_at'] = unicode(datetime.datetime.now().replace(microsecond=0))
        statsinfo['start_time'] = unicode(spider_stats['start_time'].replace(microsecond=0))
        statsinfo['finish_time'] = unicode(spider_stats['finish_time'].replace(microsecond=0))
        #statsinfo['finish_reason'] = spider_stats['finish_reason'].encode('utf-8')
        statsinfo['time_scraped_count'] = spider_stats['item_scraped_count'] if 'item_scraped_count' in spider_stats  else 0
        statsinfo['images_count']= spider_stats['images_count'] if 'images_count' in spider_stats  else 0 
        statsinfo['images_uptodate'] = spider_stats['images_uptodate'] if 'images_uptodate' in spider_stats  else 0
        statsinfo['images_downloaded'] = spider_stats['images_downloaded'] if 'images_downloaded' in spider_stats  else 0
        statsinfo['request_count'] = spider_stats['downloader/request_count'] if 'request_count' in spider_stats  else 0
        statsinfo['response_count'] = spider_stats['downloader/response_count'] if 'downloader/response_count' in spider_stats  else 0
        statsinfo['response_status_count_200'] = spider_stats['downloader/response_status_count/200'] if 'downloader/response_status_count/200' in spider_stats else 0
        statsinfo['response_status_count_301'] = spider_stats['downloader/response_status_count/301'] if 'downloader/response_status_count/301' in spider_stats else 0
        statsinfo['response_status_count_302'] = spider_stats['downloader/response_status_count/302'] if 'downloader/response_status_count/302' in spider_stats else 0
        statsinfo['response_status_count_500'] = spider_stats['downloader/response_status_count/500'] if 'downloader/response_status_count/500' in spider_stats else 0
        mongo.getdb().statsinfo.insert(statsinfo)

