import asyncio
import time
#พิมพ์เวลาที่ผ่านไปและหยุดการทำงานสั่ง
async def sleep():
    print(f'Time: {time.time() - start:.2f}')#แสดงเวลาตั้งแต่เวลาเริ่มต้นโปรแกรม
    await asyncio.sleep(1)
#คำนวณผลรวมของตัวเลขในรายการ
async def sum(name, numbers):
    total = 0
    for number in numbers:
        print(f'Task {name}: Computing {total}+{number}')
        await sleep()
        total += number
    print(f'Task {name}: Sum = {total}\n')

async def main():
    await asyncio.gather(sum("A", [1, 2]), sum("B", [1, 2, 3]))

if __name__ == "__main__":
    start = time.time()#สร้างตัวแปร start เพื่อเก็บเวลาเริ่มต้นการทำงาน
    asyncio.run(main())#เรียกใช้งานฟังก์ชัน main ในการทำงาน asynchronous
    end = time.time()#สร้างตัวแปร end เพื่อเก็บเวลาสิ้นสุดการทำงาน
    print(f'Time: {end-start:.2f} sec')#แสดงผลลัพธ์เวลาที่ใช้ในการทำงานทั้งหมด
