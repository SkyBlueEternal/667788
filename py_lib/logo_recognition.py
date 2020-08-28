#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/27 16:00
# @Author  : 柠檬菠萝
# @Email   : yzpmihome@vip.qq.com
# @File    : logo_recognition.py

import cv2
from matplotlib import pyplot as plt
from py_lib import random_str


class LogoRec:
    """
        :param 使用神经网络比较图片logo
    """
    def __init__(self):
        self.orb = cv2.xfeatures2d.SURF_create()

    def test_xfeatures2d(self, query, taste):
        """
        :param query: 传入待检测目标
        :param taste: 传入样本
        :return: 返回字典格式{"成功或者失败":"图片名称"}
        """
        pngName = random_str.generate_random_str()
        img1 = cv2.imread(query, 0)
        img2 = cv2.imread(taste, 0)

        kp1, des1 = self.orb.detectAndCompute(img1, None)
        kp2, des2 = self.orb.detectAndCompute(img2, None)

        bf = cv2.BFMatcher(normType=cv2.NORM_L2, crossCheck=True)
        matches = bf.match(des1, des2)

        matches = sorted(matches, key=lambda x: x.distance)
        img3 = cv2.drawMatches(
            img1=img1,
            keypoints1=kp1,
            img2=img2,
            keypoints2=kp2,
            matches1to2=matches[:1],
            outImg=img2,
            flags=2
        )
        plt.imshow(img3)
        plt.savefig(pngName)
        if matches:
            return {"True": pngName}
        else:
            return {"False": pngName}


if __name__ == '__main__':
    pngName = LogoRec().test_xfeatures2d(
        query="C:\\Users\work\PycharmProjects\\667788\\326746232920852861.png",
        taste="C:\\Users\work\PycharmProjects\\667788\py_lib\\baidu.png"
    )
    print(pngName)