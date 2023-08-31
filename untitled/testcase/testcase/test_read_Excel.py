"""
===============
    NAME = guxiaoyu
    2020年 月 27日 小时 分
    E-email:18339435211@139.com
================

----资产配置项目接口
"""

import json
import time

import requests
from pandas import np
import pandas as pd
import xlrd


# 三、资产配置诊断模块(assetAllocationDiagnosis)

def read_Excel():
    excel_path = "C:\\Users\\jishubu\\Desktop\\资配的展示策略文案-蒙板文案版.xlsx"

    # 打开文件，获取excel文件的workbook（工作簿）对象
    excel = xlrd.open_workbook(excel_path, encoding_override="utf-8")

    # 返回所有Sheet对象的list
    all_sheet = excel.sheets()  # Book(工作簿)对象方法
    print(all_sheet)

    sheet_name = []
    sheet_row = []
    sheet_col = []

    # # 返回所有Sheet对象的list
    # all_sheet = excel.sheets()  # Book(工作簿)对象方法
    # # print(all_sheet)
    # sheet_name = excel.sheet_names()
    # print(sheet_name)
    result_map = {}
    for sheet in all_sheet:
        sheet_name.append(sheet.name)

        # print("该Excel共有{0}个sheet,当前sheet名称为{1},该sheet共有{2}行,{3}列"
        #       .format(len(all_sheet), sheet.name, sheet.nrows, sheet.ncols))
        for each_row in range(sheet.nrows):  # 循环打印每一行
            # print("当前为%s行：" % each_row)
            # if each_row != 0 and each_row != 1 and each_row != 2:
            if each_row != 0:
                la = sheet.row_values(each_row)
                col_option01 = int(la[1])
                col_option02 = int(la[2])
                col_option03 = int(la[3])
                col_option04 = int(la[4])

                col_answer01 = str(la[5])  # 文案
                col_answer02 = str(la[6])  # 蒙版文案

                # result_map 字典中的 key
                result_map_key = str(col_option01) + ":" + str(col_option02) + ":" + str(col_option03) + ":" + str(col_option04)
                # result_map 字典中的 value
                result_map_value = str(col_answer01) + "#######test#######" + str(col_answer02)

                result_map[result_map_key] = result_map_value

    return result_map


List = []


def test_risk_questionnaire(data):  # 提交风险测评问卷
    url = 'http://192.168.0.163:16889/eos-api/v1/assetAllocation/risk/questionnaire'
    res = requests.post(url, headers=headers, json=data)
    print("提交风险测评问卷", res.json())
    # 提取数据 写入text文件  比对文案
    if res.json()["code"] == 0:
        return True
    else:
        return False


ques1 = [
    700001,
    700002,
    700003,
    700004
]

ques2 = [
    700005,
    700006,
    700007,
    700008,
    700009,
]

ques3 = [
    700010,
    700011,
    700012,
    700013,
]
ques4 = [
    700014,
    700015,
    700016,
    700013,
]
ques5 = [
    700018,
    700019,
    700020,
    700021,
    700022,
]


