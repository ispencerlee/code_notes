#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
# print "hello,world!"
print("hello,world!")

# 定义变量'welcome'
welcome = "hello,world!"

#打印变量'welcome'
print(welcome)

# 变量名称格式：只能用字母，数字，下划线，不能数字开头，建议用小写字母，例子如下
tiny_welcome = "Hey"

# 可以用’+‘来连接字符
print(welcome + tiny_welcome)

# 运用'title()函数':将字符串的首字母大写
print(welcome.title())

# 打印人名，并且首字母大写
first_name = "spencer"
last_name = "lee"
# '" "':占用空格，将名和字分隔开
full_name = first_name + " " + last_name 

print(full_name.title())

message = "Hello," + full_name.title() + "!"

print(message)

# 使用制表符或换行符来添加空白，'\n':换行符，'\t':添加制表符
print("language:\npython\njava\nc++")

#'\n','\t':让python换到下一行，并在下一行开头添加一个制表符
print("language:\n\tpython\n\tjava\n\tc++")

# rstrip()方法可以确保字符串末尾没有空白,删除字符串空白,但只是暂时删除
favorite_language = 'python ' 
print(favorite_language)
print(favorite_language.rstrip())

# 若要永久删除字符串中的空白，必须将删除操作的结果存回到变量中
favorite_language = favorite_language.rstrip() 
print(favorite_language)

# str()函数，可以将非字符串装换为字符串
age = 22 
print("Happy " + str(age) + " Birthday")

a = 3 
b = 3.0
c = 2

d = a / b 
print(d)

print(str(4 + 4))
print(str(9-1))
print(str(2*4))
print(str(16/2))

myfavorite_number =  3 
my_number = "My favorite number is " + str (myfavorite_number) 
print(my_number)

# list 定义类表
bicycles = ['trek', 'cannondale', 'redline', 'spcialized']
#打印列表
print(bicycles)
#打印列表元素'[1]'表示列表下标为1的元素
print(bicycles[1])
print(bicycles[1].title())
 
#打印列表最后一个元素
print(bicycles[-1])
 
message = "My first bike is " + bicycles[2].title()
print(message)

name_list = ['spencer','andy','tom','ken','jack']

print(name_list[0])
print(name_list[1])
print(name_list[2])
print(name_list[3])
print(name_list[4])

print(name_list[0].title() + " ,how are you?")
print(name_list[1].title() + " ,how are you?")
print(name_list[2].title() + " ,how are you?")
print(name_list[3].title() + " ,how are you?")
print(name_list[4].title() + " ,how are you?")

todo_list = ['drink coffee', 'wash head', 'take notes']

print("I will be " + todo_list[0])


# 修改列表元素
motocycles = ['honda', 'yamaha', 'suzuki']
print(motocycles)

motocycles[0] = 'ducati'
print(motocycles)

# 在列表末尾添加新元素,使用append()方法
motocycles.append('ducati')
print(motocycles)

# 在列表中插入元素，使用insert()方法
motocycles.insert(0,'ducati')
print(motocycles)

# 从列表中删除元素，使用del()方法,但条件是要知道索引,也可以使用pop()方法
del motocycles[0]
print(motocycles)

# pop()方法可删除列表末尾的元素，并让你能接着用它。属于弹出（pop）源自这样的类比：列表就像一个栈，而删除类表末尾的元素相当于弹出栈顶的元素。

popped_motocycle = motocycles.pop()
print(popped_motocycle)
print(motocycles) 

# 弹出任意位置的元素
first_owned = motocycles.pop(0)
print(first_owned)
print('The first motocycles I owned was a ' + first_owned .title() + '.') 

# 根据值删除元素，可以用remove()方法
motocycles.remove('yamaha')
print(motocycles)

# eg:

motocycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motocycles)

too_expensive = 'ducati'
motocycles.remove(too_expensive)
print(motocycles)
print("\nA " + too_expensive.title() + "is too expensive for me.")

# notes : 方法remove()只删除第一个指定的值。如要删除的值可能出现多次，就需要使用循环判断来判断是否删除了所有的这样的值。 


# 使用sort()对列表进行永久性排序
# 对汽车品牌对首字母进行永久排列

cars = ['bmw', 'toyota', 'tesla']
#按字母顺序排列
cars.sort()
print(cars)

#按反字母顺序排列
cars.sort(reverse=True)
print(cars)

# 使用sorted()对列表进行临时排列
print("Here is my original list:")
print(cars)

print("\nHere is my sorted list:")
print(sorted(cars)) 

print("\nHere is my original list again:")
print(cars)

#倒着打印列表
cars.reverse()
print(cars)

#确认列表长度可以使用len()方法
#python计算列表元素时从1开始
len(cars)
print(len(cars))

# 使用列表时避免索引错误
motocycles = ['honda', 'yamaha', 'suzuki']
print(motocycyles[3])
# 因为列表中只有三个元素，在打印输出第四个元素时，会发生错误

# 遍历整个列表
magicians = ['alice', 'david','carolina']
#让python获取整个列表magicians中的第一个值（'alcie'),并将其储存到变量到magician中
for magician in magicians:
#让python打印magician的值--依然是'alice'
    print(magician)
# 鉴于列表中还有其它值，python返回到循环的第一行，直至列表中元素循环完

eg:
    for cat in cats: 
        for dog in cats: 
            for item in list_of_items:
            

magicians = ['alice', 'dvia', 'carolina']

for magician in magicians:
    print(magician.title() + ", that was a great trick")
    print("\nI can't wait to see next trick" + magician.title())
     
