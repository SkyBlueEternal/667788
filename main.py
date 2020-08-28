#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/27 16:47
# @Author  : 柠檬菠萝
# @Email   : yzpmihome@vip.qq.com
# @File    : main.py

from py_lib import env_settings
from py_lib import dynamic_crawler
from py_lib import logo_recognition

env_settings.env()
tmp = dynamic_crawler.RequestsHttp(url="http://61.178.32.110:8086/").requests_get()
key = ""
value = ""
for k, v in tmp.items():
    key = k
    value = v
rus = logo_recognition.LogoRec().test_xfeatures2d(key, "zhongshiyou.png")
print(rus)
