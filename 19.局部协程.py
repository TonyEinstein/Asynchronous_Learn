#!/usr/bin/env python
# -*- coding: utf-8 -*-
# time: 2022/12/8 18:24
# file: 19.局部协程.py
# author: chenruhai
# email: ruhai.chen@qq.com
import asyncio
import time
from concurrent.futures import ProcessPoolExecutor, as_completed,wait
from tqdm import tqdm

def fib(n):
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)

async def cual_data(key, value):
    return key+value

async def fix_main(keys,values):
    tasks = []
    for i in range(len(keys)):
        tasks.append(asyncio.create_task(cual_data(keys[i], values[i])))
    print(f"程序于 {time.strftime('%X')} 开始执行")
    # await asyncio.wait(tasks)
    results = await asyncio.gather(*tasks)
    print(results)
    print(f"程序于 {time.strftime('%X')} 执行结束")
    return results

def main():
    numbers = list(range(10, 35))
    executor = ProcessPoolExecutor(max_workers=8)
    start_time = time.time()
    results = list(tqdm(executor.map(fib, numbers), desc="dict方式", total=len(numbers)))
    print(results)
    print("多进程方式 time is {time}s".format(time=time.time() - start_time))
    results2 = asyncio.run(fix_main(numbers,results))
    print(results2)


if __name__ == '__main__':
    main()
