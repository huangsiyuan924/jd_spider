# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JdSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    goods_id = scrapy.Field()
    goods_title = scrapy.Field()
    goods_price = scrapy.Field()
    goods_url = scrapy.Field()
    shop_name = scrapy.Field()
    shop_id = scrapy.Field()
