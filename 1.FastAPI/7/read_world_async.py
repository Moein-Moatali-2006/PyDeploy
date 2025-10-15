import time
import random
import asyncio

async def get():
    print("get started")
    r = random.randint(0,10)
    await asyncio.sleep(r)
    print("get ended in", r)

async def extract():
    print("extract started")
    r = random.randint(0,10)
    await asyncio.sleep(r)
    print("extract ended in", r)

async def download():
    print("Download started")
    await get()
    await extract()
    print("Download ended in")

async def printer(): 
    print("printer started")
    r = random.randint(0,10)
    await asyncio.sleep(r)
    print("printer ended in", r)


async def ai_video():
    print("video started")
    r = random.randint(0,10)
    await asyncio.sleep(r)
    print("video ended in", r)

async def ai_audio():
    print("audio started")
    r = random.randint(0,10)
    await asyncio.sleep(r)
    print("audio ended in", r)

async def mix_ai():
    print("mix started")
    r = random.randint(0,10)
    await asyncio.sleep(r)
    print("mix ended in", r)


async def ai():
    print("ai started")
    await asyncio.gather(ai_video(), ai_audio())
    mix_ai()
    print("ai ended in")

async def main():
    await asyncio.gather(download(), printer(), ai())
    print("Main ended")


if __name__ == "__main__":
    start = time.perf_counter()
    asyncio.run(main())
    end = time.perf_counter()
    print(end - start)
