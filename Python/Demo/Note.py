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

# 3.3 组织列表
# 3.3.1 使用方法 sort() 对列表进行永久性排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(cmp=None, key=None, reverse=False);
print cars;
cars.sort(reverse=True);
print cars;

# 3.3.2 使用函数 sorted() 对列表进行临时排序
'''要保留列表元素原来的排列顺序，同时以特定的顺序呈现它们，可使用函数 sorted() 。函数
sorted() 让你能够按特定顺序显示列表元素，同时不影响它们在列表中的原始排列顺序。'''

cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)

print("Here is the original list:")
print(sorted(cars))

# 3.3.3 倒着打印列表
'''要反转列表元素的排列顺序，可使用方法 reverse() 。'''
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)

# 3.3.4 确定列表的长度
# 使用函数 len() 可快速获悉列表的长度。在下面的示例中，列表包含4个元素，因此其长度为4：
cars = ['bmw', 'audi', 'toyota', 'subaru'];
changdu = len(cars);
print changdu;

# 3.4 使用列表时避免索引错误
'''刚开始使用列表时，经常会遇到一种错误。假设你有一个包含三个元素的列表，却要求获取
第四个元素：'''
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles[2])


# 4.1 遍历整个列表
# for 循环
magicians = ['alice', 'david', 'carolina']
for magic in magicians:
    print magic;



# 4.1.2 在 for 循环中执行更多的操作
# 在 for 循环中，可对每个元素执行任何操作
magicians = ['alice', 'david', 'carolina']
for magic in magicians:
    print magic.title() + "is a trick";

# 4.1.3 在 for 循环结束后执行一些操作
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")
print("Thank you, everyone. That was a great magic show!")


# 4.3 创建数值列表
# 列表非常适合用于存储数字集合，而Python提供了很多工具，可帮助你高效地处理数字列表。
# 4.3.1 使用函数 range()
for value in range(1,10):
    print(value);

# 4.3.2 使用 range() 创建数字列表
numbers = list(range(1,15));
print numbers;
# 使用函数 range() 时，还可指定步长。例如，下面的代码打印1~10内的偶数：
numbers = list(range(1,15,2));
print numbers;
# 使用函数 range() 几乎能够创建任何需要的数字集
squares = [];
for square in range(1,10):
    squares.append(square ** 2);
print squares;

# 4.3.3 对数字列表执行简单的统计计算
'''有几个专门用于处理数字列表的Python函数。例如，你可以轻松地找出数字列表的最大值、
最小值和总和：'''
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print min(digits),max(digits),sum(digits);
# 4.3.4 列表解析
'''前面介绍的生成列表 squares 的方式包含三四行代码，而列表解析让你只需编写一行代码就
能生成这样的列表。列表解析将 for 循环和创建新元素的代码合并成一行，并自动附加新元素。
面向初学者的书籍并非都会介绍列表解析，这里之所以介绍列表解析，是因为等你开始阅读他人
编写的代码时，很可能会遇到它们。
下面的示例使用列表解析创建你在前面看到的平方数列表：'''
squares = [value ** 2 for value in range(1,15)];
print squares;

# 4.4 使用列表的一部分    列表的部分元素——Python称之为切片
# 4.4.1 切片
'''要创建切片，可指定要使用的第一个元素和最后一个元素的索引。与函数 range() 一样，Python
在到达你指定的第二个索引前面的元素后停止。要输出列表中的前三个元素，需要指定索引0~3，
这将输出分别为 0 、 1 和 2 的元素。'''
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print players[1:3];
# 遍历切片
# 如果要遍历列表的部分元素，可在 for 循环中使用切片。
players = ['charles', 'martina', 'michael', 'florence', 'eli']
for play in players[:3]:
    print play;

# 4.4.3 复制列表
'''要复制列表，可创建一个包含整个列表的切片，方法是同时省略起始索引和终止索引（ [:] ）。
这让Python创建一个始于第一个元素，终止于最后一个元素的切片，即复制整个列表。'''
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:];
print friend_foods;

