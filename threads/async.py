import asyncio

async def hello():
    print('Hello World!')
    await asyncio.sleep(5)
    print('Goodbye World!')

async def func1():
    print("func1")
    await asyncio.sleep(5)
    print("func1 done")

async def main():
    l = await asyncio.gather(hello(), func1())

asyncio.run(main())