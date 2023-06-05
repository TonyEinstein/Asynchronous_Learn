#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :4.concurrent_ThreadPool_as_completed方式实现.py
# @Time      :2022/11/16 10:01
# @Author    : https://github.com/TonyEinstein


from concurrent.futures import ThreadPoolExecutor, as_completed
import time

def do_something(seconds):
    print (f'休眠{seconds}秒')
    time.sleep(seconds)
    return '休眠完毕'

start_time = time.perf_counter()
# 将ThreadPoolExecutor()赋值给一个叫做executor的变量。ThreadPoolExecutor(max_workers=5)可控制线程数量
executor=ThreadPoolExecutor()

# 用list comprehension的方式创建一个列表，让do_something()这个函数并发运行10次。
results = [executor.submit(do_something, 1) for i in range(10)]

"""
在concurrent.futures中，as_completed(fs)函数的作用是针对给定的 future 迭代器 fs，在其完成后，返回完成后的迭代器（类型仍然为future)。
这里的fs即为我们创建的列表results。
因为concurrent.futures.as_completed(results)返回的值是迭代器，
因此我们可以使用for循环来遍历它，然后对其中的元素（均为future类型）调用前面讲到的result()函数并打印
"""
for f in as_completed(results):
    print (f.result())

# 获取结束时间，并计算花费的时间
end_time = time.perf_counter()-start_time

print (f'总共耗时{round(end_time,2)}秒')
