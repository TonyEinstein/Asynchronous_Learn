#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :1.同步.py
# @Time      :2022/11/16 9:49
# @Author    : https://github.com/TonyEinstein


import time

def do_something():
    print ('休眠1秒')
    time.sleep(1)

start_time = time.perf_counter()
do_something()
do_something()
end_time = time.perf_counter()-start_time

print (f'总共耗时{round(end_time, 2)}秒')
