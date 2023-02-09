"""
定位标签
获取文本
"""
from lxml import etree

with open('ssr.html', 'r', encoding='utf-8') as f:
    text = f.read()

html = etree.HTML(text)  # 将text 变成xpath对象

tags = html.xpath("/html/body")
print(tags)
print(tags[0].text)

text = tags[0].xpath('./text()')
print(text)
