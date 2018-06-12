# -- coding: utf-8 --
# from test import make_pizza
from test import make_pizza as mp
import test as p
'''
Created on 20140610

@author: zhaoyong
'''

message = "hello python"
print(message)
message = "guseess"
print message
test = "demo" + message
print(test)
print(test.title())
print(test.upper())
test = "message's is oneday"
print(test)
# test = 'message's is oneday'
# print(test)
k = 3**4 + 5
j = .1+.2
m = 2 * .2
print k ,j , m
age = 23
message = "happy" +str(age) + ": MRs"
print message
m = 3/2 
j = 3.0/2
print m,j

bicyles = ['bmw','benchi','qq']
del bicyles[1]
bicyles.append("huahua")
bicyles.insert(2, 5)
print bicyles
shanchu = bicyles.pop()
duoshao = bicyles.pop(1)
print bicyles
print shanchu
print duoshao



cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(cmp=None, key=None, reverse=False)
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(sorted(cars))
print(cars)



cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)
print(len(cars))



magicians = ['alice', 'david', 'carolina']
for magician in magicians :
    print magician



# 
# for value in range(5):
#     print(value)



numbers = list(range(1,6))
print numbers



squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)
    
print squares

digts = [1,2,3,4,5,100,2**50]

print max(digts)
print min(digts)
print sum(digts)



squares = [value ** 2 for value in range(1,11)]
print squares

##----------------------切片
players = ['nanjing','beijing','changsha','huaian','tianjing','shandong']
print(players[0:3])
print(players[:3])
print(players[1:])
print(players[2:5])

for value in players[:3]:
    print value



#复制列表
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print my_foods
print friend_foods
friend_foods = my_foods[:2]
print friend_foods



##--------------------------  元组
'''
列表非常适合用于存储在程序运行期间可能变化的数据集。列表是可以修改的，这对处理网
站的用户列表或游戏中的角色列表至关重要。然而，有时候你需要创建一系列不可修改的元素，
元组可以满足这种需求。Python将不能修改的值称为不可变的，而不可变的列表被称为元组。
'''

#定义元组
'''
元组看起来犹如列表，但使用圆括号而不是方括号来标识。定义元组后，就可以使用索引来
访问其元素，就像访问列表元素一样。
'''
dimensions = (200, 50)
print dimensions[0]
print dimensions[1]
#不可修改
# dimensions[0] = 250

#遍历元祖
for value in dimensions:
    print value

#修改元组变量
#虽然不能修改元组的元素，但可以给存储元组的变量赋值。
dimensions = (200, 50)
for value in dimensions:
    print value
dimensions = (400,100)
for value in dimensions:
    print value
#相比于列表，元组是更简单的数据结构。如果需要存储的一组值在程序的整个生命周期内都
# 不变，可使用元组。

##-----------------------  if 语句
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars :
    if car == 'bmw':
        print car.upper()
    else :
        print car.title()
        
#检查是否相等时不考虑大小写
#在Python中检查是否相等时区分大小写，例如，两个大小写不同的值会被视为不相等
car = 'Audi'
print car == 'audi'

#检查是否不相等
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")
    
#比较数字
age = 18
print age == 18

answer = 17
if answer != 42:
    print("That is not the correct answer. Please try again!")
# 检查多个条件
'''
可能想同时检查多个条件，例如，有时候你需要在两个条件都为 True 时才执行相应的操作，
而有时候你只要求一个条件为 True 时就执行相应的操作。在这些情况下，使用关键字 and 和 or
'''
age = 18
age1 = 22
print (age >= 18) and (age1 <=21)

#使用 or 检查多个条件
'''
关键字 or 也能够让你检查多个条件，但只要至少有一个条件满足，就能通过整个测试。仅当
两个测试都没有通过时，使用 or 的表达式才为 False
'''
age = 18
age1 = 22
print (age >= 18) or (age1 <=21)

#检查特定值是否包含在列表中
#要判断特定的值是否已包含在列表中，可使用关键字 in 
requested_toppings = ['mushrooms', 'onions', 'pineapple']
print 'mushrooms' in requested_toppings
#检查特定值是否不包含在列表中
'''还有些时候，确定特定的值未包含在列表中很重要；在这种情况下，可使用关键字 not in '''
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print user.title()
#if-else 语句
age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")   
    
    
# if-elif-else 结构
age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10.")
    
#省略 else 代码块
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:
    price = 5
print("Your admission cost is $" + str(price) + ".")

