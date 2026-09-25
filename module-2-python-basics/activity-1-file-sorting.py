"""
Module 2 — Activity: File Sorting with os and shutil
Student: Ariel R. Amoguis
Date: September 25, 2026

============================================
WHAT DID YOU BUILD? (explain in your own words)
============================================
[Paste your working script below first, then come back and explain
it here: what does your script do, and what rule did you use to
sort the files? e.g. by extension, by name, by date, etc.]
The code is incomplete and I'm also not able to finish the code even at home.
What I'm able to do is ask the user for a folder path to enter. Checks the user input is existing or not. Print the files inside that folder.
Next the system will ask the user to input a sub_folder and checks it, but here where I got errors and was stucked until the class dismissed.


============================================
KEY VOCABULARY
============================================
- os module: Provides functions for interacting with the operating system
- shutil module: I don't have any idea since I didn't reach this part or I was not able to use this module in the code
- file path: location or address of a file in a computer
- directory: a folder used to organize and store files and other directories
(add more as needed)


============================================
YOUR SCRIPT
============================================
Paste the code you already wrote for this activity below.
"""

import os
import shutil

files_in_folder = os.listdir()

folder_path = input("Enter folder path: ")

if os.path.exists(folder_path):
    print("Folder path exist\n")
else:
    print("Folder path doesn't exist")
    exit()

for i in files_in_folder:
    print(f'{i}')

images = 0
documents = 0
videos = 0
others = 0

sub_folder = input("Enter Subfolder: ")
sub_folder = os.path.join('directory', 'subdirectory', 'filename')

if os.path.exists(sub_folder):
    print("Subfoler already existing")
else:
    print("Creating subfolder")
    os.mkdir(f"{sub_folder}")

# --- paste your existing code here ---


"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
[what tripped you up while building this? e.g. a path that didn't
exist, a file that got overwritten, something that didn't work the
way you expected at first]
I got realy confused even with instructions in the subfolder part. I really thought that it will be same with the folder path input and checking but it's not. 
In the end, I was stuck and not able to accomplish the project


============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional: how is this similar to what real automation scripts do?
think about your own gradebook/attendance workflow — could something
like this save you time there?]
"""
