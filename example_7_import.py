
# examples for gavin
# import

# import lets you use other peoples code or other code you have writen
# use the import keyword followed by the thing you would like to import

# A package is a collection of Python modules:
# while a module is a single Python file,
# a package is a directory of Python modules containing an additional __init__.py file,
# to distinguish a package from a directory that just happens to contain a bunch of Python scripts.

import file_to_import  # imports our own .py file called file_to_import
# when importing our own file it must be in the same directory (folder) as the file its being imported too

import random  # imports the random module it is a built in module meaning it part of python
# you can import other modules called a package that are not part of python but first they must be installed
# to do so you use a tool called command line tool called pip
# pip normally installs  with python
# some IDE's (Integrated development environment) (pycharm, vscode)
# come with a package manager GUI to install and update packages

file_to_import.print_header('importing')

num_1 = random.randint(0, 100)  # sets num_1 to a random number between 0 and 100
print(num_1)  # prints the random number



