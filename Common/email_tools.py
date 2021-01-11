# -*- coding:utf-8 -*-
import os
import time
import smtplib
import logging
import logging.config
from email.header import Header
from email.mime.text import MIMEText
from Common.ProjectPath.file_path import log_config_path

logging.config.fileConfig(log_config_path)


# 查找最新报告
def latest_report(report_dir):
    lists = os.listdir(report_dir)
    lists.sort(key=lambda fn: os.path.getatime(report_dir + '\\' + fn))
    logging.info("当前最新报告是:" + lists[-1])
    file = os.path.join(report_dir, lists[-1])
    return file


# 发邮件(添加收件人)
def send_mail(report):
    f = open(report, 'rb')
    mail_content = f.read()
    f.close()

    smtpserver = 'smtp.163.com'
    user = '18019781786@163.com'
    password = 'FKQXVFFCBTXACPGO'  # 根据自己邮箱密码来设置

    sender = '18019781786@163.com'
    receives = [
        '18019781786@163.com',  # 邮件接受者
        # '384795247@qq.com',
    ]
    subject = 'JST测试报告'

    msg = MIMEText(mail_content, 'html', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = sender
    msg['To'] = ','.join(receives)

    smtp = smtplib.SMTP_SSL(smtpserver, 465)
    smtp.helo(smtpserver)
    smtp.ehlo(smtpserver)
    smtp.login(user, password)

    time.sleep(5)
    smtp.sendmail(sender, receives, msg.as_string())
    smtp.quit()
    logging.info("Successful! Check your email !")


if __name__ == '__main__':
    report_dir = r'C:\Users\Administrator\Desktop\API\OutFile\HtmlReport'
    latest_report = latest_report(report_dir)
    # print(latest_report)
    # send_mail(latest_report)
