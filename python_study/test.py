#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
alien_0 = {'color': 'green', 'points': '5'}
alien_1 = {'color': 'blue', 'points': '9'}
alien_2 = {'color': 'yellow', 'points': '7'}

aliens = [alien_0, alien_1, alien_2]

print(aliens)

for alien in aliens:
    print(alien)

#import model

import random

for i in range(6):
    print(random.randint(1, 10))


import sys

while True:
    print("TYPE 'exit' to exit. ")
    response = input()
    if response == 'exit':
        sys.exit()
    else:
        print('You typed ' + response + '.')

import random

print("Let's thinking a number between 1 andd 20")

secretNumber = random.randint(1, 20)
number = int(input())

while int() != secretNumber:
    if number > secretNumber:
        print("Your guess is too high")
    elif number < secretNumber:
        print("Your guess is too low")
    else:
        print("You are right")



# 小程序：猜数字

#This is a guess the number game.

import random

secretNumber = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')

# Ask the player ot guess 6 times
for guessesTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high')
    else:
        break

if guess == secretNumber:
    print('Good job! You guessed my number in ' + str(guessesTaken) +
          ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))



'''

import random

message = [
    'It is certain', 'It is decidedly so ', 'Yes definitely',
    'Reply hazy try again', 'Ask again later', 'Concrntrate and ask again',
    'My reply is no', 'Outlook not so good', 'Very doubtful'
]

print(message[random.randint(1, len(message) - 1)])
