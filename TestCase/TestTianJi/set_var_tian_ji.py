# -*- coding: utf-8 -*-
import time
import random


# re变量反射
class GetDataTianJi(object):
    URL = 'https://www.erp321.com'
    # 账号
    username = 'ZDH@j.com'
    # 密码
    pwd = '1q2w3e4r5t6y!'
    CaseControl = {
        'login': 'all',  # 必须先登录
    }
    # 当前时间戳
    now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
    # 当前时间戳2
    now_time2 = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
    # 随机快递单号
    send_num = str(random.randint(10000000000, 100000000000))
    # 登陆cookies
    Cookie = None
    # 防跨站信息
    VIEWSTATE = None
    VIEWSTATEGENERATOR = None
    EVENTVALIDATION = None
    # 内部订单号
    o_id = None
    # 出库单号
    io_id = None
    # 批次号
    wave_id = None
    # 临时内存变量存储
    dict_var = {}
    # 拆单号
    X_id = None
    # 商品的id号
    oi_id = None


if __name__ == '__main__':
    x = getattr(GetDataTianJi, 'NowTime')
    print(x)