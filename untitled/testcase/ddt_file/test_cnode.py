"""
===============
    jishubu
    NAME = guxiaoyu
    2021年 月 14日 小时 分
    E-email:18339435211@139.com
================
"""


from telnetlib import EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
import time

driver.maximize_window()

def find_element_by_customer_text(text):
    """
    封装函数， 通过元素的文本值来进行查找元素
    :param text:
    :return:
    """
    eles = driver.find_elements_by_xpath('//ul[@class="nav pull-right"]/li')
    for ele in eles:
        if ele.text == text:
            return ele
    else:
        raise Exception('元素不存在')


driver.get('http://49.233.108.117:3000/')

api = find_element_by_customer_text('API')
api.click()
driver.implicitly_wait(10)

login = find_element_by_customer_text('登录')
login.click()

send_name = driver.find_element_by_xpath('//*[@id="name"]').send_keys('guxiaoyu')
send_pw = driver.find_element_by_xpath('//*[@id="pass"]').send_keys('123456')
signin = driver.find_element_by_xpath('//*[@id="signin_form"]/div[3]/input').click()

# WebDriverWait(driver,3).until(EC.presence_of_element_located((By.XPATH,'//ul[@class="nav pull-right"]/li[2]')))
# driver.find_element(By.XPATH,'//ul[@class="nav pull-right"]/li[2]').click()

driver.implicitly_wait(1)
top = driver.find_element_by_xpath('/html/body/div[1]/div/div/ul/li[1]/a').click()

