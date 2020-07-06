
# examples for gavin
# functions

# lets say you want to print hello world five times you could do this

print('hello world')
print('hello world')
print('hello world')
print('hello world')
print('hello world')

#  lets also say you decide you want it to say something else now you have to go back line by line and change each one
# this is shit dont do this to yourself

# instead we can write a function
# you start a function with def (for define function) followed by the name of your function same naming concepts
# apply to function names as do variable names
# after the function name you need () and then :
# then you indent/tab/four spaces and write the code for your function
# you call (make it happen) your function by typing its name with () at the end ie hello_function()
# pep8 says to have two blank lines before and after a defined function


def hello_function():
    print('hello world')


hello_function()
hello_function()
hello_function()
hello_function()
hello_function()

# now if you want hello world to say something else you only need to change one line the print line in the function

