
# examples for gavin
# strings , ints , floats and other data types

# Python has multiple  Data Types:
#
# Integers/int are whole numbers ie. 1 , 2 , 3 so on
#
# Floating-Point Numbers/float basically a int with with a decimal point ie 1.3 , 1.5 , 2.8 , 3.1 so on
#
# String/str Strings are sequences of character data ie. text between 'hello world' "hello world"
#
# Boolean may have one of two values, True or False ie 'good' in 'this is a great example' returns false
# Boolean cont. 'good' not in 'this is a great example' returns true
#
# Complex Numbers Complex numbers are specified as <real part>+<imaginary part>j ie. 2+3j
#

str_1 = 'hello '

str_2 = 'world'


int_1 = 1

int_2 = 2

print(str_1+str_2)  # adding two strings together is called string concatenation


print(int_1+int_2)

print(str_1+int_1)  # errors out because you cant combine a str and int


# The str() function changes the specified value into a string
converted_int_1 = str(int_1)  # we take the converted variable int_1 and store it in a new variable to work with later


# The int() function changes the specified value into an integer

print(str_1+converted_int_1)  # now it works since the converted_int_1 is a string
