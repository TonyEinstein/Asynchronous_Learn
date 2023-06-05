# coding=utf-8
import asyncio
import time


async def say_after(what, delay):
    await asyncio.sleep(delay)
    print(what)

print(f"程序于 {time.strftime('%X')} 开始执行")
loop = asyncio.get_event_loop()
tasks = [asyncio.ensure_future(say_after('hello', i)) for i in range(4)]
loop.run_until_complete(asyncio.wait(tasks))
print(f"程序于 {time.strftime('%X')} 执行结束")
