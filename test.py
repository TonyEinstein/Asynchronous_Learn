#!/usr/bin/env python
# -*- coding: utf-8 -*-
# time: 2022/12/2 2:44
# file: test.py
# author: chenruhai
# email: ruhai.chen@qq.com
import sys

import numpy as np

s1 = "{8.3,8.6,8.7,8.5,8.1}"
s2 = "{7.5,7.8,8.7,8.8}"

s1 = s1.replace("{","").replace("}","")
s2 = s2.replace("{","").replace("}","")
s1 = s1.split(",")
s2 = s2.split(",")
s1 = [float(i) for i in s1]
s2 = [float(i) for i in s2]

print(s1,s2)
# s1 = np.array(s1)
# s2 = np.array(s2)
# print(s1)
# print(s2)
# print(np.mean(np.abs(s1-s2)))