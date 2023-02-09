import scrapy
from lxml import etree
from info1.items import Info1Item


class FilmSpider(scrapy.Spider):  # 继承爬虫基础类
    name = 'film'  # 唯一性 爬虫文件名
    allowed_domains = ['ssr1.scrape.center']  # 允许爬的域名，可以注释掉，标识允许所有域名
    # start_urls = ['http://ssr1.scrape.center/page/2']  # 初始请求URL 必须要有
    start_urls = [f"https://ssr1.scrape.center/page/{num}" for num in range(1, 11)]

    def parse(self, response):
        print(response.status)

        film_names = response.xpath('//h2[@class="m-b-sm"]/text()').getall()
        # print("Selector", film_names)

        text_list = response.xpath('//p[@class="score m-t-md m-b-n-sm"]/text()').getall()

        scores = [i.strip() for i in text_list]
        # print(scores)

        item = Info1Item()
        item["data_list"] = list(zip(film_names, scores))

        yield item
# 构造URL
# 数据覆盖问题
