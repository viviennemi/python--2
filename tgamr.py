#!/usr/bin/python 3.10.8

import random

def playGame():
    min=1
    max=10
    count = 0  #記得要加上變數不然無法在執行迴圈時，程式找不到變數無法執行

    target = random.randrange(min,max)
    print('**猜數字**')

    while True:
        keyin = int(input(f'猜數字範圍{min}~{max}:  '))
        count += 1
        if(keyin == target):
            print(f'猜對了答案是{target}\n你已經猜了{count}次')
            break
        elif keyin <target:
            print('再大一點')
            min = keyin +1
        elif keyin >target:
            print('再小一點')
            max = keyin-1
        print(f'你已經猜了{count}次')
  

while(True):
    playGame()
    play_again = input('還要繼續嗎?')
    if not (play_again == 'y'):
        break
print('Game Over')