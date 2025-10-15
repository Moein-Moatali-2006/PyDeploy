import time
import random
import asyncio

async def marriage(name):
    r = random.randint(0, 10)
    await asyncio.sleep(r)
    print("End",name,r)

async def main():
    await asyncio.gather(marriage("Morad"), marriage("Sina"), marriage("Reza"))

if __name__ == "__main__":
    start_time = time.perf_counter()
    asyncio.run(main())
    end_time = time.perf_counter()

    total_time = end_time - start_time
    print(total_time)