# coding=utf-8
# XPath的使用：
#     节点选取
'''

nodename   选取此节点的所有子节点
/          从当前节点选取直接子节点
//         从当前节点选取子孙节点
.          选取当前节点
..         选取当前节点的父节点
@          选取属性

//title[@lang='eng'] : 选择所有名称为title，同时属性lang的值为eng的节点

'''

import requests
from lxml import etree

URL = "https://maoyan.com/board/4?offset=0"

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 '
                    '(KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}

def get_page(url):
    try:
        response = requests.get(url,headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except Exception as e:
        return None

# html = get_page(URL)

text = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
'''
# 构造了一个XPath解析对象:
html = etree.HTML(text)
# print(type(html)) <class 'lxml.etree._Element'>

# 可以直接读取文本文件进行解析:
# html = etree.parse('./test.html', etree.HTMLParser())

# 使用XPath:
result = html.xpath('//*') # 所有节点
# print(result)

# 所有li节点:
result = html.xpath('//li')
# print(result)

# 选择li节点的所有直接a子节点
result = html.xpath('//li/a')
# print(result)

# 首先选中href属性为link4.html的a节点，然后再获取其父节点，然后再获取其class属性
result = html.xpath('//a[@href="link4.html"]/../@class')
# print(result)

# 可以通过parent::来获取父节点
result = html.xpath('//a[@href="link4.html"]/parent::*/@class')

# XPath中的text()方法获取节点中的文本