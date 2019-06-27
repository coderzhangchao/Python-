# coding=utf-8

# 处理异常
# urllib的error模块定义了由request模块产生的异常
from urllib import request, error

'''
try:
    response = request.urlopen('http://cuiqingcai.com/index.htm')
except error.URLError as e:
    print(e.reason) # Not Found
'''

# HTTPError：它是URLError的子类，专门用来处理HTTP请求错误，比如认证请求失败等
'''
try:
    response = request.urlopen('http://cuiqingcai.com/index.htm')
except error.HTTPError as e:
    print(e.reason, e.code, e.headers, sep='\n')
'''

# 推荐写法:
try:
    response = request.urlopen('http://cuiqingcai.com/index.htm')
except error.HTTPError as e:
    print(e.reason, e.code, e.headers, sep='\n')
except error.URLError as e:
    print(e.reason)
else:
    print('Request Successfully')