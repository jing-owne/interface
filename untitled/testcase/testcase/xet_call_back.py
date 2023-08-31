__author__ = 'yangchuang'
import pandas as pd

import requests
import json
headers = {'Cookie': 'XIAOEID=4e1308b0594b04c7c8b693f2da454315; cookie_channel=2-1568; cookie_is_signed=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22b_u_5bd9952dc4d07_anX9tUze%22%2C%22%24device_id%22%3A%2217362e47ae21a4-051bce22fe53b9-31627405-1296000-17362e47ae3714%22%2C%22props%22%3A%7B%22%24latest_referrer%22%3A%22%22%2C%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22page_submodule%22%3A%22%E8%B4%A6%E5%8F%B7%E4%B8%BB%E9%A1%B5%22%2C%22page_name%22%3A%22%E8%B4%A6%E5%8F%B7%E4%B8%BB%E9%A1%B5_old%22%2C%22page_module%22%3A%22%E5%B0%8F%E9%B9%85%E4%BA%91%22%2C%22page_id%22%3A%224162%22%2C%22page_button%22%3A%22%22%7D%2C%22first_id%22%3A%2217362e47ae21a4-051bce22fe53b9-31627405-1296000-17362e47ae3714%22%7D; channel=16-6821; mobile_manage=0; Hm_lvt_32573db0e6d7780af79f38632658ed95=1604908839,1605088080,1605088082,1606186543; Hm_lpvt_32573db0e6d7780af79f38632658ed95=1606186543; dataUpJssdkCookie={"wxver":"","net":"","sid":""}; Hm_lvt_081e3681cee6a2749a63db50a17625e2=1603793008,1604908829,1606186545; cookie_session_id=T5L0byFuZP7sUsEpo7SghUnPmfV4gBq8; b_user_token=token_5fbccb5a4dc80f06tCqJgcaFQtePB557q; shop_type=B557q; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22b_u_5bd9952dc4d07_anX9tUze%22%2C%22%24device_id%22%3A%2217362e47ae21a4-051bce22fe53b9-31627405-1296000-17362e47ae3714%22%2C%22props%22%3A%7B%22%24latest_referrer%22%3A%22%22%2C%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22page_submodule%22%3A%22%E8%B4%A6%E5%8F%B7%E4%B8%BB%E9%A1%B5%22%2C%22page_name%22%3A%22%E8%B4%A6%E5%8F%B7%E4%B8%BB%E9%A1%B5_old%22%2C%22page_module%22%3A%22%E5%B0%8F%E9%B9%85%E4%BA%91%22%2C%22page_id%22%3A%224162%22%2C%22page_button%22%3A%22%22%7D%2C%22first_id%22%3A%2217362e47ae21a4-051bce22fe53b9-31627405-1296000-17362e47ae3714%22%7D; appsc=appSHsLXnNy5032; with_app_id=appSHsLXnNy5032; Hm_lpvt_081e3681cee6a2749a63db50a17625e2=1606211362; laravel_session=eyJpdiI6IjI1NkRhaXNTUjVQbWxnXC9KRWU4ZlwvUT09IiwidmFsdWUiOiJVWDJpbXZJRGxqb3djNDl0VjU5VW5sRnpsTjYwaGVwZ2dcLzg4VlNKMlBSSHBQdjVWQVk1ejF6SG9pNlwvUGJaYjZWMHVKWmQ0aUh2eVpNY2FqOG90c3pnPT0iLCJtYWMiOiJhNTcyZjU4YzhlZWY4ZjJiZWIyM2JjZGRhNDM0OTgwZThiMzY0ODJiZjM1ZjFjMDNjODY4OTc2M2JkYWQwZGVkIn0%3D'}
url = 'https://admin.xiaoe-tech.com/get/feedback_list?ruler=content&search=&app_type=all&forbid=&page='


def checkRes():
    print('checkRes == ')
    resList = []
    database = pd.DataFrame(list)
    print('database == ',database)
    database.to_excel('./callback.xlsx')



list = []

def que(ind):
    response = requests.get(url+str(ind),headers=headers)
    print('res == ',response)
    res = response.text
    print('res.text == ',res)
    data2 = json.loads(res)
    list.extend(data2['data'])
    print('res.list == ',list)
    if(len(list)>=sizeCoun):
        checkRes()


counter = 1
pageCoun = 117
# sizeCoun = 0
sizeCoun = 1167
while counter <= pageCoun:
    que(counter)
    counter +=1


print('list == ',list)

