from scrapy.spider import BaseSpider
from scrapy.http import Request
from lxml import etree
from scrapy.selector import Selector
from cinema.items import Movie
from cinema import constants


class BarraShoppingSpider(BaseSpider):
    
    name = "barra-shopping"
    start_urls = [
        "http://www.barrashopping.com.br/components/com_cinema/xml/cinema.php"
    ]

    def parse_index(self, response):
        root = etree.XML(response.body)
        for link in root.xpath('//RESULT/FILME/URL_LINK'):
            link = 'http://www.barrashopping.com.br/'+link.text
            yield Request(link, callback=self.parse)

    def _extract(self, sel, path):
        return ' '.join(sel.xpath(path).extract())

    def parse_item(self, response):
        sel = Selector(response)
        movie = Movie()
        room = int(self._extract(sel, '//*[@id="cinema-info"]/div[1]/p/text()').split()[1].strip())
        movie['theater'] = 'barra shopping'
        movie['room'] = str(room)
        if room in [8, 9]:
            movie['room_type'] = constants.ROOM_TYPE['vip']
        elif room == 4:
            movie['room_type'] = constants.ROOM_TYPE['imax']
        else:
            movie['room_type'] = constants.ROOM_TYPE['regular']
        movie['title'] = self._extract(sel, '//*[@id="cinema"]/div[2]/strong/text()')
        movie['sessions'] = self._extract(sel, '//*[@id="cinema-info"]/div[1]/div[1]/text()')
        return movie

    def parse(self, response):
        if response.url in BarraShoppingSpider.start_urls:
            return self.parse_index(response)
        else:
            return self.parse_item(response)
