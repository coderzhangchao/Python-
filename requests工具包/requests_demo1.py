# coding=utf-8
# requests的基本用法:

import requests

def demo1():
    # r = requests.get('https://www.baidu.com/')
    # print(type(r)) <class 'requests.models.Response'>
    # print(r.status_code) 200
    # print(type(r.text))  <class 'str'>
    # print(r.text)
    # print(r.cookies) <RequestsCookieJar[<Cookie BDORZ=27315 for .baidu.com/>]>

    '''
    r = requests.post('http://httpbin.org/post')
    r = requests.put('http://httpbin.org/put')
    r = requests.delete('http://httpbin.org/delete')
    r = requests.head('http://httpbin.org/get')
    r = requests.options('http://httpbin.org/get')
    '''

    # r = requests.get('http://httpbin.org/get')
    # print(r.text)
    '''
    {
        "args": {},
        "headers": {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate",
            "Host": "httpbin.org",
            "User-Agent": "python-requests/2.21.0"
        },
        "origin": "111.19.58.236, 111.19.58.236",
        "url": "https://httpbin.org/get"
    }
    '''

    # 带参请求：
    # r = requests.get('http://httpbin.org/get?name=germey&age=22')
    data = {
        'name': 'germey',
        'age': 22
    }
    # r = requests.get("http://httpbin.org/get", params=data)
    # print(r.text)
    '''
    "args": {
        "age": "22",
        "name": "germey"
    },
    '''

    # r = requests.get("http://httpbin.org/get")
    # print(type(r.text))
    # print(r.json())
    # print(type(r.json())) <class 'dict'>

    import re
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
    }
    r = requests.get("https://www.zhihu.com/explore", headers=headers)
    pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>', re.S)
    titles = re.findall(pattern, r.text)
    print(titles)

# demo1()

# 抓取二进制数据
def demo2():
    # r = requests.get("https://github.com/favicon.ico")
    # 保存图片
    # with open('favicon.ico','wb') as f:
        # r.content --- 二进制类型的数据
        # f.write(r.content)

    # 添加头信息
    # r = requests.get("https://www.zhihu.com/explore")
    # print(r.text)
    # <head><title>400BadRequest</title></head>

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
    }
    # r = requests.get("https://www.zhihu.com/explore",headers=headers) # 可正常访问
    # print(r.text)

    # post 请求
    data = {'name': 'germey', 'age': '22'}
    r = requests.post("http://httpbin.org/post", data=data)
    print(r.text)
    '''
    "form": {
        "age": "22",
        "name": "germey"
    },
    '''
    r = requests.get('http://www.jianshu.com')
    exit() if not r.status_code == requests.codes.ok else print('Request Successfully')

    '''
    状态码：
        1**   -- 信息性状态码
        2**   -- 成功状态码
        3**   -- 重定向状态码
        4**   -- 客户端错误状态码
        5**   -- 服务端错误状态码
    '''
demo2()