#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :16.协程最新的写法.py
# @Time      :2022/11/23 17:07
# @Author    : https://github.com/TonyEinstein

# coding=utf-8
import asyncio
import time


async def say_after(what, delay):
    await asyncio.sleep(delay)
    print(what)

async def main():
    # create_task封装了事件循环
    tasks = []
    task1 = asyncio.create_task(say_after('hello', 1))
    task2 = asyncio.create_task(say_after('world', 2))
    tasks.append(task1)
    tasks.append(task2)
    print(f"程序于 {time.strftime('%X')} 开始执行")
    await asyncio.wait(tasks)
    print(f"程序于 {time.strftime('%X')} 执行结束")


asyncio.run(main())