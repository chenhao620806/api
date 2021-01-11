# -*- coding: utf-8 -*-
import os
import unittest
import logging.config
from unittestreport import ddt, list_data
from TestCase.TestTianJi.set_var_tian_ji import GetDataTianJi
from Common.up_down import StartEnd
from Common.read_excel import DoExcel
from Common.http_request import HttpRequest
from Common.ProjectPath.file_path import log_config_path

logging.config.fileConfig(log_config_path)
# 读取Excel用例/需要运行的用例
excel_path = os.path.join(os.path.dirname(__file__), 'test_tian_ji.xlsx')
# 测试环境
base_url = GetDataTianJi.URL
# 需要运行的用例
case = GetDataTianJi.CaseControl

test_data = DoExcel().pd_read_case(excel_path, case)


@ddt
class TestHTTPRequest(StartEnd):

    @list_data(test_data)
    def test_api(self, item):
        logging.info(f"用例标题：{item['title']} 请求方法：{item['请求方法']}")
        new_url = DoExcel().re_replaces(GetDataTianJi, item['路径'])
        new_data = DoExcel().re_replaces(GetDataTianJi, item['请求数据'])
        # 请求
        res = HttpRequest().http_request(base_url + new_url, eval(new_data), item['请求方法'], cookie=GetDataTianJi.Cookie)
        # 解析响应
        json_data = res.text
        # 消耗时间
        self.total_seconds = res.elapsed.total_seconds()
        logging.info('响应数据：{0}'.format(json_data))

        # cookies
        if res.cookies:
            setattr(GetDataTianJi, 'Cookie', res.cookies)

        # 防跨站
        if item['请求方法'] == 'get':
            VIEWSTATE = DoExcel.re_find(json_data, 'VIEWSTATE')
            setattr(GetDataTianJi, 'VIEWSTATE', VIEWSTATE)
            VIEWSTATEGENERATOR = DoExcel.re_find(json_data, 'VIEWSTATEGENERATOR')
            setattr(GetDataTianJi, 'VIEWSTATEGENERATOR', VIEWSTATEGENERATOR)
            EVENTVALIDATION = DoExcel.re_find(json_data, 'EVENTVALIDATION')
            setattr(GetDataTianJi, 'EVENTVALIDATION', EVENTVALIDATION)

        # 提取订单号
        if item['请求方法'] == 'post' and item['路径'] == '/app/order/order/newOrder.aspx':
            try:
                o_id = DoExcel.re_find(json_data, r'Order\\":{\\"o_id\\":(.*?),')
                if o_id:
                    setattr(GetDataTianJi, 'o_id', o_id)
                logging.info(f'内部订单号：{o_id}')
            except:
                pass
        # 提取出库单号
        if item['请求方法'] == 'post' and item['路径'] == '/app/wms/express/expresssetter.aspx':
            try:
                io_id = DoExcel.re_find(json_data, r'io_id\\":(.*?),')
                if io_id:
                    setattr(GetDataTianJi, 'io_id', io_id)
                logging.info(f'出库单号：{io_id}')
            except:
                pass
        # 提取生成批次号
        if item['请求方法'] == 'post' and item['路径'] == 3:
            try:
                wave_id = DoExcel.re_find(json_data, r'wave_id\\":(.*?),')
                if wave_id:
                    setattr(GetDataTianJi, 'wave_id', wave_id)
                logging.info(f'生成批次号：{wave_id}')
            except:
                pass

        # 提取商品oi_id号
        if item['title'] == '修改快递（京东快递）' and item['sheet_name'] == '订单修改':
            try:
                oi_id = DoExcel.re_find(json_data, r'oi_id\\":(.*?),')
                if oi_id:
                    setattr(GetDataTianJi, 'oi_id', oi_id)
                logging.info(f'oi_id号：{oi_id}')
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


if __name__ == '__main__':
    unittest.main()
