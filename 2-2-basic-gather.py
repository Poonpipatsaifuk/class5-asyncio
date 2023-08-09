import asyncio
import time
#ใช้งานฟังก์ชัน asyncio เพื่อหยุดการทำงานเป็นเวลาที่กำหนด
async def hello(i):
    print(f"{time.ctime()} hello {i} started")
    await asyncio.sleep(4)
    print(f"{time.ctime()} hello {i} done")
#รันงาน asynchronous ที่เรียกใช้งานฟังก์ชัน hello() สองรอบและจับเวลาเวลาที่ใช้ในการรันโค้ด.
async def main():
    task1 = asyncio.create_task(hello(1)) # return immediately, the task is created
    #await asyncio.sleep(3)
    task2 = asyncio.create_task(hello(2))
    await asyncio.gather(task1, task2)

if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(f'Time: {end-start:.2f} sec')
