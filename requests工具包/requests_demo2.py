# coding=utf-8
# requests的高级用法:

import requests
'''
1、文件上传
    open（）打开一个文件，创建一个file对象，用于读写。
    
files = {'file': open('favicon.ico', 'rb')}
r = requests.post("http://httpbin.org/post", files=files)
print(r.text)
    # "files": {
    #     "file": "data:application/octet-stream;base64,A0F/AA......
    # },
'''

# 2、cookies:
'''
r = requests.get("https://www.baidu.com")
# 获取cookiea
print(r.cookies)
for key,value in r.cookies.items():
    print(key +"=" +value)

# 在请求中带入cookies:
headers = {
    'Cookie': 'q_c1=31653b264a074fc9a57816d1ea93ed8b|1474273938000|1474273938000',
    'Host': 'www.zhihu.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
}
r = requests.get('https://www.zhihu.com', headers=headers)
print(r.text)
'''

# 3、会话维持 Session
# 创建一个cookies，设置number的值为123456789
# requests.get('http://httpbin.org/cookies/set/number/123456789')
# r = requests.get('http://httpbin.org/cookies')
# print(r.text)  # "cookies": {}

'''
s = requests.Session()
s.get('http://httpbin.org/cookies/set/number/123456789')
r = s.get('http://httpbin.org/cookies')
print(r.text)
"cookies": {
    "number": "123456789"
}
'''

# 4、证书认证：
# response = requests.get('https://www.12306.cn')
# print(response.status_code)

import urllib3

urllib3.disable_warnings()
response = requests.get('https://www.12306.cn', verify=False)
print(response.status_code)

# 5、代理设置：
proxies = {
    'http': 'socks5://user:password@host:port',
    'https': 'socks5://user:password@host:port'
}
requests.get("https://www.taobao.com", proxies=proxies)

# 6、超时设置：
r = requests.get("https://www.taobao.com", timeout = 1)
print(r.status_code)

# 7、身份认证:
from requests.auth import HTTPBasicAuth

r = requests.get('http://localhost:5000', auth=HTTPBasicAuth('username', 'password'))
print(r.status_code)

r = requests.get('http://localhost:5000', auth=('username', 'password'))
print(r.status_code)