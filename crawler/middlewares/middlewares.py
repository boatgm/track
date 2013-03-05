# You can use this middleware to have a random user agent every request the spider makes.
# You can define a user USER_AGENT_LIST in your settings and the spider will chose a random user agent from that list every time.
# 
# You will have to disable the default user agent middleware and add this to your settings file.
# 
#     DOWNLOADER_MIDDLEWARES = {
#         'scraper.random_user_agent.RandomUserAgentMiddleware': 400,
#         'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None,
#     }



from scrapy import log
import base64
import random
from crawler.settings import PROXIES,USER_AGENT_LIST
 
class UMDownloadMiddleware(object):
    def process_request(self, request, spider):
        ua  = random.choice(USER_AGENT_LIST)
        if ua:
            request.headers.setdefault('User-Agent', ua)
        proxy = random.choice(PROXIES)
        #if proxy['user_pass'] is not None:
        #    request.meta['proxy'] = "http://%s" % proxy['ip_port']
        #    encoded_user_pass = base64.encodestring(proxy['user_pass'])
        #    request.headers['Proxy-Authorization'] = 'Basic ' + encoded_user_pass            
        #else:
        #    request.meta['proxy'] = "http://%s" % proxy['ip_port']
        return request
    def process_response(self, request, response, spider):
        response
        return response

class ProxyMiddleware(object):
    def process_request(self, request, spider):
        ua  = random.choice(USER_AGENT_LIST)
        if ua:
            request.headers.setdefault('User-Agent', ua)
        proxy = random.choice(PROXIES)
        if proxy['user_pass'] is not None:
            request.meta['proxy'] = "http://%s" % proxy['ip_port']
            encoded_user_pass = base64.encodestring(proxy['user_pass'])
            request.headers['Proxy-Authorization'] = 'Basic ' + encoded_user_pass            
        else:
            request.meta['proxy'] = "http://%s" % proxy['ip_port']


# A downloader middleware automatically to redirect pages containing a rel=canonical in their contents to the canonical url
# (if the page itself is not the canonical one),
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.utils.url import url_is_from_spider
from scrapy.http import HtmlResponse
from scrapy import log
class RelCanonicalMiddleware(object):
    #process redirect
    _extractor = SgmlLinkExtractor(restrict_xpaths=['//head/link[@rel="canonical"]'], tags=['link'], attrs=['href'])
 
    def process_response(self, request, response, spider):
        if isinstance(response, HtmlResponse) and response.body and getattr(spider, 'follow_canonical_links', False):
            rel_canonical = self._extractor.extract_links(response)
            if rel_canonical:
                rel_canonical = rel_canonical[0].url
                if rel_canonical != request.url and url_is_from_spider(rel_canonical, spider):
                    log.msg("Redirecting (rel=\"canonical\") to %s from %s" % (rel_canonical, request), level=log.DEBUG, spider=spider)
                    return request.replace(url=rel_canonical, callback=lambda r: r if r.status == 200 else response)
        return response


# This middleware can be used to avoid re-visiting already visited items, which can be useful for speeding up the scraping for projects with immutable items, ie. items that, once scraped, don't change.
 
from scrapy import log
from scrapy.http import Request
from scrapy.item import BaseItem
from scrapy.utils.request import request_fingerprint
 
from crawler.items import LinkItem as MyItem
 
class IgnoreVisitedItems(object):
    """Middleware to ignore re-visiting item pages if they were already visited
    before. The requests to be filtered by have a meta['filter_visited'] flag
    enabled and optionally define an id to use for identifying them, which
    defaults the request fingerprint, although you'd want to use the item id,
    if you already have it beforehand to make it more robust.
    """
 
    FILTER_VISITED = 'filter_visited'
    VISITED_ID = 'visited_id'
    CONTEXT_KEY = 'visited_ids'
 
    def process_spider_output(self, response, result, spider):
        context = getattr(spider, 'context', {})
        visited_ids = context.setdefault(self.CONTEXT_KEY, {})
        ret = []
        for x in result:
            visited = False
            if isinstance(x, Request):
                if self.FILTER_VISITED in x.meta:
                    visit_id = self._visited_id(x)
                    if visit_id in visited_ids:
                        log.msg("Ignoring already visited: %s" % x.url,
                                level=log.INFO, spider=spider)
                        visited = True
            elif isinstance(x, BaseItem):
                visit_id = self._visited_id(response.request)
                if visit_id:
                    visited_ids[visit_id] = True
                    x['visit_id'] = visit_id
                    x['visit_status'] = 'new'
            if visited:
                ret.append(MyItem(visit_id=visit_id, visit_status='old'))
            else:
                ret.append(x)
        return ret
 
    def _visited_id(self, request):
        return request.meta.get(self.VISITED_ID) or request_fingerprint(request)
 
# Snippet imported from snippets.scrapy.org (which no longer works)
# author: pablo
# date  : Aug 10, 2010

