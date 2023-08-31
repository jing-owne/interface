"""
===============
    jishubu
    NAME = guxiaoyu
    2020年 月 30日 小时 分
    E-email:18339435211@139.com
================
"""

import csv
import os
import pytest
import requests

# with open('data.csv',mode='w',encoding='utf8',newline='') as csvfile:
#     w = csv.writer(csvfile)
#     w.writerow(['用户名','密码'])
#     for i in range(1,101):
#         w.writerow(['test'+str(i),'123456'])


logincsv = os.path.join(os.path.dirname(__file__),'..testcase/ddt_file/data.csv')
test_data = []

with open(logincsv,encoding='utf8') as csvfile:
    r = csv.reader(csvfile)
    for line in r:
        test_data.append(line)
test_data.pop(0)

@pytest.mark.parametrize('username,passwd',test_data)
def test_login(username,passwd):
    url = 'http://49.233.108.117:3000/signin'
    login_data = {
        'name':username,
        'pass':passwd,
        '_csrf':None
    }
    r = requests.post(url,data=login_data)
    assert r.status_code == 200