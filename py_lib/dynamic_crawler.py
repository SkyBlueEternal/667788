#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/27 15:57
# @Author  : 柠檬菠萝
# @Email   : yzpmihome@vip.qq.com
# @File    : dynamic_crawler.py
from py_lib import random_str
from seleniumrequests import Chrome
from selenium.webdriver.chrome.options import Options


class RequestsHttp:
    # 模拟浏览器请求方法
    def __init__(self, url):
        self.url = url
        self.driver = ""
        self.page_source = ""
        self.res = ""
        self.url_png_name = random_str.generate_random_str()
        self.options = Options()
        self.options.add_argument("start-maximized")
        self.options.add_argument("disable-infobars")
        self.options.add_argument("--disable-extensions")
        self.options.add_argument('--headless')
        self.options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = Chrome(options=self.options)
        self.driver.set_window_size(1200, 300)

    def requests_get(self):
        # GET 模拟请求
        try:
            self.driver.get(self.url)
        except Exception as e:
            print("requests_get_err:", e)
            self.driver.quit()
            pass
        else:
            self.page_source = self.driver.page_source
            self.driver.get_screenshot_as_file(self.url_png_name)
            self.driver.quit()
            return {self.url_png_name:self.page_source}

    def requests_post(self):
        # POST 模拟请求
        try:
            self.res = self.driver.request('POST', self.url)
        except Exception as e:
            print("requests_post_err:", e)
            self.driver.quit()
            pass
        else:
            self.driver.encoding = 'utf-8'
            self.page_source = self.res.text
            self.driver.get_screenshot_as_file(self.url_png_name)
            self.driver.quit()
            return {self.url_png_name:self.page_source}
