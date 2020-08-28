#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/27 15:59
# @Author  : 柠檬菠萝
# @Email   : yzpmihome@vip.qq.com
# @File    : env_settings.py

import os
import platform

def env():
    # 配置环境变量
    if platform.system() == 'Windows':
        os.environ['path'] = "api_lib\\chromedriver_win32;api_lib\\Application"
    elif platform.system() == 'Linux':
        os.environ['PATH'] = "api_lib\/chromedriver_linux64;api_lib\\Application"
    elif platform.system() == 'Darwin':
        os.environ['path'] = "api_lib\/chromedriver_mac64;api_lib\\Application"
    else:
        print(platform.system(), 'NO')
        exit(0)