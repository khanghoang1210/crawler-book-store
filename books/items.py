# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
class BooksItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    poster_link = scrapy.Field()
    book_name = scrapy.Field()
    book_price = scrapy.Field()
    status = scrapy.Field()
    rating = scrapy.Field()
