# -*- coding: utf-8 -*-
import xlrd
import urllib3
import requests

urllib3.disable_warnings()


class Jst(object):
    def __init__(self, urls, username, pwd):
        """初始化 登录"""
        self.base_url = urls
        self.session = requests.session()
        # 登录网址
        data = {
            '__VIEWSTATE': '',
            '__VIEWSTATEGENERATOR': '',
            'login_id': username,
            'password': pwd,
            'verify_code': '',
            'mobile': '',
            'verification_code': '',
            'deviceId': 'KMNN4XOTIDBET73MRYFGMP5Z3XN7ZRZ6ZNMC7JC6QPIKY62EAOSOZQFX4WHENC5RBIEK6U23L2PPWTDYYWQ7Y7ZALU',
            '__CALLBACKID': 'ACall',
            '__CALLBACKPARAM': '{"Method":"Login","CallControl":"{page}"}'
        }
        url1 = self.base_url + '/login.aspx'
        resp1 = self.session.post(url=url1, data=data, verify=False)
        if 'LoginOk()' in resp1.text:
            # print(resp1.text)
            print('登陆成功' * 20)
        else:
            print('登录失败' * 20)
        '''=======================================调试开始============================================'''

    # get请求 调试
    def for_get(self, api_url):
        if 'http' in api_url:
            self.base_url = ''
        response = self.session.get(url=self.base_url + api_url, verify=False)
        print('get请求的url：', response.url, '响应结果：', response.text, sep='\n')

    # post请求 调试
    def for_post(self, api_url, body):
        if 'http' in api_url:
            self.base_url = ''
        response = self.session.post(url=self.base_url + api_url, data=body, verify=False)
        print('post请求的url：', response.url, '请求的body', body, '响应结果：', response.text, sep='\n')


class DebugData(object):
    @staticmethod
    def get_excel_data(file_path='1.xlsx', sheet_name='接口body'):
        data = xlrd.open_workbook(file_path)
        tables = data.sheet_by_name(sheet_name)
        lists = []
        for i in range(0, tables.nrows):
            x = tables.row_values(i)
            lists.append(x)

        print('req_body = {')
        for i in lists:
            try:
                row_data = "    '{0}': '{1}', ".format(i[0], int(i[1]))
                print(row_data)
            except:
                row_data = "    '{0}': '{1}', ".format(i[0], i[1])
                print(row_data)
        print('}')
        return lists

    @staticmethod
    def fidder_body():
        req_body = {
            '__VIEWSTATE': '/wEPDwUKLTY3OTg4NjM0OGRkt7ZNWxXEE5i8ncyUkNrs+TyeHv4=',
            '__VIEWSTATEGENERATOR': '8222B990',
            'search': '[{"k":"A.status","v":"SENT","c":"@=","t":""},{"k":"combinesku_type","v":2,"c":"@=","t":""},{"k":"combinesku","v":1,"c":"@=","t":""},{"k":"is_currency","v":0,"c":"@=","t":""},{"k":"A.send_date","v":"2020-12-29","c":">=","t":"date"},{"k":"A.send_date","v":"2021-01-05","c":"<","t":"date"}]',
            'dataPageCount': '',
            '__CALLBACKID': 'ACall1',
            '__CALLBACKPARAM': r'{"Method":"LoadDataToJSON","Args":["1",null,"{\"fld\":\"销售数量\",\"type\":\"desc\"}"],"CallControl":"{page}"}',
        }
        print(req_body)
        print('Copy')
        return req_body


if __name__ == '__main__':
    # 第一步  解析excel  fidder body
    DebugData.get_excel_data()
    # 第二步  二次处理  优化body
    test_body = DebugData.fidder_body()
    # 第三步  登录
    # ApiTest = Jst(urls='https://www.erp321.com', username='ZDH@j.com', pwd='1q2w3e4r5t6y!')
    # 第四步  调试
    url = 'https://bi.erp321.com/app/daas/report/subject/adsorder/channel.aspx?___skutype=combinesku'
    # 请求方法get/post
    # ApiTest.for_get(url)
    # ApiTest.for_post(url, test_body)
