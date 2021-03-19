#!/usr/bin/env python
#coding=utf-8

import pytest

@pytest.fixture
def login():
    print("denglu")
    yield


class TestDemo():

    def setup_class(self):
        # 第一步：打开浏览器
        print("打开浏览器")

    def teardown_class(self):
        # 5：关闭浏览器
        print("关闭浏览器")

    def setup(self):
        # 第一步：打开浏览器
        print("fangfa打开浏览器")

    def teardown(self):
        # 5：关闭浏览器
        print("fangfa关闭浏览器")


    def test_a(self,login):
        # 2：输入网址
        # 3：定位
        # 4：各种操作
        # 5：关闭浏览器
        print("testa")

    def test_b(self):
        pass

    def test_c(self):
        pass