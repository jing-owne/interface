# -*- coding: utf-8 -*-

"""
Created on 2020年11月9日16:58:14

@author: guxiaoyu

微信公众号:
"""



from bs4 import BeautifulSoup
import pandas as pd
import requests

url = 'http://comment.bilibili.com/123519261.xml'
html = requests.get(url)
html.encoding='utf8'

soup = BeautifulSoup(html.text, 'lxml')
results = soup.find_all('d')

comments = [comment.text for comment in results]
comments_dict = {'comments': comments}

df = pd.DataFrame(comments_dict)
df.to_csv('bili_ai5.csv', encoding='utf-8-sig')