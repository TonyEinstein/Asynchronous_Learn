#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :5.concurrent_ThreadPool_map函数方式实现.py
# @Time      :2022/11/16 10:05
# @Author    : https://github.com/TonyEinstein

from concurrent.futures import ThreadPoolExecutor
import time

def do_something(seconds):
    print (f'休眠{seconds}秒')
    time.sleep(seconds)
    return '休眠完毕'

start_time = time.perf_counter()
# ThreadPoolExecutor(max_workers=5)可控制线程数量
executor=ThreadPoolExecutor(max_workers=100)

"""
定义了sec = [5,4,3,2,1]这个列表，该列表作为map()函数的第二个参数被传入（executor.map(do_something, sec)），
因为该列表总共有5个元素，因此这里创建并且并发了5个线程来分5次执行do_something(seconds)，第一次列表中的元素5作为参数被传入do_something(seconds), 
也就是第一个线程执行后将休眠5秒，第二次列表中的元素4作为参数被传入do_something(seconds), 也就是第二个线程执行后将休眠4秒，以此类推。
"""
sec = [5,4,3,2,1]
# sec = [8,5,4,3,2,1]
# sec = [2,2,2,2,2,1]
results = executor.map(do_something, sec)
#因为5次任务是并发执行的，所以程序消耗了5秒，4秒，3秒，2秒，1秒中的最大值，总共耗时5.01秒完成。
for result in results:
 print (result)

# 获取结束时间，并计算花费的时间
end_time = time.perf_counter()-start_time

print (f'总共耗时{round(end_time,2)}秒')

"""
除了通过list comprehension来指定N次并发运行do_something(seconds)外，还可以通过concurrent.futures.ThreadPoolExecutor()下面的map()函数来达到目的，
map()函数和submit()函数的用法类似，都可以用来创建线程，然后并发执行任务并返回future对象，但是它比submit()函数更灵活。
区别是：map()函数传入的第二个参数为一个可遍历的对象，这个可遍历的对象里的元素可以用来作为函数的参数。
"""