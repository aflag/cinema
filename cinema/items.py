# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class Movie(Item):
    title = Field()
    url = Field()
    desc = Field()
    dirctor = Field()
    image = Field()
    theater = Field()
    room = Field()
    room_type = Field()
    sessions = Field()
