'''
#!/usr/bin/python3
print("Hello, world!")
print('runoob')

print("Hello, world!"); print('runoob')

if False:
    print("True")
else:
    print("false")

raw_input("press enter for escap, other one show ....\n")

x = "a"
y = "b"

print(x)
print(y)

print(x),
print(y),


if expression:
    suite
elif expression:
    suite
else:
    suite


#变量赋值不需要类型声明
counter = 100  #赋值整型变量
miles = 1000.0  #浮点型
name = "Spencer"  #字符串

print(counter)
print(miles)
print(name)

#多变量赋值
a = c = b = 1

a, b, c = 1, 3, "Spencer"

#python中有五个标准数据类型：
Numbers 
String 
List 
Tuple
Dictionary


var1 = 1 
var2 = 20

del var1[,var2[,var3]]




str = "Hello,world!"

print (str) 
print (str[0]) #输出字符串的第零个字符
print (str[1]) #输出字符串的第一个字符
print (str[5:])#输出字符串的第5个字符以后的字符串
print (str*4)#输出五次字符串
print (str + "hey")#连接一个“hey”的字符串


# List (列表）
# List支持字符，数字，字符串甚至可以包含列表（即嵌套）
#列表用[]表示，是python最通用的复合数据类型
#类表中的值也可以用到变量[头下标，尾下标]，就可以截取相应的列表，从右到左索引默认0开始，从右到左默认从-1开始，下标可以为空表示从头取到尾

list=['hello','everyone',2,4.3,100.11]
tinylist=['hey','now']

print (list[1:3])#打印输出'list'从左到右含头下标1,尾下标3之前的列表元素
print (list)#打印'list'列表的所元素
print (list * 4)
print (list + tinylist)




#python元组
#元组是另一个数据类型，类似于List(列表)
#元组用()标识，内部元素用逗号分割开，但元组不能二次赋值，相当于只读列表

tuple = ('how', 'to', 4, 245.42)
tinytuple = ('use', 'vim')

print (tuple)     #输出完整元组
print (tuple[2:3])

tuple = ('how', 'to', 4, 245.42)
list=['hello','everyone',2,4.3,100.11]

tuple[2] = 30       #tuple不允许更新
list[2] = 30        #list可以更新



# python字典
#字典(dictionary)是出列表以外python之中最灵活的内置数据结构类型。
#类表是有序的对象集合，字典是无序的对象集合
#两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移来存取
#字典用"{}"来表示，字典由索引(key)和它对应的值value组成




dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"

tinydict = {'hello', 'everyone', 'how'}

print(dict)             #输出完整的字典
print (dict[2])         #输出键为2的值 
print(dict['one'])      #输出键为'one'的值
print tinydict.key()    #输出所有的键
print tinydict.values() #输出所有的值




#python数据类型转换
#有时候，我们需要对数据内置的类型进行转换，只需要将数据类型作为函数名即可。
#例子如下：
int(x[,base])       #将x转化为一个整数
long(x[,base])      #将x转化为一个长整数


# python运算符
# python语言支持以下类型的运算符：
#   算数运算符
#   比较(关系）运算符
#   赋值运算符
#   逻辑运算符
#   位运算符
#   成员运算符
#   身份运算符
#   运算符优先级

# 算数运算符：
# + — * / 
# %（取模，返回除法的余数） 
# **（幂,返回x的y次幂）
# // (取整除，返回商的整数部分）



a = 302
b = 453
c = 0



c = a + b 
print(c)

c = a - b 
print (c)

c = a * b 
print(c)

c = a / b 
print(c)

c = a % b 
print(c)

#修改变量a, b  
a = 4 
b = 3 

c = a**b 
print(c)

c = a//b 
print(c)


'''





















