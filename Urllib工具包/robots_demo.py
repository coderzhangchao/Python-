# coding=utf-8
'''
Robots协议:
    Robots协议也称作爬虫协议、机器人协议，它的全名叫作网络爬虫排除标准（Robots Exclusion Protocol），
    用来告诉爬虫和搜索引擎哪些页面可以抓取，哪些不可以抓取。
    它通常是一个叫作robots.txt的文本文件，一般放在网站的根目录下。
    当搜索爬虫访问一个站点时，它首先会检查这个站点根目录下是否存在robots.txt文件，
    如果存在，搜索爬虫会根据其中定义的爬取范围来爬取。
    如果没有找到这个文件，搜索爬虫便会访问所有可直接访问的页面

    robots.txt 样例：
        User-agent: *
        Disallow: /
        Allow: /public/

        User-agent 描述了搜索爬虫的名称，这里将其设置为*则代表该协议对任何爬取爬虫有效
        Disallow 指定了不允许抓取的目录，比如上例子中设置为/则代表不允许抓取所有页面
        Allow 只允许爬取public目录的功能
'''

# 了解Robots协议之后，我们就可以使用robotparser模块来解析robots.txt了。
# 该模块提供了一个类RobotFileParser，它可以根据某网站的robots.txt文件来判断一个爬取爬虫是否有权限来爬取这个网页
# set_url()  read()  parse()  can_fetch()

from urllib.robotparser import RobotFileParser

rp = RobotFileParser()
rp.set_url('http://www.jianshu.com/robots.txt')
rp.read()
print(rp.can_fetch('*', 'http://www.jianshu.com/p/b67554025d7d'))
# False

print(rp.can_fetch('*', "http://www.jianshu.com/search?q=python&page=1&type=collections"))
# False

# http://www.jianshu.com/robots.txt:
'''
# See http://www.robotstxt.org/wc/norobots.html for documentation on how to use the robots.txt file
#
# To ban all spiders from the entire site uncomment the next two lines:
User-agent: *
Disallow: /search
Disallow: /convos/
Disallow: /notes/
Disallow: /admin/
Disallow: /adm/
Disallow: /p/0826cf4692f9
Disallow: /p/d8b31d20a867
Disallow: /collections/*/recommended_authors
Disallow: /trial/*
Disallow: /keyword_notes
Disallow: /stats-2017/*

User-agent: trendkite-akashic-crawler
Request-rate: 1/2 # load 1 page per 2 seconds
Crawl-delay: 60

User-agent: YisouSpider
Request-rate: 1/10 # load 1 page per 10 seconds
Crawl-delay: 60

User-agent: Cliqzbot
Disallow: /

User-agent: Googlebot
Request-rate: 2/1 # load 2 page per 1 seconds
Crawl-delay: 10
'''