def quest(ques1, ques2, ques3, ques4, ques5):
    excel_map = read_Excel()
    result_list = []
    global qu1, qu2, qu3, qu4, qu5, date
    for qu1 in ques1:
        for qu2 in ques2:
            for qu3 in ques3:
                for qu4 in ques4:
                    for qu5 in ques5:
                        # print(ques1, ques2, ques3, ques4, ques5)
                        date = {
                            "answerInfoList": [
                                {
                                    "answer": qu1,  # 700001、35岁以下/2、35岁-50岁/3、50岁-65岁/4、65岁以上
                                    "questionId": 600001  # 您的年龄
                                },
                                {
                                    "answer": qu2,  # 5、无自有房产 6、仅有一套，有贷款 7、仅有一套，无贷款 8、2-3套 9、4套及以上
                                    "questionId": 600002  # 您家庭在二线及以上城市有几套房产
                                },
                                {
                                    "answer": qu3,  # 10、100万以下 11、100万-500万  12、500万-1000万 13、1000万以上
                                    "questionId": 600003  # 您的家庭净资产（家庭总资产减去家庭总负债）中可用及已用于银行存款、股票、基金等金融产品的总金额约？
                                },
                                {
                                    "answer": qu4,  # 14、100万-500万 15、500万-1000万 16、1000万以上
                                    "questionId": 600004  # 您家庭每年的总收入金额大约为（以家庭为单位的总收入)
                                },
                                {
                                    "answer": qu5,  # 18、10%以下 19、10%-20% 20、20%-50% 21、50%-80% 22、80%以上
                                    "questionId": 600005  # 您家庭每年的总支出金额占总收入的比重（日常支出、子女教育、赡养老人等所有家庭支出）
                                }
                            ],
                            "questionnaireId": 500001
                        }

                        excel_map_key = str(qu1) + ":" + str(qu2) + ":" + str(qu5) + ":" + str(qu3)

                        # if qu1 == 700001 and qu3 == 700010:
                        #     print('35岁以下 100万以下')
                        # if qu1 == 700001 and qu3 == 700011:
                        #     print('35岁以下 100-500万')

                        time.sleep(0.06)
                        result_bool = test_risk_questionnaire(date)
                        if result_bool:

                            result_map_value = test_assetAllocation()

                            excel_map_value = excel_map[excel_map_key]

                            print(result_map_value == excel_map_value)

                            result_list_tmp = excel_map_key.split(":", 4)  # ":" -> 拆分表示标识， 4 -> 表示拆分出的结果有几个
                            result_list_tmp.extend(excel_map_value.split("#######test#######", 2))
                            result_list_tmp.append(result_bool)
                            result_list.append(result_list_tmp)
                        else:
                            return
    return result_list


def test_questionnaire(post_data):  # 提交诊断问卷
    url = "http://http://test.yetancaijing.com/eos-api/v1/assetAllocation/ratio/questionnaire"
    res = requests.post(url, headers=headers, json=post_data)
    print("提交诊断问卷：", na, res.json())
    test_assetAllocation()
    if res.json()["code"] == 0:
        return True
    else:
        return False


na1 = [
    700023,
    700024,
    700025,
    700026
]


def question2(na1, excel_map2):
    excel_map2 = read_Excel()
    global na, post_data, i, k, q
    for na in na1:
        for i in range(10, 14):
            if i > 0 and i % 2 == 0:

                for j in range(40,60):
                    if j > 0 and j % 10 == 0:

                        for k in range(10, 30):
                            if k > 0 and k % 10 == 0:

                                for q in range(5,13):
                                    if q > 0 and q % 2 == 0:
                                        # print(str(i) + '万现金 ' + str(j) + '万房产 ' + str(k) + '万金融资产 '
                                        #       + str(q) + '万其他 ' + '总共' + str(i + j + k + q) + '万资产')

                                        # a = i / (i + j + k + q)
                                        b = np.abs(i / (i + j + k + q))
                                        # c = j / (i + j + k + q)
                                        d = np.abs(j / (i + j + k + q))
                                        f = np.abs(k / (i + j + k + q))
                                        g = np.abs(q / (i + j + k + q))

                                        print('现金占比{:.2%}'.format(b), '房产占比{:.2%}'.format(d), '金融资产占比{:.2%}'.format(f),
                                              '其他资产占比{:.2%}'.format(g))
                                        post_data = {
                                            "answerInfoList": [
                                                {
                                                    "answer": na,  # 选项id   23 24 25 26
                                                    "questionId": 600006  # 年龄选项
                                                },

                                                {
                                                    "answer": i,
                                                    "questionId": 600007  # 现金资产
                                                },
                                                {
                                                    "answer": j,
                                                    "questionId": 600008  # 房产
                                                },
                                                {
                                                    "answer": k,
                                                    "questionId": 600009  # 金融资产
                                                },
                                                {
                                                    "answer": q,
                                                    "questionId": 600010  # 其它
                                                }
                                            ],
                                            "questionnaireId": 500002
                                        }
                                        test_questionnaire(post_data)

                                        excel_map_key2 = str(i) + str(j) + str(k) + str(q)
                                        excel_map_key2_format = str(i) + "--" + str(j) + "--" + str(k) + "--" + str(q)

                                        # if qu1 == 700001 and qu3 == 700010:
                                        #     print('35岁以下 100万以下')
                                        # if qu1 == 700001 and qu3 == 700011:
                                        #     print('35岁以下 100-500万')

                                        # time.sleep(0.06)
                                        result_bool = test_risk_questionnaire(date)
                                        if result_bool:

                                            result_map_value = test_assetAllocation()

                                            excel_map_value = excel_map2[excel_map_key2]

                                            if result_map_value == excel_map_value:
                                                print(excel_map_key2_format + " : true")
                                            else:
                                                print(excel_map_key2_format + " : false")

                                        else:
                                            break


