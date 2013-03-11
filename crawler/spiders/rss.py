import re
import md5
from scrapy.contrib.spiders import XMLFeedSpider
from crawler.items import *
from crawler.rss import feeds

class Rss(XMLFeedSpider):
    name = 'rss'
    start_urls = feeds
    #start_urls = ['http://rss.sina.com.cn/blog/astro/xz.xml']
    iterator = 'iternodes' 
    itertag = 'item' 

    def parse_node(self, response, selector):
        item = RssItem()
        try:
            item['url'] = selector.select('link/text()').extract()[0]
            item['md5'] = md5.md5(item['url']).hexdigest()
            item['title'] = "".join(selector.select('title/text()').extract()[0].split())
            item['content'] = "".join(re.sub(ur"\.\.\.\..*$",'',selector.select('description/text()').extract()[0].strip()).split())
            item['refer'] = response.url
            item['date'] = selector.select('pubDate/text()').extract()[0]
        except Exception as e:
            print e
        return item
