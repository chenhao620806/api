# -*- coding: utf-8 -*-
import requests
import json


class HttpRequest:
    def http_request(self, url, body, http_method, cookie=None):
        response = None
        session = requests.session()
        try:
            if http_method == 'get':
                response = session.get(url, params=body, cookies=cookie)
            elif http_method == 'post':
                response = session.post(url, data=body, cookies=cookie)
            else:
                pass
        except Exception as e:
            raise e
        return response


class HttpRequestJson:
    def http_request(self, url, body, http_method, cookie=None):
        response = None
        session = requests.session()
        try:
            if http_method == 'get':
                response = session.get(url, params=body, cookies=cookie)
            elif http_method == 'post':
                response = session.post(url, json=json.loads(body), cookies=cookie)
            else:
                pass
        except Exception as e:
            raise e
        return response


if __name__ == '__main__':
    login_url = 'https://j.jushuitan.com'
    data = {'__VIEWSTATE': '',
            'owner_co_id': '',
            'u__': '',
            '__CALLBACKID': 'ACall1',
            '__BASEPARAM': '',
            '__CALLBACKPARAM': '{"Args":["zp02@j.com","ql123123!@#"],"CallControl":"{page}","Method":"Login"}'
            }
    res = HttpRequest().http_request(login_url, data, 'post')
    print(res.text)
    # print(res.elapsed.total_seconds())
    # print(res.status_code)
