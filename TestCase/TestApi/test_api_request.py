# -*- coding: utf-8 -*-
import os
import unittest
import logging.config
from Common.up_down import StartEnd
from Common.read_excel import DoExcel
from Common.http_request import HttpRequest
from Common.ProjectPath.file_path import log_config_path
from unittestreport import ddt, list_data
from TestCase.TestApi.set_var_api import GetDataApi

logging.config.fileConfig(log_config_path)

# 读取Excel用例/需要运行的用例
excel_path = os.path.join(os.path.dirname(__file__), 'test_api.xlsx')
# 测试环境
base_url = 'https://j.jushuitan.com'
# 需要运行的用例
case = {
    'login': 'all',  # 必须先登录
}
test_data = DoExcel().pd_read_case(excel_path, case)


@ddt
class TestHTTPRequest(StartEnd):

    @list_data(test_data)
    def test_api(self, item):
        logging.info(f"用例标题：{item['title']} 请求方法：{item['请求方法']}")
        # 首先正则替换url/body ${}
        new_url = DoExcel().re_replaces(GetDataApi, item['路径'])
        new_data = DoExcel().re_replaces(GetDataApi, item['请求数据'])
        # 请求
        res = HttpRequest().http_request(base_url + new_url, eval(new_data), item['请求方法'], cookie=GetDataApi.Cookie)
        # 解析响应
        json_data = res.text
        # 消耗时间
        self.total_seconds = res.elapsed.total_seconds()
        logging.info('响应数据：{0}'.format(json_data))

        # cookies
        if res.cookies:
            setattr(GetDataApi, 'Cookie', res.cookies)

        # 提取订单号
        if item['title'] == '新建红升商品订单' and item['路径'] == '/jht/webapi/saleorder.aspx':
            try:
                order_id = DoExcel.re_find(json_data, r'ReturnValue\":(.*?),')
                if order_id:
                    setattr(GetDataApi, 'o_id', order_id)
                logging.info(f'订单号：{order_id}')
            except:
                pass
        try:
            self.assertIn(str(item['断言']), json_data)
            self.TestResult = '通过'
        except AssertionError as e:
            self.TestResult = '失败'
            logging.error(
                '失败sheet名:{0},case_ID: {1},失败原因-->{2} '.format(item['sheet_name'], item['ID'], e))
            raise
        finally:
            DoExcel.write_back(excel_path, item['sheet_name'], item['ID'] + 1, json_data, self.TestResult,
                               self.total_seconds)
            # #写入pass/fail数据
            # if self.TestResult == '通过':
            #     json_data = ''
            #     DoExcel.write_back(excel_path, item['sheet_name'], item['ID'] + 1, json_data, self.TestResult,
            #                        self.total_seconds)
            # else:
            #     DoExcel.write_back(excel_path, item['sheet_name'], item['ID'] + 1, json_data, self.TestResult,
            #                        self.total_seconds)


if __name__ == '__main__':
    unittest.main()
