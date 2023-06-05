import asyncio
import time


async def hello1(a, b):
    print("Hello world 01 begin")
    await asyncio.sleep(3)  # 模拟耗时任务3秒
    print("Hello again 01 end")
    return a + b


async def hello2(a, b):
    print("Hello world 02 begin")
    await asyncio.sleep(2)  # 模拟耗时任务2秒
    print("Hello again 02 end")
    return a - b


async def hello3(a, b):
    print("Hello world 03 begin")
    await asyncio.sleep(4)  # 模拟耗时任务4秒
    print("Hello again 03 end")
    return a * b


async def main():
    results = await asyncio.gather(hello1(10, 5), hello2(10, 5), hello3(10, 5))
    for result in results:
        print(result)


if __name__ == '__main__':
    asyncio.run(main())
    pass

'''运行结果为：
Hello world 01 begin
Hello world 02 begin
Hello world 03 begin
Hello again 02 end
Hello again 01 end
Hello again 03 end
15
5
50
'''