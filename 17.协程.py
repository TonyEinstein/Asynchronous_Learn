import asyncio
import time


async def hello1(a, b):
    print("Hello world 01 begin")
    await asyncio.sleep(3)  # 模拟耗时任务3秒
    print("Hello again 01 end")
    return a + b


def callback(future):  # 定义的回调函数
    print(future.result())
    return future.result()

async def main():
    tasks = []
    task1 = asyncio.create_task(hello1(10,5))
    task2 = asyncio.create_task(hello1(20,5))
    task1.add_done_callback(callback)
    task2.add_done_callback(callback)
    tasks.append(task1)
    tasks.append(task2)
    done, pending = await asyncio.wait(tasks)
    print("---------------------")
    for task in done:
        print(f"执行结果: {task.result()}")
    print(pending)

asyncio.run(main())

'''运行结果为：
Hello world 01 begin
Hello again 01 end
15
'''