#!/usr/bin/python 3.10.8

import random

min=1
max=10
count = 0  #記得要加上變數不然無法在執行迴圈時，程式找不到變數無法執行
target = random.randrange(min,max)
print('**猜數字**')

while True:
    keyin = int(input(f'猜數字範圍{min}~{max}:  '))
    count += 1
    if(keyin == target):
        print(f'猜對了答案是{target}\n你共猜了{count}次')
        break
    elif keyin <target:
        print(f'再大一點\n你已經猜了{count}次')
        min = keyin +1
    elif keyin >target:
        print(f'再小一點\n你已經猜了{count}次')
        max = keyin-1
    #print(f'猜錯了\n你已經猜了{count}次')
print('Game Over')