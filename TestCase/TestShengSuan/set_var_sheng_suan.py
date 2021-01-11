# -*- coding: utf-8 -*-
import time
import random


# re变量反射
class GetDataShengSuang(object):
    # 账号
    username = 'ZDH@j.com'
    # 密码
    pwd = '1q2w3e4r5t6y!'
    # 当前时间戳
    NowTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
    # 当前时间戳2
    now_time2 = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
    # 随机快递
    send_num = str(random.randint(10 ** 10, 10 ** 11))
    # cookies
    Cookie = None
    # 新建订单号
    order_id = None


if __name__ == '__main__':
    x = getattr(GetDataShengSuang, 'u__')
    print(x)
