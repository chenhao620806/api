# -*- coding: utf-8 -*-
import time
import random


# re变量反射
class GetDataGlobal(object):
    # 账号
    username = 'zp02@j.com'
    # 密码
    pwd = 'ql123123!@#'
    # 当前时间戳
    NowTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
    # 当前时间戳2
    now_time2 = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
    # 随机快递单号
    send_num = str(random.randint(10 ** 10, 10 ** 11))
    # 登陆cookies
    Cookie = None
    # 新建订单号
    o_id = None


if __name__ == '__main__':
    x = getattr(GetDataGlobal, 'u__')
    print(x)