#测试多个条件
'''
if-elif-else 结构功能强大，但仅适合用于只有一个条件满足的情况：遇到通过了的测试后，
Python就跳过余下的测试。这种行为很好，效率很高，让你能够测试一个特定的条件。
然而，有时候必须检查你关心的所有条件。在这种情况下，应使用一系列不包含 elif 和 else
代码块的简单 if 语句。在可能有多个条件为 True ，且你需要在每个条件为 True 时都采取相应措施
时，适合使用这种方法。
'''
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
    print("\nFinished making your pizza!")

# 使用 if 语句处理列表
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings :
    if requested_topping == 'green peppers' :
        print("Sorry, we are out of green peppers right now.")
    else:
        print("Adding " + requested_topping + ".")
print("\nFinished making your pizza!")




##-----------------------------字 典
'''
在Python中，字典是一系列键 — 值对。每个键都与一个值相关联，你可以使用键来访问与之
相关联的值。与键相关联的值可以是数字、字符串、列表乃至字典。事实上，可将任何Python对
象用作字典中的值。
在Python中，字典用放在花括号 {} 中的一系列键 — 值对表示:
'''
alien_0 = {'color': 'green', 'points': 5}

#访问字典中的值
print alien_0['color']
#添加键 — 值对
alien_0['x'] = 'y'
print alien_0


#先创建一个空字典
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

#修改字典中的值
#要修改字典中的值，可依次指定字典名、用方括号括起的键以及与该键相关联的新值。
alien_0 = {'color': 'green'}
print("The alien is " + alien_0['color'] + ".")
alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".")

# 删除键 — — 值对
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']
print alien_0

#由类似对象组成的字典
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}

print("Sarah's favorite language is " +
favorite_languages['sarah'].title() +
".")



#遍历字典
# 遍历所有的键 — — 值对
user_0 = {
'username': 'efermi',
'first': 'enrico',
'last': 'fermi',
}

for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)

#遍历字典中的所有键
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
for name in favorite_languages.keys():
    print(name.title())
    
#按顺序遍历字典中的所有键
'''
字典总是明确地记录键和值之间的关联关系，但获取字典的元素时，获取顺序是不可预测的。
这不是问题，因为通常你想要的只是获取与键相关联的正确的值。
要以特定的顺序返回元素，一种办法是在 for 循环中对返回的键进行排序。为此，可使用函
数 sorted() 来获得按特定顺序排列的键列表的副本：
'''
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")


#遍历字典中的所有值
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())


#嵌套
'''
有时候，需要将一系列字典存储在列表中，或将列表作为值存储在字典中，这称为嵌套。你
可以在列表中嵌套字典、在字典中嵌套列表甚至在字典中嵌套字典。
'''
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)
    
aliens = []
for alien in range(30):
    newalien = {'mouse' : 'green','touch' :'blue'}
    aliens.append(newalien)
    
print len(aliens)
for alien in aliens[:5]:
    print alien
    
# 在字典中存储列表
# 存储所点比萨的信息
pizza = {
'crust': 'thick',
'toppings': ['mushrooms', 'extra cheese'],
}
# 概述所点的比萨
print("You ordered a " + pizza['crust'] + "-crust pizza " +
"with the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)


# 在字典中存储字典
users = {
'aeinstein': {
'first': 'albert',
'last': 'einstein',
'location': 'princeton',
},
'mcurie': {
'first': 'marie',
'last': 'curie',
'location': 'paris',
},
}
for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())


#------------------------用户输入和 while 循环
#函数 input() 的工作原理
'''
函数 input() 让程序暂停运行，等待用户输入一些文本。获取用户输入后，Python将其存储在
一个变量中，以方便你使用。
'''
# message = input("Tell me something, and I will repeat it back to you: ")
# something = input("tell me something ,and i will repeat it back to you :")
# print(something)
# name = raw_input("Please enter your name: ")
# print("Hello, " + name + "!")
# 
# 
# prompt = "If you tell us who you are, we can personalize the messages you see."
# prompt += "\nWhat is your first name? "
# name = raw_input(prompt)
# print("\nHello, " + name + "!")


# height = input("How tall are you, in inches? ")
# height = int(height)
# if height >= 36:
#     print("\nYou're tall enough to ride!")
# else:
#     print("\nYou'll be able to ride when you're a little older.")
    
#求模运算符
print 4%3   
print 7%4

