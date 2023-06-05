#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :13.concurrent_多进程_map方式实现.py
# @Time      :2022/11/21 16:30
# @Author    : https://github.com/TonyEinstein

import time
from concurrent.futures import ProcessPoolExecutor, as_completed,wait
from tqdm import tqdm

def fib(n):
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)

if __name__ == '__main__':
    numb = dict()
    for i in range(10,45):
        numb[i] = i
    numbers = list(range(10,45))
    numbers_tu = tuple(range(10,45))
    with ProcessPoolExecutor(max_workers=8) as executor:
        # # map 方式---------------
        # start_time = time.time()
        # results = list(tqdm(executor.map(fib, numbers_tu), desc="tuple方式", total=len(numbers_tu)))
        # print(results)
        # print("tuple方式 time is {time}s".format(time=time.time() - start_time))

        start_time = time.time()
        results2 = list(tqdm(executor.map(fib, numbers),desc="list方式",total=len(numbers)))
        # print(results)
        print("list方式 time is {time}s".format(time=time.time() - start_time))

        # start_time = time.time()
        # results3 = list(tqdm(executor.map(fib, tuple(numb.values())), desc="dict方式",total=len(numb)))
        # print(results)
        # print("dict方式 time is {time}s".format(time=time.time() - start_time))



        # for num, result in zip(numbers, results):
        #     print(f"{num}====>{result}")

        # submit 方式-------------
        # work_dict = {executor.submit(fib, i): i for i in numbers}
        # for future in as_completed(work_dict):
        #     num = work_dict[future]
        #     try:
        #         data = future.result()
        #     except Exception as e:
        #         print(e)
        #     else:
        #         print(f"fib({num} = {data})")
