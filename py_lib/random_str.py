#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/27 17:15
# @Author  : 柠檬菠萝
# @Email   : yzpmihome@vip.qq.com
# @File    : random_str.py
import string
import random


def generate_random_str():
    char = ''.join(random.sample(string.ascii_letters + string.digits, 8))
    url_png_name = "{0}.png".format(hash(char))
    return url_png_name
