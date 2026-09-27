"""
Module 2 — Lesson 4: Functions
Student: Ariel R. Amoguis
Date: September 27, 2026

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
Functions is a block of code that does a task and can be called whenever you need it. 
For example the calculator, there are functions for computations, add, minus, multiply, divide, and etc. 
If you pressed the add button, you are calling the add function of the calculation, same goes with the other operations.


============================================
KEY VOCABULARY
============================================
- parameters: variable/s that are put in the parenthesis next to the name of the function
- return values: 'return' basically give back the data or value after the function excuted. 
- arguments: arguments are placed inside the parenthesis when the functions are called. 
- pass: functions cannot be empty, with pass you can temporarily make the function 'blank' or do nothing.


============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yourself — not copied from class.
"""

num1 = int(input('Enter number 1 : '))
num2 = int(input('Enter number 2 : '))

def add():
    sum = num1 + num2
    print(sum)
    
def minus():
    difference = num1 + num2
    return difference

def multiply():
    product = num1 + num2
    return product

def divide():
    qoutient = num1 + num2
    print(qoutient)

print('Enter operation [1: add, 2: minus, 3: multiply, 4: divide ]')
operation = int(input('> '))

if operation == 1:
    add()
elif operation == 2:
    print(minus())
elif operation == 3:
    print(multiply())
elif operation == 4:
    divide()
else:
    print('Invalid input')


"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
After writing the code, I tried it, it works and no error but there are no total or the answer to the numbers I add. 
I found out that when using return to return the value, you must call the function this way 'print(function_name())'. 
I changed it a little bit, the add and divide funtion in my preference of creating a function. 
I prefer more the way add and divide function, where the printing of total is inside the function too.



============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional]
"""
