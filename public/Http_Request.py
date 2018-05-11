# -*- coding: utf-8 -*-
# @Time    : 2018/4/13 10:16
# @Author  : XQQ
# @File    : Http_Request
# @Software: PyCharm Community Edition
import requests
class Http_Request:
    def get_Request(self,url,params):
        result = requests.get(url, params)
        return result
    def post_Request(self,url,params):
        result = requests.post(url, params)
        return result