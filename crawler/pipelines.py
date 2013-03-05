import requests
from crawler.db import mongo

class RssPipeline(object):
    def process_item(self, item, spider):
        return item
class track_storage(object):

    def process_item(self, item, spider):
        if 'UserItem' is item.__class__.__name__:

            pass
        elif 'StatusItem' is item.__class__.__name__:

            pass
        elif 'RssItem' is item.__class__.__name__:
            #mongo.getdb().rss.insert(dict(item))
            #print dict(item)
            pass

        return item
    def process_user_item(self, item):
        pass

    def process_status_item(self, item):
        pass

    def datacore(self, item):
        pass



