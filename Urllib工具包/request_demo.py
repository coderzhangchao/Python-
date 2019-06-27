# coding=utf-8
'''
    URI 的全称为 Uniform Resource Identifier ，即统一资源标志符
    URL 的全称为 Universa l Resource Locator ，即统一资源定位符
    URL 是 URI 的子集
'''
from urllib import request

# 1、request 的使用
def request_demo1():
    # response = request.urlopen('https://www.python.org')
    # print(response.read().decode('utf-8'))

    response = request.urlopen('https://www.python.org')
    print(type(response))
    # <class 'http.client.HTTPResponse'>

    '''
    可以发现，它是一个HTTPResposne类型的对象。
    它主要包含read()、readinto()、getheader(name)、getheaders()、fileno()等方法，
    以及msg、version、status、reason、debuglevel、closed等属性。
    '''
    print(response.status)
    print(response.getheaders())
    print(response.getheader('Server'))

# request_demo1()

from urllib import parse
import urllib.error
import socket

# 2、带参数的请求
def request_demo2():
    # data参数：
    data = bytes(parse.urlencode({'word': '你好'}), encoding='utf8')
    response = request.urlopen('http://httpbin.org/post', data=data)
    print(response.read())

    # timeout参数:
    response = request.urlopen('http://httpbin.org/get', timeout=1)
    print(response.read())

    try:
        response = request.urlopen('http://httpbin.org/get', timeout=0.1)
    except urllib.error.URLError as e:
        if isinstance(e.reason, socket.timeout):
            print('TIME OUT')

# request_demo2()

# Request 的用法
# def __init__(self, url, data=None, headers={},
    #              origin_req_host=None, unverifiable=False,
    #              method=None)
def request_demo3():
    # request = request.Request('https://python.org')
    # response = request.urlopen(request)
    # print(response.read().decode('utf-8'))

    url = 'http://httpbin.org/post'
    headers = {
        'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
        'Host': 'httpbin.org'
    }
    dict = {
        'name': 'Germey'
    }
    data = bytes(parse.urlencode(dict), encoding='utf8')
    req = request.Request(url=url, data=data, headers=headers, method='POST')
    response = request.urlopen(req)
    print(response.read().decode('utf-8'))

# request_demo3()

from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, build_opener
from urllib.error import URLError
#高级用法
def request_demo4():
    # 1、请求验证
    username = 'username'
    password = 'password'
    url = 'http://localhost:5000/'

    p = HTTPPasswordMgrWithDefaultRealm()
    p.add_password(None, url, username, password)
    auth_handler = HTTPBasicAuthHandler(p)
    opener = build_opener(auth_handler)

    try:
        result = opener.open(url)
        html = result.read().decode('utf-8')
        print(html)
    except URLError as e:
        print(e.reason)

    # 2、代理：
    from urllib.request import ProxyHandler
    proxy_handler = ProxyHandler({
        'http': 'http://127.0.0.1:9743',
        'https': 'https://127.0.0.1:9743'
    })
    opener = build_opener(proxy_handler)
    try:
        response = opener.open('https://www.baidu.com')
        print(response.read().decode('utf-8'))
    except URLError as e:
        print(e.reason)

    # 3、cookie
    import http.cookiejar

    cookie = http.cookiejar.CookieJar()
    handler = request.HTTPCookieProcessor(cookie)
    opener = build_opener(handler)
    response = opener.open('http://www.baidu.com')
    for item in cookie:
        print(item.name + "=" + item.value)

request_demo4()
