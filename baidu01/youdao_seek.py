#!/usr/bin/python3
#-*-coding:UTF-8-*-
#!@Author:lumm   
#!@Time:2019/4/1

from selenium import webdriver
import unittest,time

class YoudaoTest(unittest.TestCase):#继承unittest.testCase各种断言方法

    def setUp(self):
        self.driver=webdriver.Chrome(r"E:\WorkSpace\python\PycharmProjects\JenkinsGUI\testbaidu01\chromedriver.exe")
        self.driver.implicitly_wait(30) #隐性等待30s
        self.base_url='https://www.hao123.com'
        print('测试开始')

    def test_youdao(self):
        driver=self.driver
        driver.get(self.base_url+'/')
        # driver.find_element_by_id('translateContent').clear()  有道
        # driver.find_element_by_id('translateContent').send_keys('unittest')
        # driver.find_element_by_id('translateContent').submit()

        driver.find_element_by_css_selector('.textInput.input-hook').clear()
        driver.find_element_by_css_selector('.textInput.input-hook').send_keys('unittest')
        driver.find_element_by_css_selector('.textInput.input-hook').submit()
        time.sleep(3)
        title=driver.title
        #self.assertIn("unittest",title)
        self.assertEqual(title, u"hao123_上网从这里开始")

    def tearDown(self):
        self.driver.quit()
        print('测试完成')

if __name__ == '__main__':
    unittest.main()