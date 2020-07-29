'''
-*- coding: utf-8 -*-
@Author  : Haxp
@Time    : 29/07/2020 7:59 PM
@Software: PyCharm
@File    : mysqlUtil.py
@Email   : huangsiyuan924@gmail.com
'''
import pymysql


class MysqlHelper():

    def __init__(self, table_name):
        # 连接MySQL
        self.db = pymysql.connect("localhost", "root", "asdasdasd", "test")
        # 创建cursor对象
        self.cursor = self.db.cursor()
        self.table_name = table_name
        self.cursor.execute('''
                        CREATE TABLE IF NOT EXISTS {}(
                        goods_id BIGINT PRIMARY KEY,
                        goods_title VARCHAR(150) NOT NULL,
                        goods_price FLOAT(10, 2) NOT NULL,
                        goods_url VARCHAR(100) NOT NULL,
                        shop_name VARCHAR(30) NOT NULL,
                        shop_id INT NOT NULL
                        )
        '''.format(self.table_name))

    def insert_jd(self, goods_id, goods_title, goods_price, goods_url, shop_name, shop_id):
        sql = "INSERT INTO "+ self.table_name +"(goods_id, goods_title, goods_price, goods_url, shop_name, shop_id) VALUES('%s', '%s', '%s', '%s', '%s', '%s')" % \
              (goods_id, goods_title, goods_price, goods_url, shop_name, shop_id)
        self.cursor.execute(sql)
        self.db.commit()
    def close(self):
        self.db.close()