# number = input("Enter a number, and I'll tell you if it's even or odd: ")
# number = int(number)
# if number % 2 == 0:
#     print("\nThe number " + str(number) + " is even.")
# else:
#     print("\nThe number " + str(number) + " is odd.")
    
    
#在 Python 2.7 中获取输入
#  while 循环简介
'''
for 循环用于针对集合中的每个元素都一个代码块，而 while 循环不断地运行，直到指定的条
件不满足为止。'''
# current_number = 0
# while current_number <= 5 :
#     print current_number
#     current_number += 1
# 
# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program. "
# message = ""
# while message != 'quit':
#     message = raw_input(prompt)
#     print(message)
    
    
#使用标志
# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program. "
# active = True
# while active:
#     message = raw_input(prompt)
#     if message == 'quit':
#         active = False
#     else:
#         print(message)
        
# 使用 break 退出循环
# prompt = "\nPlease enter the name of a city you have visited:"
# prompt += "\n(Enter 'quit' when you are finished.) "
# while True:
#     city = raw_input(prompt)
#     if city == 'quit':
#         break
#     else:
#         print("I'd love to go to " + city.title() + "!")
        
# 在循环中使用 continue
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)

#使用 while 循环来处理列表和字典
unconfirmedusers = ['alian','python','java','go','c++']
confirmedusers = []
while unconfirmedusers:
    user = unconfirmedusers.pop()
    confirmedusers.append(user)
for valueuser in confirmedusers:
    print ("user is " + valueuser)
    
# 删除包含特定值的所有列表元素
pets  = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)


# 使用用户输入来填充字典
# response = {}
# while True :
#     name = raw_input("what your name is :")
#     response['name'] = name
#     age = raw_input("what your age is :")
#     response['age'] = int(age)
#     quitmessage = raw_input("if you break, enter quit")
#     if quitmessage == 'quit' :
#         break
# for key,value in response.items() :
#     print key,value




#----------------------------------------------函 数
# 定义函数
'''显示简单的问候语'''
def greet_user():
    print("Hello!")
    
print greet_user()

def greet_use(username):
    print("Hello!" + username +"everyday !")
print greet_use("zhaoyong")
    
    
# 实参和形参
#传递实参
def describe_pet(animal_type, pet_name):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet('hamster', 'harry')


# 关键字实参
# 关键字实参是传递给函数的名称 — 值对。
def describe_pe(animal_type, pet_name):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet(animal_type='hamster', pet_name='harry')

# 默认值
'''
编写函数时，可给每个形参指定默认值。在调用函数中给形参提供了实参时，Python将使用
指定的实参值；否则，将使用形参的默认值。因此，给形参指定默认值后，可在函数调用中省略
相应的实参。使用默认值可简化函数调用，还可清楚地指出函数的典型用法。
'''
def describe(pet_name, animal_type='dog'):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe(pet_name='willie')

# 返回值  :函数并非总是直接显示输出，相反，它可以处理一些数据，并返回一个或一组值。
# 返回简单值
def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print musician



def formatted_name(first_name, middle_name, last_name):
    full_name = first_name + ' ' + middle_name + ' ' + last_name
    return full_name.title()
musician = formatted_name('john', 'lee', 'hooker')
print(musician)


# 返回字典  函数可返回任何类型的值，包括列表和字典等较复杂的数据结构。
def build_person(first_name, last_name):
    person = {'first': first_name, 'last': last_name}
    return person
musician = build_person('jimi', 'hendrix')
print(musician)
  
  
# 结合使用函数和 while 循环   """返回整洁的姓名"""
def get_formatted_name_(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()
 # 这是一个无限循环!
# while True:
#     print("\nPlease tell me your name:")
#     f_name = raw_input("First name: ")
#     l_name = raw_input("Last name: ")
# formatted_name = get_formatted_name_(f_name, l_name)
# print("\nHello, " + formatted_name + "!")   
    
# 传递列表
def greet_users(names):
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)
usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

# 在函数中修改列表
def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
# 模拟根据设计制作3D打印模型的过程
        print("Printing model: " + current_design)
        completed_models.append(current_design)
def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

#禁止函数修改列表
'''
为解决这个问题，可向函数传
递列表的副本而不是原件；这样函数所做的任何修改都只影响副本，而丝毫不影响原件。
要将列表的副本传递给函数
'''
# 传递任意数量的实参
'''
有时候，你预先不知道函数需要接受多少个实参，好在Python允许函数从调用语句中收集任
意数量的实参。'''
def make_pizza(*toppings):
    """打印顾客点的所有配料"""
    print(toppings)
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')


#结合使用位置实参和任意数量实参
# 如果要让函数接受不同类型的实参，必须在函数定义中将接纳任意数量实参的形参放在最
# 后。Python先匹配位置实参和关键字实参，再将余下的实参都收集到最后一个形参中。
# def pizza(size, *toppings):
#     """概述要制作的比萨"""
#     print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
#     for topping in toppings:
#         print("- " + topping)
# pizza(16, 'pepperoni')
# pizza(12, 'mushrooms', 'green peppers', 'extra cheese')



