#!/usr/bin/env python
# -*- coding: utf-8 -*-

user_firstname = "spencer"
user_lastname = "lee"
user_fullname = user_firstname.title() +" " +  user_lastname.title()

welcome_1 = "Hello "  
welcome_2 = " would you like to learn some Python today?"
welcome = welcome_1 + user_fullname + welcome_2

print(welcome)


print(user_fullname.upper())
print(user_fullname.lower())
print(user_fullname.title())

print("Albert Einstein once said, " + "A person who never made mistake never tried anything new" )

famous_person = "Albert Einstein"
einstein_says = " once said, " + "A person who never made mistake never tried anything new"
message = famous_person + einstein_says 

print(message)
 
print("my_name\n\tspencer\n\tlee\n\t")
