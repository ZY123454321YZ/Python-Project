# -- coding: utf-8 --
'''
Created on 2018年6月12日

@author: zhaoyong
'''
print ("hello  World");

message = "hello world python"
print message
zfc = 'a'
zfc1 = "b"
print zfc,zfc1
#首字母大写
name = "love"
print name.title()
#大写
print name.upper()
#小写
print name.lower()

#合并字符串
first_name = "zhaoyong"
last_name = "fyn"
full_name = first_name + last_name
print full_name
#换行符
print "languaes:\r\tptyon\njava"

#删除空白
f_l = "python "
print f_l.strip()

#浮点数
a = 0.1
b = 0.2 
print a + b

#使用函数 str() 避免类型错误
age = 26
message = "happy " + str(age) + " birthday"
print message

#Python 2 中的整数
a = 3
b = 2.0
c = 3.0
d = 2
print a/b,c/d,a/d


#列表
bicycles = ['car','tracle']
print bicycles

#访问列表元素
print bicycles[0]
print bicycles[-1]
#修改列表元素
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)

# 3.2.2 在列表中添加元素
# 1. 在列表末尾添加元素
motorcycles = ['honda', 'yamaha', 'suzuki']
print motorcycles
motorcycles.append("benchi")
print motorcycles
# 2. 在列表中插入元素
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0,"bmw")
print motorcycles

# 3.2.3 从列表中删除元素
motorcycles = ['honda', 'yamaha', 'suzuki']
# 1. 使用 del 语句删除元素
del motorcycles[0]
print motorcycles

# 2. 使用方法 pop() 删除元素
'''
方法 pop() 可删除列表末尾的元素，并让你能够接着使用它。术语弹出（pop）源自这样的类
比：列表就像一个栈，而删除列表末尾的元素相当于弹出栈顶元素。
'''
motorcycles = ['honda', 'yamaha', 'suzuki']
pop_cycles = motorcycles.pop()
print pop_cycles

# 3. 弹出列表中任何位置处的元素
# 实际上，你可以使用 pop() 来删除列表中任何位置的元素，只需在括号中指定要删除的元素
# 的索引即可。
motorcycles = ['honda', 'yamaha', 'suzuki']
pop_cycles = motorcycles.pop(0)
print pop_cycles

# 4. 根据值删除元素
'''有时候，你不知道要从列表中删除的值所处的位置。如果你只知道要删除的元素的值，可使
用方法 remove() 。'''
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.remove("suzuki")
print motorcycles