# 将函数存储在模块中
'''
函数的优点之一是，使用它们可将代码块与主程序分离。通过给函数指定描述性名称，可让
主程序容易理解得多。你还可以更进一步，将函数存储在被称为模块的独立文件中，再将模块导
入到主程序中。 import 语句允许在当前运行的程序文件中使用模块中的代码。
'''
# 导入整个模块          要让函数是可导入的，得先创建模块。模块是扩展名为.py的文件，包含要导入到程序中的代码。
# make_pizza(10,'person','tiger','dog')



#使用 as 给函数指定别名
# 列如 from pizza import make_pizza as mp
# map(10,'person','tiger','dog')



#使用 as 给模块指定别名
p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

#------------------------------------------------创建和使用类
#根据类创建实例
class Dog(object):
    def __init__(self,name,age):  
        self.name=name
        self.age=age  
    def sit(self):
        print(self.name.title()+" is now sitting")
        
my_dog = Dog('while',6)
print my_dog.name
print my_dog.age
my_dog.sit()

#创建多个实例
your_dog = Dog("black",12)
your_dog.sit()

# 使用类和实例
# class Car(object):
#     def __init__(self,make,model,year):
#         self.make = make
#         self.model = model
#         self.year = year
#     def get_descriptive_name(self):
#         print self.make + " " + self.model + " " + str(self.year)
#         
# my_car = Car("beijing","1947",1988)
# my_car.get_descriptive_name()


# 给属性指定默认值
class Car(object):
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
         print self.make + " " + self.model + " " + str(self.year)
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    def update_odometer(self, mileage):
        self.odometer_reading = mileage
    def fill_gas_tank(self):
        print("This car doesn't need a gas tank!")
my_new_car = Car('audi', 'a4', 2016)
# print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()


# 修改属性的值
my_new_car = Car('audi', 'a4', 2016)
my_new_car.odometer_reading = 100
my_new_car.read_odometer()

#  通过方法修改属性的值
my_new_car.update_odometer(200)
my_new_car.read_odometer()


#####-------------继承
'''编写类时，并非总是要从空白开始。如果你要编写的类是另一个现成类的特殊版本，可使用
继承。一个类继承另一个类时，它将自动获得另一个类的所有属性和方法；原有的类称为父类，
而新类称为子类。子类继承了其父类的所有属性和方法，同时还可以定义自己的属性和方法。'''
# class ElectricCar(Car):
#     def __init__(self, make, model, year):
#         super(ElectricCar,self).__init__(make, model, year)
# my_tesla = ElectricCar('tesla', 'model s', 2016)
# print(my_tesla.get_descriptive_name())


# 给子类定义属性和方法
# class ElectricCar(Car):
#     def __init__(self, make, model, year):
#         super(ElectricCar,self).__init__(make, model, year)
#         self.battery_size = 70
#     def describe_battery(self):
#         print("This car has a " + str(self.battery_size) + "-kWh battery.")
# my_tesla = ElectricCar('tesla', 'model s', 2016)
# print(my_tesla.get_descriptive_name())
# my_tesla.describe_battery()   




#  重写父类的方法 
'''
对于父类的方法，只要它不符合子类模拟的实物的行为，都可对其进行重写。为此，可在子
类中定义一个这样的方法，即它与要重写的父类方法同名。这样，Python将不会考虑这个父类方
法，而只关注你在子类中定义的相应方法。'''
# class ElectricCar(Car):
#     def __init__(self, make, model, year):
#         super(ElectricCar,self).__init__(make, model, year)
#         self.battery_size = 70
#     def fill_gas_tank(self):
#         print("This car  need a gas tank!")
# my_new_car = ElectricCar('calinda','zookerpr',1986)
# my_new_car.fill_gas_tank()

# 将实例用作属性
'''使用代码模拟实物时，你可能会发现自己给类添加的细节越来越多：属性和方法清单以及文
件都越来越长。在这种情况下，可能需要将类的一部分作为一个独立的类提取出来。你可以将大
型类拆分成多个协同工作的小类。'''
class Battery():
    '''一次模拟电动汽车电瓶的简单尝试'''
    def __init__(self, battery_size=70):
        """初始化电瓶的属性"""
        self.battery_size = battery_size
    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")
class ElectricCar(Car):
    """电动汽车的独特之处"""
    def __init__(self, make, model, year):
        """初始化父类的属性，再初始化电动汽车特有的属性"""
        super(ElectricCar,self).__init__(make, model, year)
        self.battery = Battery()
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()




