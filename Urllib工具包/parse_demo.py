# coding=utf-8
# 解析链接：
'''
1、urlparse() --- URL的识别和分段
'''
from urllib.parse import urlparse

# urlparse(url, scheme='', allow_fragments=True)
result = urlparse('http://www.baidu.com/index.html;user?id=5#comment')
print(type(result))
# <class 'urllib.parse.ParseResult'>

print(result)
# ParseResult(scheme='http', netloc='www.baidu.com', path='/index.html',
#             params='user', query='id=5', fragment='comment')

'''
2、urlunparse()
'''
from urllib.parse import urlunparse

data = ['http', 'www.baidu.com', 'index.html', 'user', 'a=6', 'comment']
print(urlunparse(data))
# http://www.baidu.com/index.html;user?a=6#comment

data = ['http', 'www.baidu.com', 'index.html', '', '', '']
print(urlunparse(data))
# http://www.baidu.com/index.html

# 注: data 的长度必须为6 否则抛异常

'''
3、urljoin() --- 
'''
from urllib.parse import urljoin

print(urljoin('http://www.baidu.com', 'FAQ.html'))
# http://www.baidu.com/FAQ.html

print(urljoin('http://www.baidu.com', 'https://cuiqingcai.com/FAQ.html'))
# https://cuiqingcai.com/FAQ.html

print(urljoin('http://www.baidu.com/about.html', 'https://cuiqingcai.com/FAQ.html'))
# https://cuiqingcai.com/FAQ.html

print(urljoin('http://www.baidu.com/about.html', 'https://cuiqingcai.com/FAQ.html?question=2'))
# https://cuiqingcai.com/FAQ.html?question=2

print(urljoin('http://www.baidu.com?wd=abc', 'https://cuiqingcai.com/index.php'))
# https://cuiqingcai.com/index.php

print(urljoin('http://www.baidu.com', '?category=2#comment'))
# http://www.baidu.com?category=2#comment

print(urljoin('www.baidu.com', '?category=2#comment'))
# www.baidu.com?category=2#comment

print(urljoin('www.baidu.com#comment', '?category=2'))
# www.baidu.com?category=2

'''
4、urlencode() -- 构造GET请求参数的时候非常有用
'''

from urllib.parse import urlencode

params = {
    'name': 'germey',
    'age': 22
}
base_url = 'http://www.baidu.com?'
# 参数序列化：
url = base_url + urlencode(params)
print(url)
# http://www.baidu.com?name=germey&age=22

# parse_qs() parse_qsl() 反序列化

'''
5、quote() -- 
    该方法可以将内容转化为URL编码的格式。
    URL中带有中文参数时，有时可能会导致乱码的问题，此时用这个方法可以将中文字符转化为URL编码
'''
from urllib.parse import quote

keyword = '壁纸'
url = 'https://www.baidu.com/s?wd=' + quote(keyword)
print(url)
# https://www.baidu.com/s?wd=%E5%A3%81%E7%BA%B8

# unquote()
from urllib.parse import unquote

url = 'https://www.baidu.com/s?wd=%E5%A3%81%E7%BA%B8'
print(unquote(url))
# https://www.baidu.com/s?wd=壁纸




