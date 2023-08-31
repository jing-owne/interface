# # 代码块1
# # 使用pip命令安装pytest库
# pip install pytest
#
# #查看pytest的版本信息
# pytest -version

# 代码块2
"""
import pytest


class Test_class:

    def test_001(self):
        print('用例001')
        assert 8 == 8

    def test_002(self):
        print('用例002')
        assert 6 == 6

    def test_003(self):
        print('用例003')
        assert 3 == 2


if __name__ == "__main__":
    # 里面参数需要传list，多个参数放list就不会有警告了
    # pytest.main('-q test_class.py')
    pytest.main(['-q', 'test_class.py'])
"""
# 执行结果
"""
C:\Program Files\Python37\python.exe" C:/Users/jishubu/PycharmProjects/untitled1/balabala/test_class.py
F.F                                                                      [100%]
================================== FAILURES ===================================
_____________________________ Test_class.test_001 _____________________________

self = <test_class.Test_class object at 0x000002CD4193D128>

    def test_001(self):
        print('用例001')
>       assert 6 == 1
E       assert 6 == 1

test_class.py:16: AssertionError
---------------------------- Captured stdout call -----------------------------
用例001
_____________________________ Test_class.test_003 _____________________________

self = <test_class.Test_class object at 0x000002CD4197D4A8>

    def test_003(self):
        print('003')
>       assert 3 == 2
E       assert 3 == 2

test_class.py:24: AssertionError
---------------------------- Captured stdout call -----------------------------
003
=========================== short test summary info ===========================
FAILED test_class.py::Test_class::test_001 - assert 6 == 1
FAILED test_class.py::Test_class::test_003 - assert 3 == 2
2 failed, 1 passed in 0.11s

Process finished with exit code 0

"""

# # 需预先装上pytest-html
# pip install pytest_html

# # 生成html格式的报告
# pytest -v test_1.py --html=Path

# 生成xml格式的报告
# pytest -v test_1.py --junitxml=Path

# 生成txt格式的报告
# pytest -v test_1.py --resultlog=Path
#


# file->Setting->Tools->Python Integrated Tools->项目名称->Default test runner->选择py.test
# 右键选择pytest运行或者直接运行.py文件


"""
生成报告
. test_class.py::Test_class::test_001
. test_class.py::Test_class::test_002
F test_class.py::Test_class::test_003
self = <test_class.Test_class object at 0x000001582B868978>

    def test_003(self):
        print('用例003')
>       assert 3 == 2
E       assert 3 == 2
E         +3
E         -2

test_class.py:24: AssertionError
"""


#
# import  requests
# import json
#
#
# url = 'http://49.233.108.117:3000/api/v1/topics'
# # 发送get请求
# try:
#     res = requests.get(url)
# except requests.exceptions.ConnectionError:  # 当不确定报错类型时
#     print('出现未知异常')
#         print("请求地址:", res.url)
# print("json数据:",res.json)
# print('文本:',res.text)
# print('请求:',res.request)
# print('状态码:',res.status_code)

# 将运行结果 保存到文件中
# json.dump(res.json(),open('.data.json',mode='w',encoding='utf-8'),ensure_ascii = False,indent=4)





# for x in [-1,0,1,2,3,4]:
#     try:                          #选择要执行的代码
#         print(f'10 / {x} =',10/x)
#     except ZeroDivisionError:     #知道0除错误 使用ZeroDivisionError方法
#         print('0不能做除数')
#     except Exception:             #当不确定报错类型时
#         print('出现未知异常')
#     finally:
#         print('执行结束')           #不管有没有异常都会执行
#


import  requests
import json
import pprint

###   get 请求

# query_data= {
#     "page" : 1,
#     "tab" : "ask",
#     "limit" :1,
#     "mdrender":"false"
# }
# url = 'http://49.233.108.117:3000/api/v1/topics'
# try:
#     r= requests.get(url,query_data)
#     print(r.status_code)
#     pp = pprint.PrettyPrinter(indent=4)     #美化输出
#     pp.pprint(r.json())
#
# except Exception:
#     print("hello")
# # json.dump(r.json(),open('.data.json',mode='w',encoding='utf-8'),ensure_ascii = False,indent=4)
# accesstoken ='32f50cd9-f670-48a0-9df6-e614f3a149d4'

# ###  post 请求
# url = 'http://49.233.108.117:3000/api/v1/topics'
# body_data = {
#     "Content-Type":'application/x-www-form-urlencoded',
#     "accesstoken" : '32f50cd9-f670-48a0-9df6-e614f3a149d4',
#     "title": "kengansdggnsdlmnldmmn.msndskjb,,c",
#     "tab" : "ask",
#     "content": "jlsdjgkbjbi'fherjdgsjbjksdgnnbsdhgjbbbdsgkjbsdgdjbhsgv"
# }
# r = requests.post(url,json=body_data)
# print(r.json())

# url = 'https://movie.douban.com/'

import json
import requests
import re
# 简单的自动化接口测试
test_data:dict = json.load(open('test_data.json', encoding ='utf-8'))
print(test_data)

for test_title,test_content in test_data.items():
    print(f'开始测试:{test_title}')
    print(f'测试信息：{test_content}')
    print(f'{test_content.get("method")}')
    #获取字典中的method的字段值
    methodn = test_content.get('method')
    url = test_content.get('url')
    data = test_content.get('data')
    #如果数据中的请求方式为get
    if methodn == "get":
        r = requests.get(url= url,params=data)
    elif methodn == 'post':
        r = requests.post(url = url,json = data)
    #打印服务器响应结果
    print(f'响应状态码：{r.status_code}')
    print(f'响应结果：{r.json()}')
    # print(r.search('topic_id','5f954082efcb8875786d7c08').span)

