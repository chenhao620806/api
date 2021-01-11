#
#
#
# from locust import HttpUser, TaskSet, task
#
#
# # 定义用户行为
# class UserBehavior(TaskSet):
#     def on_start(self):
#         print("start")
#
#     @task(1)
#     def bky_index(self):
#         self.client.get("/")
#
#     @task(2)
#     def blogs(self):
#         self.client.get("/Clairewang/p/8622280.html")
#
#
# class WebsiteUser(HttpUser):
#     host = "https://www.cnblogs.com"
#     tasks = [UserBehavior]
#     min_wait = 2000
#     max_wait = 7000

#  locust -f C:\Users\Administrator\Desktop\API\ApiDebug\testlocust.py --master 调度机
#  locust -f C:\Users\Administrator\Desktop\API\ApiDebug\testlocust.py --worker 执行机
#  http://localhost:8089/


# -*- coding: utf-8 -*-


# ---------------------------------------------------
import urllib3
import requests
import json

urllib3.disable_warnings()
session = requests.session()
url = 'https://fi.jushengsuan.com/api/zz/open/UserLogin/login?_A_C_I_D='
data = '''{"preToken":"ED4C9A27A00FA4652128C555F41535CC","username":"ZDH@j.com","password":"MXEydzNlNHI1dDZ5IQ==","checkCode":"bwc8","rememberMe":false}'''
res = session.post(url, json=json.loads(data), verify=False)
print(res.text)
print(res.cookies)
# res2 = session.get('https://asia.jsterp.com/OMS/Order/Create', cookies=res.cookies)
# # print(res2.text)

# x = '''{"CreateOrderLabelRequests":[],"CreateOrderRequest":{"OrderId":null,"PlatformOrderId":null,"OrderType":"","WarehouseId":"99","SettlementMethod":"","ShopId":11005333,"PlatformBuyerId":"","LogisticsCompanyCode":null,"OrderTime":null,"PayTime":"2021-1-5 16:56:11","IsCod":false,"Salesman":"","OfflineNote":"","BuyerMessage":"","SellerRemark":"","BuyerId":null,"ReceiverCountry":"","ReceiverProvince":"","ReceiverCity":"","ReceiverDistrict":"","ReceiverAddress":"","DeliveryWay":"SelfTake","ReceiverFirstName":"红升","ReceiverLastName":"","ReceiverPhone":"","ReceiverMobile":"18019781786","ReiceiverIdCard":"","PayAmount":30,"FreightIncome":0,"PaidAmount":"30.00","ShopFreeAmount":0,"InvoiceTitle":null,"InvoiceTaxNo":null,"Amount":30},"CreateOrderItemRequests":[{"SkuId":"KS02-1","ItemId":"KS02","Name":"FDDFFDF","CostPrice":10,"BasePrice":30,"Price":30,"Qty":1,"Amount":30,"SafetyStockQty":18,"NameplatePrice":40,"WholesalePrice":10,"MemberPrice":20,"SalePrice":30,"IsGift":false,"Weight":0,"Pic":"https://upyun.dinghuale.com/uploads/20200713/202007131103233026.jpg","PropertiesValue":"","SkuType":"Normal"}]}'''
# res3 = session.post('https://asia.jsterp.com/OMS/Order/Create', json=json.loads(x), verify=False, cookies=res.cookies)
# print('666', res3.text)
