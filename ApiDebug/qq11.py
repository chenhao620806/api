# import urllib3
# import requests
# import pandas as pd
# from openpyxl import load_workbook
# from openpyxl.styles import Font
#
#
# def write_back(file_name='20201201_menu.xlsx', sheet_name='Sheet1', i=1, result='', pass_time='', writes=None):
#     # 测试响应写回excel文件
#     wb = load_workbook(file_name)
#     sheet = wb[sheet_name]
#     if writes or writes == 0:
#         sheet.cell(i, 8).value = writes
#     else:
#         font_pass = Font(size=11, bold=True, color="00FF00")
#         font_false = Font(size=11, bold=True, color="FF0000")
#
#         if result == 'Pass':
#             sheet.cell(i, 5).font = font_pass
#         else:
#             sheet.cell(i, 5).font = font_false
#
#         sheet.cell(i, 5).value = result
#         sheet.cell(i, 4).value = pass_time
#
#     wb.save(file_name)
#
#
# def pandas_data():
#     df = pd.read_excel('20201201_menu.xlsx', sheet_name='Sheet1')
#     test_data = []
#     for i in df.index.values:
#         row_data = df.loc[i, list(df.head(0))].to_dict()
#         test_data.append(row_data)
#     return test_data
#
#
# urllib3.disable_warnings()
# base_url = 'https://www.erp321.com/'
# session = requests.session()
# data = {'__VIEWSTATE': '', '__VIEWSTATEGENERATOR': '', 'login_id': 'ZDH@j.com', 'password': '1q2w3e4r5t6y!',
#         'verify_code': '', 'mobile': '', 'verification_code': '',
#         'deviceId': 'JBV4SH5BC2NQJEN2CL4WZQD4FD3QHA5V4RUXLWWEIY3MYTBQU2VFQMGKTC53Z2UMH4AFQWEHVGFDSK6C5WHFUHCRWY',
#         '__CALLBACKID': 'ACall', '__CALLBACKPARAM': '{"Method":"Login","CallControl":"{page}"}'}
# resp1 = session.post(url=base_url + '/login.aspx?refer=%2f', data=data, verify=False)
#
# test_data = pandas_data()
#
# result = 'Pass'
# elapsed_time = 1
# for i in test_data:
#     print(i)
#     try:
#         Text = session.get(base_url + i['url'], verify=False, timeout=15)
#         status = Text.status_code
#         elapsed_time = Text.elapsed.total_seconds()
#         result = None
#         if status == 200 and elapsed_time <= 15:
#             result = "Pass"
#         else:
#             result = "Fail"
#     except:
#         elapsed_time = 15
#         result = "TimeOut"
#     finally:
#         write_back(file_name='20201201_menu.xlsx', sheet_name='Sheet1', i=i['id'] + 1, result=result,
#                    pass_time=str(elapsed_time))
#
# test_data2 = pandas_data()
# print(test_data2)
#
# pass_num = 0
# fail_num = 0
# Timeout = 0
# for x in test_data2:
#     if x['测试结果'] == 'Pass':
#         pass_num += 1
#     elif x['测试结果'] == 'Fail':
#         fail_num += 1
#     else:
#         Timeout += 1
#
# write_back(i=2, writes=pass_num)
# write_back(i=3, writes=fail_num)
# write_back(i=4, writes=Timeout)


# -*- coding: utf-8 -*-
import pandas as pd


def pandas_data(file_name, sheet_name):
    df = pd.read_excel(file_name, sheet_name=sheet_name)
    test_data = []
    for i in df.index.values:
        row_data = df.loc[i, list(df.head(0))].to_dict()
        test_data.append(row_data)
    # print(test_data)
    # print(len(test_data), '条')
    for x in test_data:
        # print(x)
        pass
    return test_data


list_data = pandas_data('20201201_menu.xlsx', 'Sheet3')
for i in list_data:
    print(f"{i['名称']} = ['{i['名称']}', ('{i['定位方式']}', '{i['定位语法']}')]")
for i in list_data:
    print(f"self.isElementExit(self.{i['名称']})")
