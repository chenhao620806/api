# -*- coding: utf-8 -*-
import unittest
import time
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from Common.ProjectPath.file_path import test_report_path, test_dir_path
from Common.HTMLRunner import HTMLTestRunner
from Common.email_tools import latest_report, send_mail

Run2 = [
    "test_api_request.py",
    "test_bao_biao_request.py",
    "test_crm_request.py",
    "test_erp_request.py",
    "test_Global_request.py",
    "test_jht_request.py",
    "test_kua_jing_request.py",
    "test_sheng_suan_request.py",
    "test_tian_ji_request.py",
    "test_yi_can_request.py",
]

if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d")
    report_name = test_report_path + '/' + now + '-Run2.html'
    with open(report_name, 'wb') as f:
        runner = HTMLTestRunner(stream=f, title="测试报告", description='', verbosity=2, retry=0,
                                save_last_try=True)
        for i in range(len(Run2)):
            discover = unittest.defaultTestLoader.discover(test_dir_path, pattern=Run2[i])
            runner.run(discover)
    f.close()

    latest_report = latest_report(test_report_path)
    # send_mail(latest_report)