# 二、资产配置风险评测模块（riskAssessment）
def test_question():  # （获取题库）
    url = "http://http://test.yetancaijing.com/eos-api/v1/assetAllocation/risk/question"
    get_data = {
        "questionnaireId": 500001  # 问卷ID
    }
    res = requests.get(url=url, headers=headers, params=get_data)
    print("获取题库:", res.json())


def test_assetAllocation():  # 获取用户的风险测评结果
    url = "http://http://test.yetancaijing.com/eos-api/v1/assetAllocation/risk/result"
    get_data = {
        "questionnaireId": 500001  # 问卷ID
    }
    r = requests.get(url=url, headers=headers, params=get_data)
    # question2(na1)
    res = r.text
    # print(res)
    data2 = json.loads(res)
    # print("loads  data2 = ",data2)
    # print("loads  data2['data'] = ",data2['data'])
    List.append(data2['data'])
    # List.extend(data2['data'])
    print("获取用户的风险测评结果:", data2)

    result_map_value = str(data2['data']["analysisReport"]) + "#######test#######" + str(data2['data']["maskInfo"])

    return result_map_value


def test_compositeResult():  # 查询资产配置的风险评测和诊断结果（复合接口）
    url = "http://http://test.yetancaijing.com/eos-api/v1/assetAllocation/ratio/compositeResult"

    get_data = {
        "ratioQuestionnaireId": "500002",  # 诊断问卷ID
        "riskQuestionnaireId": "500001"  # 风险问卷ID
    }
    r = requests.get(url, headers=headers, params=get_data)
    print("查询资产配置的风险评测和诊断结果:", r.text)


def write_excel(result):
    """操作Excel"""
    # print("List == ",List)
    # database = pd.DataFrame(List)
    # # database = np.DataFrame(List,columns=['analysisReport','completed','maskInfo','id'])
    # print("***"*20)
    #
    # database.to_excel('./资产投资.xlsx')
    # print('导出成功')

    print("List == ", result)
    database = pd.DataFrame(result, columns = ['年龄', '房产', '家庭年支出/收入比例', '可支配金额', '文案', '蒙版文案', '执行结果'])
    # database = np.DataFrame(List,columns=['analysisReport','completed','maskInfo','id'])
    print("***" * 20)

    database.to_excel('./资产投资.xlsx')
    print('导出成功')


def test_user():  # 查询用户信息
    url = 'http://test.yetancaijing.com/eos-api/v1/user'
    r = requests.get(url, headers=headers)
    print("查询用户信息", r.json())


if __name__ == '__main__':
    headers = {'token': '413fa4630fe44b7c8dc2f4fea87218bc'}
    # question2(na1)
    result_list = quest(ques1, ques2, ques3, ques4, ques5)
    # test_risk_questionnaire(data)   # 提交风险测评问卷
    # test_questionnaire(post_data)   # 提交诊断问卷
    # test_question()
    # test_assetAllocation()   # 获取用户的风险测评结果
    # test_compositeResult()
    # write_excel(result_list)
    read_Excel()
