import pymongo
from crawler.settings import MONGODB
class mongo(object):
    db = None

    @classmethod
    def getdb(self):
        if self.db is None:
            self.db = pymongo.Connection(MONGODB['host'],MONGODB['port'])[MONGODB['name']]
        return self.db

