import re
from scrapy.contrib.spiders import XMLFeedSpider
from crawler.items import *
from crawler.rss import feeds

class Rss(XMLFeedSpider):
    name = 'rss'
    #start_urls = feeds
    start_urls = ['http://rss.sina.com.cn/blog/astro/xz.xml']
    iterator = 'iternodes' 
    itertag = 'item' 

    def parse_node(self, response, selector):
        item = RssItem()
        #item['url'] = re.sub(ur'^<[^>]*>','',selector.select('link').extract()[0]) 
        item['url'] = selector.select('link/text()').extract()[0]
        print "#########",item['url']
        item['title'] = "".join(selector.select('title/text()').extract()[0].split())
        print "#########",item ['title']
        item['content'] = "".join(selector.select('description/text()').extract()[0].split())
        print "#########",item ['content']
        item['refer'] = response.url
        item['date'] = selector.select('pubDate/text()').extract()[0]
        #pubDate
        return item
