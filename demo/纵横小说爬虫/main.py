import requests
from lxml import etree
import pandas as pd


def one():
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

    response = requests.get('https://book.zongheng.com/showchapter/1218197.html', headers=headers)
    # print(response.text)
    html = etree.HTML(response.text)
    a_tags = html.xpath('//ul[@class="chapter-list clearfix"]/li/a')
    chapter_list = []
    for a in a_tags:
        chapter_name = a.xpath('./text()')
        chapter_url = a.xpath('./@href')
        chapter_list.extend(zip(chapter_name, chapter_url))

    # df = pd.DataFrame(data=chapter_tag_list, columns=["章节名称", "章节地址"])
    # df.to_excel('小说-人间最高处.xlsx', index=False)

    return chapter_list


my_chapter_list = one()

for item in my_chapter_list[0:2]:
    chapter_name = item[0]
    chapter_url = item[1]
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

    response = requests.get(chapter_url, headers=headers)
    # print(response.text)
    html = etree.HTML(response.text)

    content_list = html.xpath('//div[@itemprop="acticleBody"]/p/text()')

    content = ''.join([content.strip() for content in content_list])

    print(content)
