#!/usr/bin/python 3.10.8

import random

min=1
max=10
target = random.randrange(min,max)
#print(target)

while true:
    keyin = int(input(f'猜數字範圍{min}~{max}'))
    count+=1
    if(keyin == target):
        print(f'猜對了,答案是{target}')
        print(f'你共猜了{count}次')
        break
    else:
        print(f'猜錯了,\n你已經猜了{count}次')
print('Game Over')