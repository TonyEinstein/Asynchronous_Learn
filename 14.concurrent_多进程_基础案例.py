#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :14.concurrent_多进程_基础案例.py
# @Time      :2022/11/21 16:30
# @Author    : https://github.com/TonyEinstein

import time


def fib(n):
    if n<= 2:
        return 1
    return fib(n-1)+fib(n-2)

if __name__ == '__main__':
    start_time = time.time()
    for num in range(25, 35):
        r = fib(num)
        print("exe result {}".format(r))
    print("last time is {time}s".format(time = time.time()-start_time))
