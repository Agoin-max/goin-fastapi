import asyncio


async def func1():
    print(1)
    await asyncio.sleep(2)
    print(2)


async def func2():
    print(3)
    await asyncio.sleep(2)
    print(4)


tasks = [
    asyncio.ensure_future(func1()),
    asyncio.ensure_future(func2()),
]

# 事件循环
loop = asyncio.get_event_loop()
# 将任务放到任务列表
loop.run_until_complete(asyncio.wait(tasks))

# asyncio.run(func1())  # python3.7 等价于loop与loop.run
