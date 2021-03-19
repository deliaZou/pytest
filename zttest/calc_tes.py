#!/usr/bin/env python
#coding=utf-8
import sys
import os
sys.append(os.getcwd())
import unittest
from zttest.calc import Calc



class TestCal(unittest.TestCase):

    def test_add_1(self):
        self.calc = Calc()
        result = self.calc.add(1,3)
        print(result)
        self.assertEqual(4, result)