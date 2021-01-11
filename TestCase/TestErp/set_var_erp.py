# -*- coding: utf-8 -*-
import time
import random


# re变量反射
class GetData(object):
    URL = 'https://www.erp321.com'
    # 账号
    username = 'ZDH@j.com'
    # 密码
    pwd = '1q2w3e4r5t6y!'
    ErpControl = {
        'login': 'all',  # 必须先登录
        "直接发货": 'all',
        "详情发货": 'all',
        "生成批次": 'all',
        "订单取消": 'all',
        "拆分合并": 'all',
        "订单修改": 'all',
        "赠品规则": 'all',
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
    x = getattr(GetData, 'Cookie')
    print(x)
