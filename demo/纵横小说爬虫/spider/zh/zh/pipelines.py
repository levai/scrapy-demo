# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql
from zh.settings import mysql_local
from zh.items import ZhItem


class ZhPipeline:
    def open_spider(self, spider):
        # 爬虫开始的时候，就启动
        print('----爬虫启动----')
        # 连接mysql 数据库相关操作
        self.conn = pymysql.connect(**mysql_local)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        try:
            if isinstance(item, ZhItem):  # 属于ZhItem 实例，则进行存储数据
                print('管道数据', dict(item))
                sql = "INSERT INTO zongheng_info(book_name,author,book_url,nums,catalog_url,chapter_name,content_url,content,order_num) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                author = item['author']
                book_name = item['book_name']
                book_url = item['book_url']
                nums = item['nums']
                catalog_url = item['catalog_url']
                chapter_name = item['chapter_name']
                content_url = item['content_url']
                content = item['content']
                order_num = item['order_num']
                data = (book_name, author, book_url, nums, catalog_url, chapter_name, content_url, content, order_num)
                self.cursor.execute(sql, data)
                self.conn.commit()
                return item
        except Exception as e:
            print('数据存储错误', e)

    def close_spider(self, spider):
        print('----爬虫结束----')
        self.cursor.close()
        self.conn.close()
