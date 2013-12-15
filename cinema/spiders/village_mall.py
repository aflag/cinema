from scrapy.spider import BaseSpider
from scrapy.http import Request
from lxml import etree
from scrapy.selector import Selector
from cinema.items import Movie
from cinema import constants


class VillageMallSpider(BaseSpider):
    
    name = "village-mall"
    start_urls = [
        "http://www.shoppingvillagemall.com.br/cinema"
    ]


    def _has_class(self, class_name):
        return 'contains(concat(" ", normalize-space(@class), " "), " %s ")' % class_name

    def _extract(self, sel, path):
        return ' '.join(sel.xpath(path).extract())

    def parse(self, response):
        sel = Selector(response)
        for item in sel.xpath('//*[@id="cinema"]/article[2]/div/div[%s]' % self._has_class('itemInfo')):
            movie = Movie()
            movie['title'] = self._extract(item, 'div/div/div[%s]/h3/text()' % self._has_class('rightInfo'))
            movie['url'] = response.url
            movie['desc'] = self._extract(item, 'div/div/div[%s]/div[%s]/p/text()' % (self._has_class('rightInfo'), self._has_class('text'))).replace('amp;', '')
            movie['image'] = self._extract(item, 'div/div/div[%s]/img/@src' % self._has_class('leftImage'))
            movie['theater'] = self.name
            movie['sessions'] = self._extract(item, 'div/div/div[%s]/div[%s]/div/p/text()' % (self._has_class('rightInfo'), self._has_class('salas')))
            movie['room_type'] = constants.ROOM_TYPE['vip']
            yield movie
