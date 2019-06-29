# coding=utf-8
'''
    提取出猫眼电影TOP100的电影名称、时间、评分、图片等信息
    提取的结果会以文件形式保存下来
'''
import json
import requests
from requests.exceptions import RequestException
import re
import time


def get_one_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None


def parse_one_page(html):
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'
                         + '.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
                         + '.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield {
            'index': item[0],
            'image': item[1],
            'title': item[2],
            'actor': item[3].strip()[3:],
            'time': item[4].strip()[5:],
            'score': item[5] + item[6]
        }

# json.dumps()函数是将一个Python数据类型列表进行json格式的编码
# （可以这么理解，json.dumps()函数是将字典转化为字符串）
def write_to_file(content):
    with open('result.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')


def main(offset):
    url = 'http://maoyan.com/board/4?offset=' + str(offset)
    html = get_one_page(url)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)


if __name__ == '__main__':
    for i in range(10):
        main(offset=i * 10)
        time.sleep(1)

'''
yield的使用：

alist = [1,2,3,4,5]

def addlist(list):
    for i in list:
        yield i+1
        
for i in addlist(alist):
    print(i) 2,3,4,5,6
    
'''