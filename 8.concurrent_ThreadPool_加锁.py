#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :8.concurrent_ThreadPool_加锁.py
# @Time      :2022/11/19 16:11
# @Author    : https://github.com/TonyEinstein


import time
import threading
from concurrent.futures import ThreadPoolExecutor,as_completed

def get():
    for i in range(3):
        time.sleep(1)
        print(i)


def task(lock):
    lock.acquire()   #获取锁
    get()
    lock.release()   #释放锁



if __name__ == "__main__":
    lock=threading.RLock()
    with ThreadPoolExecutor(max_workers=5) as executor:
        for i in range(5):
            ans = [executor.submit(task, lock)]
