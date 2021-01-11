# -*- coding: utf-8 -*-
import unittest
from unittestreport import TestRunner
from Common.ProjectPath.file_path import test_report_path, test_dir_path, test_report_name

# TestHost = input('请输入测试环境 ：')
# setattr(ConfigBase, 'BaseUrl', TestHost)9999
Run1 = 'test_*'

if __name__ == '__main__':
    # 加载测试用例  正则表达式读取
    discover = unittest.defaultTestLoader.discover(test_dir_path, pattern=Run1)
    runner = TestRunner(suite=discover, filename=test_report_name, report_dir=test_report_path,
                        templates=1, title='接口测试', tester='hongsheng')
    runner.rerun_run(count=0, interval=2)

    # 钉钉提醒
    # runner.dingtalk_notice(url='https://oapi.dingtalk.com/robot/send?access_token=b5931ea7aaa785686d3d6335f9d377dfbce7ae103a17df5ee17dd57314574b4a', key='123456')
    # 邮件发送
    # runner.send_email(host="smtp.163.com", port=465, user="18019781786@163.com", password="FKQXVFFCBTXACPGO", to_addrs=['18019781786@163.com'], is_file=True)
