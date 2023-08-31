"""
主要处理API请求
"""
import json
import requests

class HandlerRequests:

    def __init__(self,datafile):
        """

        :param datafile: 测试数据文件的路径
        """
        self.datafile = datafile

    def parse_file(self):
        """
        根据文件路径将文件内容解析为字典数据格式
        :return:
        """
        try:
            return json.load(open(self.datafile,encoding='utf8'))
        except FileNotFoundError: # 如果文件找不到
            print('文件找不到')
            return None

    def do_requests(self,test_data:dict):
        """
        处理请求数据
        :param test_data: 测试数据
        :return:
        """
        for test_title,test_content in test_data.items():
            print(f"开始进行测试{test_title}")
            method:str = test_content.get('method')
            url = test_content.get('url')
            data = test_content.get('data')
            method = method.lower()
            try:
                if method == 'get':
                    r = requests.get(url,params=data)
                    # 执行结果
                    result_data = r.json()
                    test_content['result'] = result_data
                elif method == 'post':
                    r =requests.post(url,json=data)
                    result_data = r.json()
                    test_content['result'] = result_data
            except Exception:
                print('程序出现异常')
                test_content['result'] = "程序运行错误，请人工检查"

        return test_data

    def save_report(self,data,newfilepath):
        """
        将测试结果保存到新文件中
        :param data:  测试数据
        :param newfilepath:  新的文件路径
        :return:
        """
        json.dump(data,open(newfilepath,encoding='utf8',mode='w'),indent=4,ensure_ascii=False)



if __name__ == '__main__':
    hr = HandlerRequests(datafile='../testdata/test_data.json')
    # 1. 解析文件
    testdata = hr.parse_file()
    if testdata:
        newdata = hr.do_requests(test_data=testdata)
        hr.save_report(newdata,newfilepath='./testdata_report.json')