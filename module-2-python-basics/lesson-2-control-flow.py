"""
Module 2 — Lesson 2: Control Flow (if / elif / else)
Student: Ariel R. Amoguis
Date: September 25, 2026

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
We use if, elif, else if we want a flow or we have conditions that needs to met before executing a block of code. 
If this condition is true, do this. Else if this condition is true, do this one instead. Otherwise, do this.


============================================
KEY VOCABULARY
============================================
- condition: a requirement that needs to be true before a block of code is execute. 
- if / elif / else: if is the first condition, elif is use if there is more another conditions, and else is usually the block of code that will be execute if no if conditions is met.
- comparison operator: a operator/symbol that is use to compare. 
- boolean expression: expression that results True or False
(add more as needed)


============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yourself — not copied from class.
"""

from random import randint

bot = randint(1, 100)

print('Guess the number')
print('1-100, enter 0 to exit')

while True:
    guess = int(input('Enter your guess: '))

    if guess == bot:
        print('Correct, congratulations!')
        break
    elif guess == 0:
            break
    elif guess > bot:
        print('Too high, lower!')
    elif guess < bot:
        print('Too low, higher!')
    else:
        print('Invalid input!')


"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
For me, there is nothing from this topic is too confusing. Just need to familiarize the comparison operators.

============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional]
"""