# 4.5 元组
'''列表非常适合用于存储在程序运行期间可能变化的数据集。列表是可以修改的，这对处理网
站的用户列表或游戏中的角色列表至关重要。然而，有时候你需要创建一系列不可修改的元素，
元组可以满足这种需求。Python将不能修改的值称为不可变的，而不可变的列表被称为元组。'''
# 4.5.1 定义元组
'''元组看起来犹如列表，但使用圆括号而不是方括号来标识。定义元组后，就可以使用索引来
访问其元素，就像访问列表元素一样。'''
dimensions = (200, 50)
print dimensions[0],dimensions[1];

# 4.5.2 遍历元组中的所有值
# 使用 for 循环来遍历元组中的所有值：
dimensions = (200, 50,100,"apple");
for dimen in dimensions:
    print dimen;

# 4.5.3 修改元组变量
# 虽然不能修改元组的元素，但可以给存储元组的变量赋值。
dimensions = (200, 50,100,"apple");
print dimensions;
dimensions = (666);
print dimensions;


# 5.   if 语句
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print car.upper();
    else :
        print car.lower();
    
# 5.2 条件测试
car = 'Audi'
print car.lower() == 'audi'

# 5.2.3 检查是否不相等
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")
# 5.2.4 比较数字
answer = 17
if answer != 42:
    print("That is not the correct answer. Please try again!")
# 5.2.5 检查多个条件
# 1. 使用 and 检查多个条件
# 2. 使用 or 检查多个条件


# 5.2.6 检查特定值是否包含在列表中
requested_toppings = ['mushrooms', 'onions', 'pineapple']
if 'onions'  in requested_toppings:
    print "ok";

# 5.2.7 检查特定值是否不包含在列表中
requested_toppings = ['mushrooms', 'onions', 'pineapple']
if 'onions' not in requested_toppings:
    print "ok";

# 5.2.8 布尔表达式
boole = True;
print boole;

# 5.3  if 语句
# 5.3.1 简单的 if 语句
age = 19;
if age >= 18:
    print str(age) + " year";
# 5.3.2  if-else 语句
age = 19;
if age >20:
    print str(age) + " year";
else:
    print "hello python";
# 5.3.3  if-elif-else 结构
age = 19;
if age > 20:
    print "one";
elif age > 18:
    print "two";
elif age > 25:
    print "three";
else:
    print "four";  



# 5.4 使用 if 语句处理列表
# 5.4.1 检查特殊元素
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
            print("Adding " + requested_topping + ".")
print("\nFinished making your pizza!")

# 5.4.2 确定列表不是空的
requested_toppings = [];
if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")
# 5.4.3 使用多个列表
available_toppings = ['mushrooms', 'olives', 'green peppers',
'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print "we have " + requested_topping + ".";
    else :
        print "we donot have " + requested_topping + ".";



# 6.               字 典
# 6.1 一个简单的字典  key value 键值对
alien_0 = {'color': 'green', 'points': 5}
print alien_0['color'];
# 6.2 使用字典
# 6.2.1 访问字典中的值
alien_0 = {'color': 'green', 'points': 5}
new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")

# 6.2.2 添加键 — 值对
alien_0 = {'color': 'green', 'points': 5}
alien_0['x'] = 100;
print alien_0;

# 6.2.3 先创建一个空字典
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print alien_0;

# 6.2.4 修改字典中的值
alien_0 = {'color': 'green'}
print("The alien is " + alien_0['color'] + ".")
alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".")

# 6.2.5 删除键 — — 值对
alien_0 = {'color': 'green', 'points': 5}
print alien_0;
del alien_0['color'];
print alien_0;

