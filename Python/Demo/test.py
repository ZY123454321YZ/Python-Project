# -- coding: utf-8 --
age = 23
message = "Happy " + str(age) + " Birthday!"
print(message)
one = 3/2
two = 3.0/2
print one
print two
print one + two


#
bicyles = ["one","two","three"]
print bicyles
print bicyles[2]
print bicyles[-1]
bicyles[0] = "distinct"
print bicyles
bicyles.append(3)
print bicyles






bicyles.insert(0, 200)
print bicyles
del bicyles[1]
print bicyles
peple = bicyles.pop()
print bicyles
bicyles.insert(4,500)
print bicyles
bicyles.pop(2)
print bicyles


#字典
alien = {'key':"value",'key1':'value2'}
alien['key']='city'
print(alien['key'])
print(alien['key1'])
del alien['key']
print (alien)
alien = {'car':'speed','key':'value'}
print(alien)
for key,value in alien.items():
    print("\nkey = "+key)
    print("value: "+value)
    
for name in alien.keys():
    print(name.title())
    
# message = input("start message ...")
# print(message)
    
#while 循环
# current_number = 1
# while current_number <=5:
#     print(current_number)
#     current_number+=1
#     
# prompt = "\nPlease enter the name of a city you have visited:"
# prompt += "\n(Enter 'quit' when you are finished.) "
# while True:
#     city = input(prompt)
#     if   city == 'quit':
#      break
#     else:
#      print(city)

def make_pizza(size,*toppings):
    print("\nMaking a " + str(size) +"-inch pizza with the following toppings:")
    print("start . ......")
    for topping in toppings:
        print("- " + topping)

