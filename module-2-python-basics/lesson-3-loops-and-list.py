"""
Module 2 — Lesson 3: Loops & Lists
Student: Ariel R. Amoguis
Date: September 25, 2026

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
Loops and list. List is a variable that has many value, from the name itself is a 'list". 
Loops, from the name itself too, a 'loop', a block of code is done again and again until a certain condition met, a loop can also be infinite.


============================================
KEY VOCABULARY
============================================
- list: one container, stores many values
- for loop: mostly used for iteration
- while loop: a loop that can be infinite
- index: position of values inside a list, starts with 0
- iteration: accessing the items of a list one at a time
(add more as needed)


============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yourself — not copied from class.
"""

fav = ['aysukrim', 'prays', 'sinigang', 'apol']

print("Favorites")

for c, i in enumerate(fav, start=1):
    print(f"{c}: {i}")

while True:
    inputed = input("Type anything, press q to exit: ")

    print(f"You've entered: {inputed}")

    if inputed == 'q' or inputed == "Q":
        break


"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
One thing to remember is, if you have to conditions, you can use 'or' but still need to put the variable that will be check, in this code its the 'inputed'. 
That's the only error I had

============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional]
"""
