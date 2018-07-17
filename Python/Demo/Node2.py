# -- coding: utf-8 --
'''
Created on 2018��6��26��

@author: Administrator
'''
# 9.3 继承
# 9.3.1 子类的方法 __init__()
'''如果你要编写的类是另一个现成类的特殊版本，可使用
继承。一个类继承另一个类时，它将自动获得另一个类的所有属性和方法；原有的类称为父类，
而新类称为子类。子类继承了其父类的所有属性和方法，同时还可以定义自己的属性和方法。'''
class Car():
# '''一次模拟汽车的简单尝试'''
# 创建子类的实例时，Python首先需要完成的任务是给父类的所有属性赋值。为此，子类的方
# 法 __init__() 需要父类施以援手。
# 例如，下面来模拟电动汽车。电动汽车是一种特殊的汽车，因此我们可以在前面创建的 Car
# 类的基础上创建新类 ElectricCar ，这样我们就只需为电动汽车特有的属性和行为编写代码。
# 下面来创建一个简单的 ElectricCar 类版本，它具备 Car 类的所有功能:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.battery_size = 100;
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self, miles):
        self.odometer_reading += miles


# class ElectricCar(Car):
# #    """电动汽车的独特之处"""
#     def __init__(self, make, model, year):
# #    """初始化父类的属性"""
#         Car.__init__(make, model, year)
#         my_tesla = ElectricCar('tesla', 'model s', 2016)
#         print(my_tesla.get_descriptive_name())

# 9.3.3 给子类定义属性和方法
class ElectrickCar(Car):
#    """电动汽车的独特之处"""
    def __init__(self, make, model, year):
#    """初始化父类的属性"""
        Car.__init__(self,make, model, year)
#         self.battery_size = 70;
    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")
my_tesla = ElectrickCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
class father():  
    def __init__(self,age):  
        self.age = age;  
    def get_age(self):  
        print(self.age);  
          
class son(father):  
    def __init__(self,age):  
        father.__init__(self,age);#注意此处参数含self  
        self.toy_number = 5;  
    def get_toy_number(self):  
        print(self.toy_number);  
myson = son(6)  
myson.get_age()  
myson.get_toy_number()  


# 9.3.4 重写父类的方法
# 对于父类的方法，只要它不符合子类模拟的实物的行为，都可对其进行重写。为此，可在子
# 类中定义一个这样的方法，即它与要重写的父类方法同名。这样，Python将不会考虑这个父类方
# 法，而只关注你在子类中定义的相应方法。
class CodeCar():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.battery_size = 100;
    def fill_gas_tank(self):
        print "this is car need a gas tank!"
class ElectricCar(Car):
    def __init__(self,make,model,year):
        Car.__init__(self, make, model, year);
    def fill_gas_tank(self):
        print "this is car doesnot need a gas tank!"

mycar = ElectricCar("demo","demo","1968");
mycar.fill_gas_tank()

# 9.3.5 将实例用作属性









