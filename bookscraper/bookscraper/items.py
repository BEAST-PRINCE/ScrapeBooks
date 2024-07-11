# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


# def serialize_price(value):
#     return f'${value}'



class BookscraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    title = scrapy.Field()
    product_type = scrapy.Field()
    price_excl_tax = scrapy.Field()
    # price_excl_tax = scrapy.Field(serializer = serialize_price)
    tax = scrapy.Field()
    availablity = scrapy.Field()
    no_of_reviews = scrapy.Field()
    stars = scrapy.Field()
    catagory = scrapy.Field()
    description = scrapy.Field()
    price = scrapy.Field()