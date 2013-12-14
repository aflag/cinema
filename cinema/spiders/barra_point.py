from scrapy.spider import BaseSpider
from scrapy.http import Request
from lxml import etree
from scrapy.selector import Selector
from cinema.items import Movie
from cinema import constants


class BarraPointSpider(BaseSpider):
    
    name = "barra-point"
    start_urls = [
        "http://www.grupoestacao.com.br/grupoestacao/salas/barra.php"
    ]

    def parse(self, response):
        sel = Selector(response)
        movie = Movie()
        movie['theater'] = self.name
        movie['room_type'] = constants.ROOM_TYPE['alt']
        movie['url'] = response.url
        movie['desc'] = ' '.join(sel.xpath('/html/body/table/tr/td[2]/table/tr[2]/td/table/tr/td/table/tr[3]/td[1]/div/p').extract())
        return movie
