import asyncio

async def fn():
    print("one")
    await asyncio.sleep(1)
    # asyncio.create_task(fn2())
    print("four")
    await asyncio.sleep(1)
    print("five")
    await asyncio.sleep(1)

async def fn2():
    print("two")
    await asyncio.sleep(1)
    print("three")

async def fn3():
    print("six")
    await asyncio.sleep(1)
    print("seven")

asyncio.run(fn())