"""
Module 2 — Lesson 1: Variables & Data Types
Student: Ariel R. Amoguis
Date: September 25, 2026

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
Think the variable as a box, a container that has a value or the item inside. 
Now, we different type of item, it can be wood, metal, glass, leather. That type is the data type, the data type tells what type of value is inside the variable.


============================================
KEY VOCABULARY
============================================
- variable: container that has a value
- data type: the type of the value inside the variable
- int: short for integer, used for whole numbers
- float: the float is used for numbers that has decimals
- string: used for text, must be inside '' or "", if a number is inside the string, it will be considered as string and not a integer.
- boolean: returns True or False only
(add more as needed)


============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yourself — not copied from class.
"""

name = input("Enter your name: ")

is_valid_username = bool(name)  
print(is_valid_username)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(f"Name: {name}")
print(f'The sum of {num1} and {num2} is {num1+num2}')
print(f'The difference of {num1} and {num2} is {num1-num2}')
print(f'The product of {num1} and {num2} is {num1*num2}')
print(f'The qoutient of {num1} and {num2} is {num1/num2}')
print(type(num1/num2))


"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
Nothing, this is a very basic and important lesson in programming.


============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional]
"""
