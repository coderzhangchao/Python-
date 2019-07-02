# coding=utf-8
'''
Selenium是一个自动化测试工具，利用它可以驱动浏览器执行特定的动作，如点击、下拉等操作，
同时还可以获取浏览器当前呈现的页面的源代码，做到可见即可爬。对于一些JavaScript动态渲染的页面来说，此种抓取方式非常有效。

pip install selenium -i https://mirrors.aliyun.com/pypi/simple/
安装：chromedriver
    官方网站：https://sites.google.com/a/chromium.org/chromedriver
    下载地址：https://chromedriver.storage.googleapis.com/index.html

如果能打开浏览器，说明配置正确
driver = webdriver.Chrome()

'''
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

'''
# 入门代码示例:
browser = webdriver.Chrome() # 打开浏览器
try:
    # 访问网页
    browser.get('https://www.baidu.com')
    # 查找节点
    input = browser.find_element_by_id('kw')
    # input 框设值
    input.send_keys('Python')
    input.send_keys(Keys.ENTER)
    # 隐式等待
    wait = WebDriverWait(browser, 10)
    wait.until(EC.presence_of_element_located((By.ID, 'content_left')))
    print(browser.current_url)
    print(browser.get_cookies())
    print(browser.page_source)
finally:
    time.sleep(10)
    # 关闭浏览器
    browser.close()
    
'''

'''
1、声明浏览器对象：
    from selenium import webdriver

    browser = webdriver.Chrome()
    browser = webdriver.Firefox()
    browser = webdriver.Edge()
    browser = webdriver.PhantomJS()
    browser = webdriver.Safari()
    
'''

'''
2、访问网页：
    from selenium import webdriver
 
    browser = webdriver.Chrome()
    browser.get('https://www.taobao.com')
    
    # 打印网页源码
    print(browser.page_source)
    browser.close()
    
'''

'''
3、查找节点
    from selenium import webdriver
 
    browser = webdriver.Chrome()
    browser.get('https://www.taobao.com')
    
    input_first = browser.find_element_by_id('q')
    input_second = browser.find_element_by_css_selector('#q')
    input_third = browser.find_element_by_xpath('//*[@id="q"]')
    
    print(input_first, input_second, input_third)
    browser.close()
    
    所有获取单个节点的方法:
        find_element_by_id
        find_element_by_name
        find_element_by_xpath
        find_element_by_link_text
        find_element_by_partial_link_text
        find_element_by_tag_name
        find_element_by_class_name
        find_element_by_css_selector
        
        Selenium还提供了通用方法find_element()，它需要传入两个参数：
        查找方式By和值。实际上，它就是find_element_by_id()这种方法的通用函数版本，
        比如find_element_by_id(id)就等价于find_element(By.ID, id)
        
        from selenium import webdriver
        from selenium.webdriver.common.by import By
         
        browser = webdriver.Chrome()
        browser.get('https://www.taobao.com')
        input_first = browser.find_element(By.ID, 'q')
        print(input_first)
        browser.close()
        
    多个节点: -- find_elements
        from selenium import webdriver
 
        browser = webdriver.Chrome()
        browser.get('https://www.taobao.com')
        lis = browser.find_elements_by_css_selector('.service-bd li')
        print(lis)
        browser.close()

'''

'''
4、节点之间的交互：
    from selenium import webdriver
    import time
     
    browser = webdriver.Chrome()
    browser.get('https://www.taobao.com')
    # 搜索输入框
    input = browser.find_element_by_id('q')
    # 输入框设值
    input.send_keys('iPhone')
    time.sleep(1)
    # 清空输入框
    input.clear()
    input.send_keys('iPad')
    # 获取按钮并点击
    button = browser.find_element_by_class_name('btn-search')
    button.click()
'''

# 测试拖拽
from selenium.webdriver import ActionChains
def demo():
    browser = webdriver.Chrome()
    url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
    try:
        browser.get(url)
        # 切换到子页面中
        browser.switch_to.frame('iframeResult')
        source = browser.find_element_by_css_selector('#draggable')
        target = browser.find_element_by_css_selector('#droppable')

        actions = ActionChains(browser)
        actions.drag_and_drop(source, target)
        actions.perform()
    finally:
        time.sleep(10)
        browser.close()
# demo()

'''
5、执行JavaScript  --- execute_script
'''
def demo1():
    browser = webdriver.Chrome()
    browser.get('https://www.zhihu.com/explore')

    browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    browser.execute_script('alert("To Bottom")')

