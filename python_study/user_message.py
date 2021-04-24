#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
message = input("Tell me something, and I will repeat it back to you: ")
print(message)

name = input("please enter your name: ")
print("Hello, " + name.title())

age = input("How old are you?")
age = int(age)
if age>=18:
    print("you can")
else:
    print("you can't")

number = input("Enter a number, and I'll tell you if it's even of odd: ")
number = int(number)

if number%2 == 0:
    print("\nThe number " + str(number) + " is even")
else: 
    print("\nThe number " + str(number) + " is odd")

'''


prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."
message = ""
while message != 'quit':
    message = input(prompt)
if message != 'quit':
    print(message)










