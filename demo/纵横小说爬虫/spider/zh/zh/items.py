# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    book_name = scrapy.Field()
    book_url = scrapy.Field()
    author = scrapy.Field()
    catalog_url = scrapy.Field()
    nums = scrapy.Field()
    chapter_name = scrapy.Field()
    content_url = scrapy.Field()
    content = scrapy.Field()
    order_num = scrapy.Field()
