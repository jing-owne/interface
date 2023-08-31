"""
===============
    jishubu
    NAME = guxiaoyu
    2021年 月 15日 小时 分
    E-email:18339435211@139.com
================
"""

from selenium import webdriver

driver = webdriver.Chrome()
import time

driver.maximize_window()


def activity(text):
    """
    封装函数， 通过元素的文本值来进行查找元素
    :param text:
    :return:
    """
    # eles = driver.find_elements_by_xpath('//ul[@class="nav pull-right"]/li')
    # for ele in eles:
    #     if ele.text == text:
    #         return ele
    # else:
    #     raise Exception('元素不存在')

driver.get('http://test.yetancaijing.com/admin/#/login')

login = driver.find_element_by_xpath('/html/body/div[1]/div/main/div[2]/form/div[2]/div/div/input').send_keys('guxiaoyu')
passw = driver.find_element_by_xpath('/html/body/div/div/main/div[2]/form/div[3]/div/div[1]/input').send_keys('123456')
driver.add_cookie('')



captca = driver.find_element_by_xpath('/html/body/div[1]/div/main/div[2]/form/div[4]/div/div/div[1]/div/input')

# activity = driver.find_element_by_xpath('/html/body/div[1]/aside/div/ul/li[1]/div/span').click()
#
# driver.implicitly_wait(10)
#
# login = find_element_by_customer_text('登录')
# login.click()
