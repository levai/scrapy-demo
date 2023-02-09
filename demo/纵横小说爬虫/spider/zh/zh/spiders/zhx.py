import scrapy
from lxml import etree
from zh.items import ZhItem
import copy


class ZhxSpider(scrapy.Spider):
    name = 'zhx'

    # allowed_domains = ['xxx.com']
    # start_urls = ['http://xxx.com/']

    def parse(self, response):
        pass

    def start_requests(self):
        # 重写请求
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7,fi;q=0.6',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            # 'Cookie': 'ZHID=3A1B35FEF6D405DF91FF11CD97F4E2EF; zhffr=0; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221851359edac2f7-0fb5067efd4663-19525635-1296000-1851359edad9da%22%2C%22%24device_id%22%3A%221851359edac2f7-0fb5067efd4663-19525635-1296000-1851359edad9da%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; ver=2018; zh_visitTime=1674892661700; Hm_lvt_c202865d524849216eea846069349eb9=1674892662; Hm_lpvt_c202865d524849216eea846069349eb9=1674892797',
            'Pragma': 'no-cache',
            'Referer': 'https://www.zongheng.com/',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
        }
        url = "https://book.zongheng.com/store/c0/c0/b0/u0/p1/v0/s1/t0/u0/i1/ALL.html"
        yield scrapy.Request(url, headers=headers, callback=self.parse_one)

    def parse_one(self, response):
        html = etree.HTML(response.text)
        book_info_tags = html.xpath('//div[@class="bookinfo"]')
        # print(book_info_tags)
        for tag in book_info_tags[:1]:
            book_name = tag.xpath('./div[1]/a/text()')[0]
            book_url = tag.xpath('./div[1]/a/@href')[0]
            author = tag.xpath('./div[2]/a[1]/text()')[0]
            # print(book_name, book_url, author)
            headers = {
                'authority': 'book.zongheng.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7,fi;q=0.6',
                'cache-control': 'no-cache',
                # 'cookie': 'ZHID=3A1B35FEF6D405DF91FF11CD97F4E2EF; zhffr=0; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221851359edac2f7-0fb5067efd4663-19525635-1296000-1851359edad9da%22%2C%22%24device_id%22%3A%221851359edac2f7-0fb5067efd4663-19525635-1296000-1851359edad9da%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; JSESSIONID=abc04hVMajNXtcyxHwtuy; rSet=1_2_1_14_1; ver=2018; zh_visitTime=1674892661700; Hm_lvt_c202865d524849216eea846069349eb9=1674892662; PassportCaptchaId=84a2a54356c10ca6f1109f628f17b9e6; Hm_lpvt_c202865d524849216eea846069349eb9=1674909301',
                'pragma': 'no-cache',
                'referer': 'https://book.zongheng.com/store/c0/c0/b0/u0/p1/v9/s1/t0/u0/i1/ALL.html',
                'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"macOS"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
            }
            # book_info  通过meta传递下一级
            book_info = {
                'book_name': book_name,
                'book_url': book_url,
                'author': author
            }
            yield scrapy.Request(url=book_url, headers=headers, callback=self.parse_two,
                                 meta={"book_info": copy.deepcopy(book_info)})

    def parse_two(self, response):
        html = etree.HTML(response.text)
        book_info = response.meta['book_info']
        # print('一级数据', book_info)
        catalog_url = html.xpath('//a[@class="all-catalog"]/@href')[0]
        nums = html.xpath('//div[@class="nums"]/span[1]/i/text()')[0]
        headers = {
            'authority': 'book.zongheng.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7,fi;q=0.6',
            'cache-control': 'no-cache',
            # 'cookie': 'ZHID=3A1B35FEF6D405DF91FF11CD97F4E2EF; zhffr=0; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221851359edac2f7-0fb5067efd4663-19525635-1296000-1851359edad9da%22%2C%22%24device_id%22%3A%221851359edac2f7-0fb5067efd4663-19525635-1296000-1851359edad9da%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; JSESSIONID=abc04hVMajNXtcyxHwtuy; rSet=1_2_1_14_1; ver=2018; zh_visitTime=1674892661700; Hm_lvt_c202865d524849216eea846069349eb9=1674892662; PassportCaptchaId=84a2a54356c10ca6f1109f628f17b9e6; Hm_lpvt_c202865d524849216eea846069349eb9=1674909301',
            'pragma': 'no-cache',
            'referer': 'https://book.zongheng.com/store/c0/c0/b0/u0/p1/v9/s1/t0/u0/i1/ALL.html',
            'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        }
        # 追加数据
        book_info['catalog_url'] = catalog_url
        book_info['nums'] = nums.strip()
        yield scrapy.Request(url=catalog_url, headers=headers, callback=self.parse_three,
                             meta={"book_info": copy.deepcopy(book_info)})

    def parse_three(self, response):
        book_info = response.meta['book_info']
        # print('二级数据', book_info)
        html = etree.HTML(response.text)
        a_tags = html.xpath('//ul[@class="chapter-list clearfix"]/li/a')

        for index,a in enumerate(a_tags):
            chapter_name = a.xpath('./text()')[0]
            content_url = a.xpath('./@href')[0]
            headers = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7,fi;q=0.6',
                'Cache-Control': 'no-cache',
                'Connection': 'keep-alive',
                # 'Cookie': 'ZHID=3A1B35FEF6D405DF91FF11CD97F4E2EF; zhffr=0; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221851359edac2f7-0fb5067efd4663-19525635-1296000-1851359edad9da%22%2C%22%24device_id%22%3A%221851359edac2f7-0fb5067efd4663-19525635-1296000-1851359edad9da%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; ver=2018; zh_visitTime=1674892661700; Hm_lvt_c202865d524849216eea846069349eb9=1674892662; Hm_lpvt_c202865d524849216eea846069349eb9=1674892797',
                'Pragma': 'no-cache',
                'Referer': 'https://www.zongheng.com/',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-User': '?1',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
                'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"macOS"',
            }
            book_info['chapter_name'] = chapter_name
            book_info['content_url'] = content_url
            book_info['order_num'] = index+1
            # print('3级数据', chapter_name, content_url)
            yield scrapy.Request(url=content_url, headers=headers, callback=self.parse_four,
                                 meta={"book_info": copy.deepcopy(book_info)},priority=50)  # 注意拷贝问题

    def parse_four(self, response):
        book_info = response.meta['book_info']
        # print('三级数据', book_info)
        html = etree.HTML(response.text)
        content_list = html.xpath('//div[@class="content"]/p/text()')
        content = ''.join([content.strip() for content in content_list])
        book_info['content'] = content
        item = ZhItem()
        item.update(book_info)
        yield item