# 在for循环中，想包含多少行代码多可以。
#每个缩进的代码都是循环的一部分

favorite_pizzaes = ['tomato', 'potato', 'apple']

for favorite_pizza in favorite_pizzaes:
    print("I like " + favorite_pizza)
print("It's have pretty nice smell")
     


#创建数值列表
# 使用函数rang()
#使用函数打印一系列数字
for value in range(1,4):
    print(value)

numbers = list(range(1,7))
print(numbers)

#使用函数range(),可以指定步长
#打印1~10的偶数
#range的(2,11)定义了数列范围，（2）定义了步长
even_number = list(range(2,12,2))
print(even_number)

squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)

print(squares)


squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)    
 
#对数字列表进行简单的统计
digits = [1,3,3,0,4,5]
#找到数字列表的最大值
print(min(digits))
#最小值
print(max(digits))
#求和
print(sum(digits))

#列表解析
squares = [value**2 for value in range(1,11)]
print(squares)


for number in range(1,21):
    print(number)

lists = []
for list in range(1,10000001):
    lists.append(list)
print(lists)


lists = []
for list in range(1,1000001):
    lists.append(list)

print(min(lists))
print(max(lists))
print(sum(lists))

lists = []
for list in range(1,21,2):
    lists.append(list)
print(lists)

lists = []
for list in range(3,31,3):
    lists.append(list)
print(lists)

squares = [value**2 for value in range(1,11)]

lists = [list for list in range(3,31,3)]
print(lists)

#切片
#要创建切片,可以指定要使用的第二个元素和最后一个元素。
#与函数rane()一样，python在到达指定的第二个索引前面的元素后停止。


players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
#若未指定第一个索引，python将自动从列表开头开始
print(players[:3])
#若未指定第二个索引，python将中至于末尾
print(players[1:])
#复数索引返回列表末尾相应距离
print(players[-2:])

#遍历切片

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
for palyer in players[:3]:
    print(player.title())

#复制列表
#要复制整个列表可以创建一整个列表切片，方法是同时省略起始索引和终止索引（[:]).
my_foods = ['pizaa', 'fallafel', 'carrot cake']
friend_foods = my_foods[:]
print(my_foods)    
print(friend_foods)


#元组
#定义元组,使用括号标识,且不可更改。元组定义后，可以使用索引来访问其他元素，就像访问列表元素一样
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

#元组中的元素无法修改
dimensions[0] = 20
#会报错

#遍历元组中的所有元素
dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)

#修改元组变量
dimensions = (200, 50)
#if语句
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

#条件测试
#每条if语句的核心都是一个值True或False的表达式， 这种表达式被称为条件测试。
#在python中检查是否相等是区分大小写

#使用and检查多个条件
#使用in检查特定值是否在列表中

#python中并不要求if-elif结构后面必须有else代码块，可以省略

#字典
#创建字典
alien_0 = {'color':'green', 'points':5}

#打印字典元素
print(alien_0['color'])
print(alien_0['points'])

#创建一个空字典
alien_0 = {}

#向字典中添加元素
alien_0['color'] = 'green'
alien_0['points'] = '6'

print(alien_0)
#修改字典中的值
alien_0={'clor':'green'}
print("This alien is " + alien_0['color'] + ".")

alien_0['color'] = blue
print("This alien is now " + alien_0['color'] + ".")

#删除键-值对
alien_0 = {'color':'green', 'points':"4"}
print(alien_0)

del alien_0['color']
print(alien_0)


#使用字典
#python中字典是一系列键-值的对。每个键都与一个值相关联，可以使用那个键来访问与之对应的值。
#与键相关的值可以是数字，字符串，列表乃至字典。事实上，可将任何python对象用作字典中的值。
#字典用放在花括号{}中的一系列键-值对表示
alien_0 = {'color':'green', 'points':5}

#字典是一种动态结构，可随时在其中添加键-值对。
#要添加键-值对可依次指定字典名，用括号括起的键和相关的值。

#用户输入
#input()
message = input("Tell me something, and I will repeat it back to you: ")
print(message)

name = input("please enter your name: ")
print("Hello, " + name.title())

age = input("How old are you?")
#将字符串类型转换为int类型用于比较
age = int(age)
if age>=18:
    print("you can")
else:
    print("you can't")

age = 12

if age < 4:
    print("Your admission cost is $0")
elif age < 18:
    print("Your admission cost is $5")
else:
    print("Your admission cost is $10")

    requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished makding pizza")

#如果你只想执行一个代码块，就使用if-elif-else结构 
#如果要运行多个代码块，就使用一系列独立的if语句

#使用while循环
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

number = input("Enter a number, and I'll tell you if it's even of odd: ")
number = int(number)

if number % 2 == 0:
    print("\nThe number " + str(number) + " is even")
else:
    print("\nThe number " + str(number) + " is odd")

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."
message = ""
while message != 'quit':
    message = input(prompt)
if message != 'quit':
    print(message)

# 函数

#定义函数


def greet_user():
    """显示简单的问候语"""
    print("Hello!")


greet_user()

'''
#向函数传递信息


def greet_user(username):
    """显示简单的问候语"""
    print("Hello, " + username.title() + "!")


greet_user('spencer')

# 实参和形参
# 在greet_user中username是形参，spencer是实参


def display_message():
    print("In this section I learned how to use function.")


display_message()


def favorite_book(title):
    print("My favorite book is: " + title.title())


favorite_book('python')

# 传递实参

#位置实参
