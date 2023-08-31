from flask import Flask, request
import json
from Mysql import connect, curs

sss = Flask(__name__)
# 默认返回内容
ReturnDic = {
    'return_code': 10086,
    'msg': '查询失败'
}


@sss.route('/index', methods=['POST'])
def InputCropID():
    # 定义参数
    inputData = request.json.get('corp_id')
    userdata = SelectCropID(inputData)
    return userdata


def SelectCropID(inputData):
    global corpdatalist
    try:
        # 查询企业信息
        sql1 = "SELECT corp_id, corp_name,status FROM liz_qywechat_event.qye_tenant where corp_id='%s';" % inputData
        curs.execute(sql1)
        corpcontent = curs.fetchall()
        print(corpcontent)

        CorpList = []
        for row in corpcontent:
            corpdatalist = {
                'corp_id': row[0],
                'corp_name': row[1],
                'status': row[2],
            }
        CorpList.append(corpdatalist)
        connect.close()
        return CorpList

    except:
        return ReturnDic


if __name__ == '__main__':
    sss.run()
