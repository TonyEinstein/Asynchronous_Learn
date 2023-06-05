#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :3.concurrent_ThreadPool_submit方式实现.py
# @Time      :2022/11/16 9:45
# @Author    : https://github.com/TonyEinstein

# 使用from concurrent.futures import ThreadPoolExecutor来调用concurrent.futures的线程池处理器对象
from concurrent.futures import ThreadPoolExecutor, wait
import time

"""
在concurent.futures中，ThreadPoolExecutor是Executor下面的两个子类之一（另一个是ProcessPoolExecutor），它使用线程池来执行异步调用.
"""


def do_something(seconds):
    print (f'休眠{seconds}秒')
    time.sleep(seconds)
    return '休眠完毕'

start_time = time.perf_counter()

# 将ThreadPoolExecutor()赋值给一个叫做executor的变量。
executor = ThreadPoolExecutor()

"""
使用ThreadPoolExecutor下面的submit()函数来创建线程，submit()函数中包含了要调用的任务，即do_something()，
以及该函数要调用的参数（也就是dosmeting()里面的seconds)，这里我们放1，表示休眠一秒钟，所以写成submit(do_something, 1)，
因为submit()函数返回的值为future类型的对象，所以这里我们把future简写为f, 分别赋值给f1和f2两个变量，表示并发执行两次do_something()函数。

"""
f1 = executor.submit(do_something, 1)
# wait(f1)
f2 = executor.submit(do_something, 1)


"""
result()的作用是告知你任务走到了哪一步，是否有异常，如果任务没有异常正常完成的话，
那么result()会返回自定义函数下面return的内容（也就是我们do_someting()最下面的return'休眠完毕'），
如果任务执行过程中遇到异常 ，那么result()则会返回异常的具体内容。
"""
print (f1.result())
print (f2.result())
"""
 done()则返回一个布尔值，来告诉你任务是否完成，如果完成，则返回True，反之则返回False。
"""
print (f'task1是否完成: {f1.done()}')
print (f'task2是否完成: {f2.done()}')

# 获取结束时间，并计算花费的时间
end_time = time.perf_counter()-start_time

print (f'总共耗时{round(end_time,2)}秒')



"""
这一段代码缺乏灵活性，因为我们是通过手动的方式创建了f1和f2两个线程，
如果我们要并发运行do_something()这个任务100次，显然我们不可能去手动创建f1, f2, f3......f100这100个变量。
"""












