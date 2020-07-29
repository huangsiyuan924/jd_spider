# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from jd_spider.mysqlUtil import MysqlHelper


class JdSpiderPipeline(object):
    def __init__(self):
        self.helper = MysqlHelper("jd_spider_laptop")

    def process_item(self, item, spider):
        goods_id = item["goods_id"]
        goods_title = item["goods_title"]
        goods_price = item["goods_price"]
        goods_url = item["goods_url"]
        shop_name = item["shop_name"]
        shop_id = item["shop_id"]
        self.helper.insert_jd(goods_id, goods_title, goods_price, goods_url, shop_name, shop_id)
        return item
