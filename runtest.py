#!/usr/bin/python3
#-*-coding:UTF-8-*-
#!@Author:lumm   
#!@Time:2019/4/1

import unittest
from baidu01 import youdao_seek
from baidu01 import baidu_seek
# import youdao_seek
# import baidu_seek

suite=unittest.TestSuite()
suite.addTest(baidu_seek.BaiduTest('test_baidu'))
suite.addTest(youdao_seek.YoudaoTest('test_youdao'))

if __name__ == '__main__':
    runner=unittest.TextTestRunner()
    runner.run(suite)

