#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :2.Threading代码多线程_原始.py
# @Time      :2022/11/16 9:50
# @Author    : https://github.com/TonyEinstein

import threading
import time


def say_after(what, delay):
    print(what)
    time.sleep(delay)
    print(what)


print(f"程序于 {time.strftime('%X')} 开始执行\n")
threads = []

for i in range(1, 6):
    t = threading.Thread(target=say_after, name="线程" + str(i), args=('hello', 3))
    print(t.name + '开始执行。')
    t.start()
    threads.append(t)

for i in threads:
    i.join()
print(f"\n程序于 {time.strftime('%X')} 执行结束")