# 6.2.6 由类似对象组成的字典
'''字典存储的是一个对象（游戏中的一个外星人）的多种信息，但你也可以
使用字典来存储众多对象的同一种信息.'''
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
};
print favorite_languages['jen'];

# 6.3 遍历字典
# 6.3.1 遍历所有的键 — — 值对
user_0 = {
'username': 'efermi',
'first': 'enrico',
'last': 'fermi',
}
for k,v in user_0.items():
    print k + ":" + v
    
# 6.3.2 遍历字典中的所有键
user_0 = {
'username': 'efermi',
'first': 'enrico',
'last': 'fermi',
}
for k in user_0.keys():
    print k;

# 6.3.3 按顺序遍历字典中的所有键
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
for name in sorted(favorite_languages.keys()):
    print name;

# 6.3.4 遍历字典中的所有值
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
for value in favorite_languages.values():
    print value;

# 6.4 嵌套
# 有时候，需要将一系列字典存储在列表中，或将列表作为值存储在字典中，这称为嵌套。
# 你可以在列表中嵌套字典、在字典中嵌套列表甚至在字典中嵌套字典。
# 6.4.1 字典列表
alien_0 = {'sex':'man','points':5}
alien_1 = {'sex':'man','points':5}
alien_2 = {'sex':'man','points':5}
aliens = [alien_0,alien_1,alien_2];
for alien in aliens:
    print alien;

# 6.4.2 在字典中存储列表
# 存储所点比萨的信息
pizza = {
'crust': 'thick',
'toppings': ['mushrooms', 'extra cheese'],
}
for value in pizza.get('toppings'):
    print value;
    
# 6.4.3 在字典中存储字典
users = {
    'alien' :{'length' : 7,
              'weight' : 8
              },
    'helln' : {'length' : 9,
              'weight'  : 10
              }
    }

for userkey,uservalue in users.items():
    fullname = userkey + " length is : " + str(uservalue['length']);
    print fullname;

# 7.1 函数 input() 的工作原理
# message = input("really start :");
# print message;

# 7.1.2 使用 int() 来获取数值输入
# age = input("How old are you? ")
# print age;
# 7.1.4 在 Python 2.7 中获取输入

# 7.2  while 循环简介
# 7.2.1 使用 while 循环
# current_number = 1;
# while current_number <= 5:
#     print current_number;
#     current_number += 1;

# 7.2.2 让用户选择何时退出
# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program. "
# message = "";
# while message != "quit":
#     message = input(prompt);
#     print message;

# 7.2.3 使用标志
# 7.2.4 使用 break 退出循环
# prompt = "\nPlease enter the name of a city you have visited:"
# prompt += "\n(Enter 'quit' when you are finished.) "

# message = "";
# while True:
#      message = input(prompt);
#      if message == 'break':
#          break;
#      else:
#          print 'l love go to ' + message.title();
    
# 7.2.5 在循环中使用 continue
# current_number = 0;
# while current_number <= 10:
#     current_number += 1;
#     if current_number % 2 == 0:
#         continue;
#     print "current_number  is :" + str(current_number);

# 7.2.6 避免无限循环
# 7.3 使用 while 循环来处理列表和字典
# 7.3.1 在列表之间移动元素
'''假设有一个列表，其中包含新注册但还未验证的网站用户；验证这些用户后，如何将他们移
到另一个已验证用户列表中呢？一种办法是使用一个 while 循环，在验证用户的同时将其从未验
证用户列表中提取出来，再将其加入到另一个已验证用户列表中。'''
# 首先，创建一个待验证用户列表
# 和一个用于存储已验证用户的空列表
unconfirmed_users = ['alice', 'brian', 'candace'];
confirmed_users = [];
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user);
for user in confirmed_users:
    print "user is :" + user;

# 7.3.2 删除包含特定值的所有列表元素
pets  = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat'];
while 'cat' in pets:
    pets.remove('cat');
print pets;

