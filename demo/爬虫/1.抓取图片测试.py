import requests
import re


# https://ssr1.scrape.center/
def get_img(url, name):
    # url = "https://p1.meituan.net/movie/6bea9af4524dfbd0b668eaa7e187c3df767253.jpg@464w_644h_1e_1c"
    headers = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
    }
    res = requests.get(url, headers=headers)
    img_name = f'{name}.jpg'
    with open(img_name, 'wb') as f:
        f.write(res.content)


# with open('ssr.html', 'r', encoding='utf-8') as f:
#     text = f.read()
# # 正则匹配图片路径
# list2 = re.findall('src="(https.*?)"', text)

def get_urls():
    headers = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
    }
    res = requests.get('https://ssr1.scrape.center/', headers)
    text = res.text
    urls = re.findall('src="(https.*?)"', text)
    names = re.findall('"m-b-sm">(.*?)</h2>', text)
    print(names)
    print(urls)
    return urls


urls = get_urls()

for index, url in enumerate(urls):
    get_img(url, index)
