import asyncio
import time
#พิมพ์เวลาที่ผ่านไปและหยุดการทำงานสั่ง
async def sleep():
    print(f'Time: {time.time() - start:.2f}')
    await asyncio.sleep(1)
#หาผลรวมตัวเลข
async def sum(name, numbers):
    total = 0
    for number in numbers:
        print(f'Task {name}: Computing {total}+{number}')
        await sleep()
        total += number
    print(f'Task {name}: Sum = {total}\n')
#เวลาเริ่มต้นการทำงาน
start = time.time()

loop = asyncio.get_event_loop()
tasks = [
    loop.create_task(sum("A", [1, 2])),
    loop.create_task(sum("B", [1, 2, 3])),
]
loop.run_until_complete(asyncio.wait(tasks))#รันการทำงาน Asyncio Task
loop.close()#ปิด event loop เมื่อเสร็จแล้ว

end = time.time()#สิ้นสุดการทำงาน
print(f'Time {end-start:.2f} sec')#แสดงผลลัพธ์เวลาที่ใช้ในการทำงานทั้งหมด
