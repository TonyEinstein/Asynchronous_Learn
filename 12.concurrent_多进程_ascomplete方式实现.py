#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :12.concurrent_多进程_ascomplete方式实现.py
# @Time      :2022/11/21 16:29
# @Author    : https://github.com/TonyEinstein

import time
from concurrent.futures import ProcessPoolExecutor, as_completed

def fib(n):
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)

if __name__ == '__main__':
    start_time = time.time()
    numbers = range(20,35)
    with ProcessPoolExecutor(max_workers=3) as executor:
        # # map 方式---------------
        # results = executor.map(fib, numbers)
        # for num, result in zip(numbers, results):
        #     print(f"{num}====>{result}")

        # submit 方式-------------
        work_dict = {executor.submit(fib, i): i for i in numbers}
        for future in as_completed(work_dict):
            num = work_dict[future]
            try:
                data = future.result()
            except Exception as e:
                print(e)
            else:
                print(f"fib({num} = {data})")
    print("last time is {time}s".format(time=time.time() - start_time))