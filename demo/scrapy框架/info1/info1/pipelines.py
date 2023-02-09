# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql
from info1.settings import mysql_local
import pandas as pd


# 存储到mysql
class Info1Pipeline:
    def open_spider(self, spider):
        # 爬虫开始的时候，就启动
        print('----爬虫启动----')
        # 连接mysql 数据库相关操作
        self.conn = pymysql.connect(**mysql_local)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        data_list = item['data_list']
        sql = "INSERT INTO film_info(name,score) VALUES(%s,%s)"
        self.cursor.executemany(sql, data_list)
        self.conn.commit()
        return item

    def close_spider(self, spider):
        print('----爬虫结束----')
        self.cursor.close()
        self.conn.close()


# 存储到excel
class Info1ExcelPipeline:
    def open_spider(self, spider):
        # 爬虫开始的时候，就启动
        self.data_list = []
        pass

    def process_item(self, item, spider):
        tempt_list = item['data_list']
        self.data_list.extend(tempt_list)
        return item

    def close_spider(self, spider):
        df = pd.DataFrame(data=self.data_list, columns=["电影名称", "评分"])
        df.to_excel('电影信息.xlsx', index=False)
        pass
