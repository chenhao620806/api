# -*- coding: utf-8 -*-
import time
import random


# re变量反射
class GetDataBaoBiao(object):
    # 账号
    username = 'ZDH@j.com'
    # 密码
    pwd = '1q2w3e4r5t6y!'
    # 当前时间戳
    NowTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
    # 当前时间戳2
    now_time2 = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
    # 随机快递单号
    send_num = str(random.randint(10 ** 10, 10 ** 11))
    # 登陆cookies
    Cookie = None
    # 防跨站信息
    VIEWSTATE = None
    VIEWSTATEGENERATOR = None
    EVENTVALIDATION = None
    # 新建订单号
    order_id = None


if __name__ == '__main__':
    x = getattr(GetDataBaoBiao, 'Cookie')
    print(x)
