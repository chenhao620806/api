# -*- coding: utf-8 -*-
import time
import random


# re变量反射
class GetDataJht(object):
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
    order_id = None

    BASEPARAM = '{"app_name":"聚货通","app_version":"2.2.7","factory":"Xiaomi","opsystem":"android","opsystem_version":"10","phone_model":"mi max 3","screen_resolution":"1080*1080"}'
    u__ = '{"u_co_id":"10158260","u_co_name":"测试公司002","u_id":"22906","u_name":"秋萝2","u_cid":"132536830997562685","u_dbc":"1","u_tt":"1","u_r":"11,12,13,14,15,17,22,23,27,28,29,30,31,32,33,34,35,36,39,40,41,52,53,54,61,62","u_proxy":null,"u_co_type":"标准商家","u_t":"%s","u_lid":"zp02@j.com","u_sign":"2122712.7AFAAE8E47714604B657507B7454E5AD,40e73681b245a49b5429a470d10c8ab0","u_shop":"","u_apps":"1,2,4,5,6,7,8,9,10,12,15","u_ug_id":"","u_pwd_valid":"0","u_drp":"","u_app":"App","data":null,"safe_level":2,"mobile":"177*****088"}'%NowTime


if __name__ == '__main__':
    x = getattr(GetDataJht, 'u__')
    print(x)
