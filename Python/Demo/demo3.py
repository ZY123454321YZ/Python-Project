# -*- coding: UTF-8 -*-
'''
Created on 20140301

@author: zhaoyong
'''
import random


times = 3
select = random.randint(1,10)
print("选择的",select)
guess = 0
print("---------------开始游戏了----------")
while (guess != select) and (times > 0) :
    print("请输入数字：")
    temp = input()
    guess = int(temp)
    times = times - 1
    if guess == select :
        print("你真棒答对了")
        print("可惜猜对了也没有奖励哦!")
    elif guess > select :
        print('猜大了重新猜吧')
    elif guess < select :
        print('猜小了重新猜吧')
    if times > 0:
        print("再重新猜一次吧！")
    else :
        print('游戏结束了！')
print('下次再接再厉吧！')
    
print(type(12.0))
print(type(False))
print(type(10))
print(type("100"))
    
    
    
    
