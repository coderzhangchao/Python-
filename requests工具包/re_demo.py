# coding=utf-8
# 正则表达式的使用:

import re
import requests

'''
1、match()
    尝试从字符串的起始位置匹配正则表达式，如果匹配，就返回匹配成功的结果；如果不匹配，就返回None
    
    group()  -- 输出完整的匹配结果;
    group(1) -- 输出第一个被()包围的匹配结果
    
    \s -- 匹配任意空白字符
    \w -- 匹配字母、数字及下划线
'''

def demo1():
    content = 'Hello 123 4567 World_This is a Regex Demo'
    print(len(content))
    result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}', content)
    if result != None :
        print(result.group()) # Hello 123 4567 World_This
        print(result.span())  # (0, 25)

    content = 'Hello 1234567 World_This is a Regex Demo'
    result = re.match('^Hello\s(\d+)\sWorld', content)
    if result != None:
        print(result.group())
        print(result.group(1)) # 1234567
        print(result.span())

    # 贪婪与非贪婪模式:
    content = 'Hello 1234567 World_This is a Regex Demo'
    result = re.match('^He.*(\d+).*Demo$', content)
    print(result)
    print(result.group(1)) # 7

    '''
        在贪婪匹配下，.*会匹配尽可能多的字符。
        正则表达式中.*后面是\d+，也就是至少一个数字，并没有指定具体多少个数字，
        因此，.*就尽可能匹配多的字符，这里就把123456匹配了，给\d+留下一个可满足条件的数字7，
        最后得到的内容就只有数字7了
        
        下面的示例:
            He.*?  --- 加 ? 改为非贪婪模式
    '''

    content = 'Hello 1234567 World_This is a Regex Demo'
    result = re.match('^He.*?(\d+).*Demo$', content)
    print(result)
    print(result.group(1))

    # 修饰符: 常用
    #     re.I : 使匹配对大小写不敏感
    #     re.S : 使.匹配包括换行在内的所有字符

# demo1()

'''
2、search()
    匹配时会扫描整个字符串，然后返回第一个成功匹配的结果。
    也就是说，正则表达式可以是字符串的一部分，在匹配时，search()方法会依次扫描字符串，
    直到找到第一个符合规则的字符串，然后返回匹配内容，如果搜索完了还没有找到，就返回None
    
'''
html = '''<div id="songs-list">
        <h2 class="title">经典老歌</h2>
        <p class="introduction">
            经典老歌列表
        </p>
        <ul id="list" class="list-group">
            <li data-view="2">一路上有你</li>
            <li data-view="7">
                <a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
            </li>
            <li data-view="4" class="active">
                <a href="/3.mp3" singer="齐秦">往事随风</a>
            </li>
            <li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
            <li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
            <li data-view="5">
                <a href="/6.mp3" singer="邓丽君"><i class="fa fa-user"></i>但愿人长久</a>
            </li>
        </ul>
    </div>'''

def demo2():
    content = 'Extra stings Hello 1234567 World_This is a Regex Demo Extra stings'
    result = re.match('Hello.*?(\d+).*?Demo', content)
    print(result) # None

    print('**************')

    content = 'Extra stings Hello 1234567 World_This is a Regex Demo Extra stings'
    result = re.search('Hello.*?(\d+).*?Demo', content)
    print(result)
    if result != None:
        print(result.group()) # Hello 1234567 World_This is a Regex Demo

    print('********************************')

    # 尝试提取class为active的li节点内部的超链接包含的歌手名和歌名
    # <li.*?active.*?singer="(.*?)">(.*?)</a>
    result = re.search('<li.*?active.*?singer="(.*?)">(.*?)</a>', html, re.S)
    if result:
        print(result.group(1), result.group(2)) # 齐秦 往事随风

# demo2()

'''
3、findall()
    该方法会搜索整个字符串，然后返回匹配正则表达式的所有内容。
'''

def demo3():
    # 获取所有a节点的超链接、歌手和歌名
    results = re.findall('<li.*?href="(.*?)".*?singer="(.*?)">(<i.*</i>)*(.*?)</a>', html , re.S)
    # print(results)
    # print(type(results))
    for result in results:
        # print(result)
        print(result[0], result[1], result[3])

# demo3()

'''
4、sub()
    把一串文本中的所有数字都去掉，如果只用字符串的replace()方法，
    那就太烦琐了，这时可以借助sub()方法
'''

def demo4():
    content = '54aK54yr5oiR54ix5L2g'
    content = re.sub('\d+', '', content)
    print(content) # aKyroiRixLg

    sub_html = re.sub('<a.*?>|</a>', '', html)
    print(sub_html)
    results = re.findall('<li.*?>(.*?)</li>', sub_html, re.S)
    for result in results:
        print(result.strip())

# demo4()

'''
5、compile()
'''

def demo5():
    content1 = '2016-12-15 12:00'
    content2 = '2016-12-17 12:55'
    content3 = '2016-12-22 13:21'
    pattern = re.compile('\d{2}:\d{2}')
    result1 = re.sub(pattern, '', content1)
    result2 = re.sub(pattern, '', content2)
    result3 = re.sub(pattern, '', content3)
    print(result1, result2, result3)
    # 2016 - 12 - 15  2016 - 12 - 17  2016 - 12 - 22

demo5()