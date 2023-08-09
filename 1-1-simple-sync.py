#1-1-simple-sync.py
import time 

def sleep():
    print(f'time:{time.time() - start:.2f}')
    time.sleep(1)

#คำนวณผลรวมของตัวเลขในรายการ
def sum(name, numbers):
    total = 0
    for number in numbers:
        print(f'Task{name}: Computing {total}+{number}')
        sleep()
        total += number
    #import module ใน Python เพื่อใช้ในการจับเวลา
    print(f'Task {name}: Sum = {total}\n')

start = time.time()
#คำนวณผลรวมของรายการตัวเลข
task = [
        sum("A",[1,2]),
        sum("b",[1,2,3]),
]
end = time.time()
print(f'Time: {end-start:.2} sec')
