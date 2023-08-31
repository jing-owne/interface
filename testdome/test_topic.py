# 测试话题
import requests


"""###主题首页
def test_index_topic():
    # 发送请求
    url = 'http://49.233.108.117:3000/api/v1/topics'
    quarydata = {
        'page': '1',
        'tab': 'ask',
        'limit': '3',
        'mdrender': 'false'
    }
    r = requests.get(url, params=quarydata)

    # 对结果进行验证
    assert r.status_code == 200

    # 返回数据中的data字段应该为3
    res = r.json()
    print('响应数据', res)
    assert len(res.get('data')) == 3

    # 判断返回数据中的tab 是否为ask
    for obj in res:
        print('获取到的数据', obj)
        assert obj['tab'] == quarydata.get('tab')

        #


# ##获取企业微信的登录token
def test_qiye_wechat():
    url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
    # 企业ID
    # ww88fc20d87e4cdfa1

    # Secret
    # hIICPQ6gsvmCUR8H3xfWxOI8DT1Q0iSBF0FgvhQGdgE
    querydata = {
        "corpid": "ww88fc20d87e4cdfa1",
        "corpsecret": "hIICPQ6gsvmCUR8H3xfWxOI8DT1Q0iSBF0FgvhQGdgE"
    }
    r = requests.get(url, params=querydata)
    # 对结果添加验证
    # 1. error_code  应用为0
    res_json = r.json()
    assert res_json.get("errcode") == 0
    # 2. errmsg ok 返回结果
    assert res_json.get("errmsg") == "ok"
    # 3. access_token 长度小于 等于512字节
    assert len(res_json.get('access_token')) <= 512
    # 4. expires_in 7200s
    assert res_json.get('expires_in') == 7200

"""


import requests,json
from jsonschema import  validate
import pytest

# def test_data():
#     test_data = json.load(open('testdata/test_json.json',encoding='utf8'))
#     for test_title,test_content in test_data.items():
#         # print(test_title,test_content)
#         print(f"开始执行：{test_title}")
#         request_method = test_content.get("method")
#         request_url = test_content.get('url')
#         request_data = test_content.get('data')
#         res_json_schema = test_content.get("json_schema")
#
#         if request_method == "post":
#             r = requests.post(url=request_url,json=request_data)
#             validate(instance=r.json(),schema=res_json_schema)
#         elif request_method == "get":
#             r = requests.get(url=request_url,params=request_data)
#             validate(instance=r.json(),schema=res_json_schema)
#         print('运行结束')




@pytest.mark.parametrize("url,querydata",[("http://49.233.108.117:3000/api/v1/topics",{"limit":1}),("http://49.233.108.117:3000/api/v1/topics",{"limit":2})])
def test_d(url,querydata):
    r = requests.get(url,params=querydata)
    # print(f'执行结果:{r.json()}')
    print(r.request.url)
    print('*'*50)


