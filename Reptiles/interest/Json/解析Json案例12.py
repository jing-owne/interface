# -*- coding: utf-8 -*-
"""
Created on 2020年11月9日16:53:41

@author: guxiaoyu

微信公众号: python养成计划

"""
import json
dict_data = {
    "animals": {
        "dog": [
            {
                "name": "Rufus",
                "age":15
            },
            {
                "name": "Marty",
                "age": 'null'
            }
        ]
    }
}
# 将dict格式数据转换成json格式字符串
dump_data = json.dumps(dict_data)
load_data = json.loads(dump_data)
data = load_data.get("animals").get("dog")
result1 = []
for i in data:
    result1.append(i.get("name"))
print(result1)


import jsonpath
load_data = json.loads(dump_data)
jobs=load_data['animals']['dog']
result2 = []
for i in data:
    result2.append(jsonpath.jsonpath(i,'$..name')[0])
print(result2)










