import asyncio
import time
#ใช้งานฟังก์ชัน asyncio เพื่อหยุดการทำงานเป็นเวลาที่กำหนด
async def hello(i):
    print(f"{time.ctime()}hello{i}started")
    await asyncio.sleep(4)
    print(f"{time.ctime()}hello{i}done")
#สร้างรายการของ coroutine (coros) ที่เป็นผลลัพธ์จากการเรียกใช้งานฟังก์ชัน hello
async def main():
    coros = [hello(i)for i in range(10)]
    await asyncio.gather(*coros)

if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())   
    end = time.time()
    print(f'Time:{end-start:.2f}sec')
