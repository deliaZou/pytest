#!/usr/bin/env python
#coding=utf-8
import unittest
import os
import sys
sys.path.append(os.getcwd())
import yaml
from zttest.calc import Calc
import pytest

class Testcalc():

    # @pytest.mark.improtant
    @pytest.mark.parametrize("data1, data2, expect",yaml.safe_load(open('test.yaml')))
    def test_add_1(self,data1, data2, expect):
        self.calc = Calc()
        result = self.calc.add(data1,data2)
        print(result)
        assert expect == result

    @pytest.mark.run(order=1)
    def test_div_1(self):
        self.calc = Calc()
        result = self.calc.div(3, 3)
        print(result)
        assert 1 == result

if __name__ == "__main__":
    pytest.main()