# 7.3.3 使用用户输入来填充字典
# 可使用 while 循环提示用户输入任意数量的信息。
# responses = {};
# flag = True;
# while flag:
#     name = input("what's your name");
#     response = input("Which mountain would you like to climb someday? ")
#     responses[name] = response;
#     repeat = input("Would you like to let another person respond? (yes/ no)");
#     if repeat == 'no':
#         break;
# for key,value in responses.items():
#     print key + ":" + value;

# 8.                  函 数
# 8.1 定义函数
def greatHello():
    print 'hello world';
greatHello();

# 8.1.1 向函数传递信息
def great(userName):
        print userName.title() + '  hello world';
great('zhaoyong');

# 8.1.2 实参和形参
# 8.2 传递实参
def describe_pet(animal_type, pet_name):
# 显示宠物的信息
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet('hamster', 'harry')
# 1. 调用函数多次

# 8.2.2 关键字实参
'''关键字实参是传递给函数的名称 — 值对。你直接在实参中将名称和值关联起来了，因此向函
数传递实参时不会混淆（不会得到名为Hamster的harry这样的结果）。关键字实参让你无需考虑函
数调用中的实参顺序，还清楚地指出了函数调用中各个值的用途。'''
def describe_pets(animal_type, pet_name):
# '''显示宠物的信息'''
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pets(animal_type='longfei', pet_name='xiao xiongmao')
# 8.2.3 默认值
'''编写函数时，可给每个形参指定默认值。在调用函数中给形参提供了实参时，Python将使用
指定的实参值；否则，将使用形参的默认值。因此，给形参指定默认值后，可在函数调用中省略
相应的实参。使用默认值可简化函数调用，还可清楚地指出函数的典型用法。'''
def describe(animal_type, pet_name = "xiaogou"):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe("flood");

# 8.2.4 等效的函数调用
'''鉴于可混合使用位置实参、关键字实参和默认值，通常有多种等效的函数调用方式。请看下
面的函数 describe_pets() 的定义，其中给一个形参提供了默认值：'''
def describe_dog(pet_name, animal_type='dog'):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
# 下面对这个函数的所有调用都可行：
# 一条名为Willie的小狗
describe_dog('willie')
describe_dog(pet_name='willie')

# 一只名为Harry的仓鼠
describe_dog('harry', 'hamster')
describe_dog(pet_name='harry', animal_type='hamster')
describe_dog(animal_type='hamster', pet_name='harry')


# 8.3 返回值
# 8.3.1 返回简单值
def get_fullname(first_name,last_name):
    full_name = first_name + last_name ;
    return full_name.title();

print get_fullname("zhangfei","guanyu");

# 8.3.2 让实参变成可选的
'''有时候，需要让实参变成可选的，这样使用函数的人就只需在必要时才提供额外的信息。可
使用默认值来让实参变成可选的。'''
def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
        return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)

# 8.3.3 返回字典
'''函数可返回任何类型的值，包括列表和字典等较复杂的数据结构。例如，下面的函数接受姓
名的组成部分，并返回一个表示人的字典：'''

def get_build_name(first_name,last_name):
    person = {'first' : first_name,'last' : last_name}
    return person;
full_name = get_build_name('BMW','MRZ');
print full_name;


# 8.4 传递列表
# 向函数传递列表很有用，这种列表包含的可能是名字、数字或更复杂的对
# 象（如字典）。将列表传递给函数后，函数就能直接访问其内容。下面使用函数来提高处理列表
# 的效率。

def great_users(users):
    for user in users:
        print "hello " + user;
users = ['liming','zhangsan','lisi'];
great_users(users);

# 8.5 传递任意数量的实参
def make_pizzas(*toppings):
    print toppings;
make_pizzas('shaobing');
make_pizzas('mantou','baozi','zongzi');
# 8.5.1 结合使用位置实参和任意数量实参
def make_pizza(size, *toppings):
    print("\nMaking a " + str(size) +
"-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

































































































































































































































































































