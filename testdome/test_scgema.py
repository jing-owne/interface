"""
使用Schemade 的方式 进行断言

"""
import requests
from jsonschema import validate


def test_topic_schema():
    # 发布话题
    url = "http://49.233.108.117:3000/api/v1/topics"
    post_data = {
        "accesstoken": "eb13d528-667a-4111-9905-5df1c08f1b17",
        "title": "xxxxxxxxxxxxxxxx",
        "tab": "ask",
        "content": "xxxxxxxxxxxetewvdffdgergxxxxxxxxxxxxxx"
    }
    r = requests.post(url, json=post_data)
    print(r.json())

    """
    {'success': True, 'topic_id': '5f9e506a8a40383a1a250371'}
    """

    # 实际运行结果
    sonata = r.json()
    # 使用schema 描述数据的结果
    schema = {
        "type": "object",
        "properties": {
            "success": {"type": "boolean"},
            "topic_id": {"type": "string"}
        }
    }
    # 使用jsonschema 中提供的 validate 方法对结果进行验证
    validate(instance=sonata, schema=schema)