# -- coding: utf-8 --
'''
Created on 20140316

@author: zhaoyong
'''
score = int(input("请输入一个分数:"))
if 100 >= score >=90 :
    print("A")
elif 90 >= score >= 80:
    print("B")
elif 80 >= score >= 70:
    print("C")
elif 70 >= score >= 60:
    print("D")
else :
    print("你学习能力太差啦，不及格")

'''
for 目标 in 表达式:
        循环体
在这里，目标指的的每次迭代的变量的值，表达式一般是序列（字符串，列表，元组等）
'''
favourite = "FishWater"
for i in favourite:
    print i   
member = ['小甲鱼','西红柿','小布丁ma']
for each in member:
    print(each + ":" + str(len(each)))
    
    