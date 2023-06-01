# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field
class BooksItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    poster_link = Field()
    book_name = Field()
    book_price = Field()
    status = Field()
    rating_star = Field()
