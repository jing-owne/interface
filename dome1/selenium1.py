"""
from selenium import  webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()

driver.get("https://www.baidu.com/")

more_link = driver.find_element_by_xpath('//*[@class="mnav s-top-more-btn"]/a')

# 实例化对象
actions = ActionChains(driver)
# 鼠标移动到元素上
actions.move_to_element(more_link).perform()

# 点击百度音乐
driver.find_element_by_xpath('//*[@name="tj_mp3"]/div').click()

# 1. 获取所有打开的浏览器窗口
all_windows = driver.window_handles
print(all_windows,len(all_windows))
driver.switch_to.window(all_windows[-1])


# 新打开百度音乐，在新页面中搜索 helloworld
driver.find_element_by_id('kw').send_keys('helloworld')

# 切换浏览器窗口
driver.switch_to.window(all_windows[0])
driver.find_element_by_id('kw').send_keys('fanmao')

driver.quit()
"""


#css定位元素
# from selenium import webdriver
# from selenium.webdriver import ActionChains
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
#
# driver = webdriver.Chrome(executable_path='./chromedriver.exe')
#
# driver.get("http://49.233.108.117:3000/signin")
# driver.find_element_by_css_selector('#name').send_keys('test10')
# driver.find_element_by_css_selector('#pass').send_keys('123456')
# driver.find_element(By.CSS_SELECTOR,'.span-primary').click()
#
#
# driver.find_element(By.CSS_SELECTOR,'.span-success').click()
#
# driver.find_element(By.ID,'tab-value').click()
# driver.find_element(By.CSS_SELECTOR,'[value="ask"]').click()
#
# driver.find_element(By.ID,'title').send_keys('helloworld')
#
# # 点击图片
# driver.find_element(By.CSS_SELECTOR,'div.editor-toolbar>a:nth-child(9)').click()
#
# # 上传图片
# driver.find_element(By.CSS_SELECTOR,'input[type="file"]').send_keys(r'C:\Users\zengy\Desktop\th.jpg')
#
# # 输入文本
#
# md_div = driver.find_element(By.CSS_SELECTOR,'div.CodeMirror-scroll')
# md_div.click()
# ActionChains(driver).move_to_element(md_div).send_keys('helloworld')\
#     .pause(3)\
#     .send_keys(Keys.ENTER)\
#     .send_keys(Keys.ENTER)\
#     .pause(1).send_keys('### web 自动化')\
#     .send_keys(Keys.ENTER)\
#     .send_keys('hahahahhahahah')\
#     .key_down(Keys.CONTROL).key_down(Keys.SHIFT).send_keys(Keys.ARROW_LEFT)\
#     .key_up(Keys.SHIFT).key_up(Keys.CONTROL)\
#     .key_down(Keys.CONTROL).send_keys('b').key_up(Keys.CONTROL)\
#     .pause(1)\
#     .perform()
#
#
# driver.find_element(By.CSS_SELECTOR,'[type="submit"]').click()


# 拖拽
# from selenium import  webdriver
# from selenium.webdriver import ActionChains
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
# driver.get('https://map.baidu.com/')
# driver.implicitly_wait(30)
# map_div = driver.find_element(By.ID,'mask')
#
# for x in range(100):
#     action = ActionChains(driver)
#     action.click_and_hold(map_div)
#     action.move_by_offset(xoffset=0,yoffset=200).pause(0.2)
#     action.release().perform()

# 隐藏式等待
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
# # 隐式等待 设置最长的等待时间，元素显示出来即可，剩余的等待时间则不再等待；
# driver.implicitly_wait(30) # 最长等待30秒
#
# driver.get("https://www.juhe.cn/")
#
# frame = driver.find_element(By.ID,'layui-layer-iframe1')
# driver.switch_to.frame(frame)
# driver.find_element(By.ID,'mobilephone').send_keys('1111111')


from selenium import webdriver
import os

from selenium.webdriver.common.by import By

chromedriver = os.path.join(os.path.dirname(__file__),'../drivers/chromedriver.exe')
print(chromedriver)

class Client:

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=chromedriver)
        self.driver.implicitly_wait(10)
        self.driver.get('http://49.233.108.117:3000/')

    def action(self,element,**kwargs):
        ele = self.driver.find_element(*element)
        ac = kwargs.get('action')
        if ac == "sendkeys":
            ele.send_keys(kwargs.get('value'))
        elif ac == 'click':
            ele.click()

if __name__ == '__main__':
    import csv

    client = Client()
    file = os.path.join(os.path.dirname(__file__),'../data/data.csv')
    with open(file, encoding='utf8') as f:
        reader = csv.DictReader(f)
        for line in reader:
            print(line)
            client.action((By.XPATH, line['element_xpath']),action=line['action'],value=line['value'])


    #
    # client.action((By.LINK_TEXT,'登录'),action='click')
    # client.action((By.ID,'name'),action='sendkeys',value='test10')
    # client.action((By.ID, 'pass'), action='sendkeys', value='123456')
    # client.action((By.CSS_SELECTOR, '[type="submit"]'), action='click')
