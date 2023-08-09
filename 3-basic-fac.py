#นำเข้าโมดูลที่จำเป็น asyncio
import asyncio
import time
#คำนวณค่าแฟกทอเรียลของจำนวนเต็มบวก n โดยใช้กำหนดการรอให้เวลาผ่านไปในแต่ละการวนลูป.
async def factorial(n):
    f = 1
    for i in range(2, n + 1):
        print(f"Computing factorial({n}), currently i={i}...")
        await asyncio.sleep(1)
        f *= i
    return f
#สร้างและรันงาน asynchronous สำหรับการคำนวณแฟกทอเรียลของตัวเลข 2, 3, และ 4 แสดงผลลัพธ์ที่ได้.
async def main():
    L = await asyncio.gather(factorial(2),  factorial(3), factorial(4))
    print(L)    # [2, 6, 24]

if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(f'Time: {end-start:.2f} sec')
