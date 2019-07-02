# coding=utf-8
'''
    抓取的目标是今日头条的街拍美图，抓取完成之后，将每组图片分文件夹下载到本地并保存下来
'''
import time
import requests
from urllib.parse import urlencode

base_url = "https://www.toutiao.com/api/search/content/?"
# 毫秒级时间戳
data_time = int(round(time.time() * 1000))
headers = {
    'Host' : 'www.toutiao.com',
    'Referer' : 'https://www.toutiao.com/search/?keyword=%E8%A1%97%E6%8B%8D',
    'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                   'Chrome/73.0.3683.75 Safari/537.36',
    'X-Requested-With' :  'XMLHttpRequest'
}

def get_page(offset):
    parame = {
        'aid' : '24',
        'app_name' : 'web_search',
        'offset' : offset,
        'format' : 'json',
        'keyword' : '街拍',
        'autoload' : 'true',
        'count' : '20',
        'en_qc' : '1',
        'cur_tab' : '1',
        'from' : 'search_tab',
        'pd' : 'synthesis',
        'timestamp' : int(round(time.time() * 1000))
    }
    url = base_url + urlencode(parame)
    print(url)
    try:
        response = requests.get(url,headers=headers)
        if response.status_code == 200:
            return response.json()
        return None
    except:
        print('请求错误...')
        return None


# offset : 0 -- 9
if __name__ == '__main__':
    for i in range(10):
        json = get_page(i)
        print(type(json))
        print(json)

        break



