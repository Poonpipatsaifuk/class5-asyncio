import asyncio
import time 
from concurrent.futures.thread import ThreadPoolExecutor
#พิมพ์เวลาที่ผ่านไปและหยุดการทำงานสั่ง
def sleep():
    print(f'Time: {time.time() - start:.2f}')
    time.sleep(1)
#คำนวณผลรวมของตัวเลขในรายการ
async def sum(name, numbers):
    _executor = ThreadPoolExecutor(2)
    total = 0 
    for number in numbers:
        print(f'Task {name}: Computer {total}+{number}')
        await loop.run_in_executor(_executor, sleep)
        total += number
    print(f'Task {name}:Sum = {total}\n')
#เวลาเริ่มต้นการทำงาน
start =time.time()

loop = asyncio.get_event_loop()#การเรียกของวน loop ของ asyncio 
task = [
        loop.create_task(sum("A", [1,2])),
        loop.create_task(sum("B", [1,2,3])),
]
loop.run_until_complete(asyncio.wait(task))#รันการทำงาน Asyncio Task
loop.close#ปิด event loop เมื่อเสร็จแล้ว

end= time.time()#สร้างตัวแปร end เพื่อเก็บเวลาสิ้นสุดการทำงาน
print(f'Time: {end-start:.2f} sec')