# demo1()

'''
6、获取节点信息
    get_attribute()方法来获取节点的属性:
    
    browser = webdriver.Chrome()
    url = 'https://www.zhihu.com/explore'
    browser.get(url)
    logo = browser.find_element_by_id('zh-top-link-logo')
    print(logo)
    print(logo.get_attribute('class'))
    
    获取文本值: WebElement节点的text属性：
    browser = webdriver.Chrome()
    url = 'https://www.zhihu.com/explore'
    browser.get(url)
    input = browser.find_element_by_class_name('zu-top-add-question')
    print(input.text)
    
    获取id、位置、标签名和大小：
    browser = webdriver.Chrome()
    url = 'https://www.zhihu.com/explore'
    browser.get(url)
    input = browser.find_element_by_class_name('zu-top-add-question')
    
    # id属性可以获取节点id
    print(input.id)
    
    # location属性可以获取该节点在页面中的相对位置
    print(input.location)
    print(input.tag_name)
    
    # size属性可以获取节点的大小，也就是宽高
    print(input.size)
    
'''

'''
Frame:
    我们知道网页中有一种节点叫作iframe，也就是子Frame，相当于页面的子页面，它的结构和外部网页的结构完全一致。
    Selenium打开页面后，它默认是在父级Frame里面操作，而此时如果页面中还有子Frame，
    它是不能获取到子Frame里面的节点的
'''
from selenium.common.exceptions import NoSuchElementException

def demo2():
    browser = webdriver.Chrome()
    url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
    browser.get(url)

    browser.switch_to.frame('iframeResult')

    try:
        logo = browser.find_element_by_class_name('logo')
    except NoSuchElementException:
        print('NO LOGO')

    browser.switch_to.parent_frame()

    logo = browser.find_element_by_class_name('logo')
    print(logo)
    print(logo.text)

    time.sleep(10)

# demo2()

'''
延时等待：

    隐式等待  --- browser.implicitly_wait(10)
    当使用隐式等待执行测试的时候，如果Selenium没有在DOM中找到节点，将继续等待，超出设定时间后，
    则抛出找不到节点的异常。换句话说，当查找节点而节点并没有立即出现的时候，
    隐式等待将等待一段时间再查找DOM，默认的时间是0
    
    from selenium import webdriver
 
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    browser.get('https://www.zhihu.com/explore')
    input = browser.find_element_by_class_name('zu-top-add-question')
    print(input)
    
    显式等待：
    
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    
    # 等待条件
    from selenium.webdriver.support import expected_conditions as EC
     
    browser = webdriver.Chrome()
    browser.get('https://www.taobao.com/')
    wait = WebDriverWait(browser, 10)
    
    # 节点出现
    input = wait.until(EC.presence_of_element_located((By.ID, 'q')))
    
    # 可点击
    button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-search')))
    print(input, button)
    
'''

'''
前进和后退:

    browser = webdriver.Chrome()
    browser.get('https://www.baidu.com/')
    browser.get('https://www.taobao.com/')
    browser.get('https://www.python.org/')
    
    # 后退
    browser.back()
    time.sleep(1)
    
    # 前进
    browser.forward()
    browser.close()
'''

'''
Cookies：
    
    browser = webdriver.Chrome()
    browser.get('https://www.zhihu.com/explore')
    
    # 获取Cookies
    print(browser.get_cookies())
    
    # 添加Cookies
    browser.add_cookie({'name': 'name', 'domain': 'www.zhihu.com', 'value': 'germey'})
    print(browser.get_cookies())
    
    # 删除
    browser.delete_all_cookies()
    print(browser.get_cookies())
'''

'''
选项卡管理：

    browser = webdriver.Chrome()
    browser.get('https://www.baidu.com')
    
    browser.execute_script('window.open()')
    print(browser.window_handles)
    
    browser.switch_to_window(browser.window_handles[1])
    browser.get('https://www.taobao.com')
    
    time.sleep(1)
    browser.switch_to_window(browser.window_handles[0])
   
    browser.get('https://python.org')
    
'''

'''
异常处理：

    from selenium import webdriver
    from selenium.common.exceptions import TimeoutException, NoSuchElementException
 
    browser = webdriver.Chrome()
    try:
        browser.get('https://www.baidu.com')
    except TimeoutException:
        print('Time Out')
    try:
        browser.find_element_by_id('hello')
    except NoSuchElementException:
        print('No Element')
    finally:
        browser.close()
        
'''
