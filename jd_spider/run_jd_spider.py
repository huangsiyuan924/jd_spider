'''
-*- coding: utf-8 -*-
@Author  : Haxp
@Time    : 29/07/2020 6:50 PM
@Software: PyCharm
@File    : run_jd_spider.py
@Email   : huangsiyuan924@gmail.com
'''

from scrapy.cmdline import execute

execute("scrapy crawl jd".split())