# -*- coding: utf-8 -*-
import scrapy

from jd_spider.items import JdSpiderItem


class JdSpider(scrapy.Spider):
    name = 'jd'
    allowed_domains = ['jd.com']
    start_urls = ['https://search.jd.com/Search?keyword=笔记本电脑']
    def __init__(self):
        self.page = 1
    def parse(self, response):
        # 下一页url
        self.page += 2
        next_page_url = "https://search.jd.com/Search?keyword=笔记本电脑&page=" + str(self.page) + "&s=" + str((self.page - 1) * 30 + 1) + "&click=1"
        item_selector_list = response.xpath('//li[@class="gl-item"]')
        print("next_page_url" + next_page_url)
        # 一页的商品id列表
        item_id_list = item_selector_list.xpath("@data-sku").extract()
        for i in range(len(item_selector_list)):
            item = JdSpiderItem()
            # 商品id
            goods_id = item_id_list[i]
            # 商品标题
            goods_title = "".join(response.xpath('//li[@data-sku="' + goods_id + '"]//a/em/text()').extract()).strip()
            # 商品价格
            goods_price = response.xpath('//li[@data-sku="' + goods_id + '"]//strong/i/text()').extract_first()
            # 商品链接
            goods_url = "https://item.jd.com/" + goods_id + ".html"
            # 店家名字
            shop_name = response.xpath('//li[@data-sku="' + goods_id + '"]//div[@class="p-shop"]//a/@title').extract_first()
            # 店家id
            shop_id = response.xpath('//li[@data-sku="' + goods_id + '"]//div[@class="p-shop"]//a/@href').extract_first().split("index-")[1].split(".html")[0]

            item["goods_id"] = goods_id
            item["goods_title"] = goods_title
            item["goods_price"] = goods_price
            item["goods_url"] = goods_url
            item["shop_name"] = shop_name
            item["shop_id"] = shop_id
            yield item

        yield scrapy.Request(
            url=next_page_url,
            callback=self.parse
        )