# -*- coding: utf-8 -*-
import os
import time

# 根目录API
project_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
# print(project_path)

# 日志配置
log_config_path = os.path.join(project_path, 'Common', 'log.conf')
# print(log_config_path)

# 日志路径
log_path = os.path.join(project_path, 'OutFile', 'Log', 'log.log')
# print(log_path)

# 报告路径
test_report_path = os.path.join(project_path, 'OutFile', 'HtmlReport')
# print(test_report_path)

# 被测试目录
test_dir_path = os.path.join(project_path, 'TestCase')
# print(test_dir_path)

# 测试报告名称（时间戳命名）
# test_report_name = test_report_path + '/' + time.strftime("%Y-%m-%d %H_%M_%S") + 'HTML.html'
test_report_name = test_report_path + '/' + time.strftime("%Y-%m-%d") + '-Run1.html'
