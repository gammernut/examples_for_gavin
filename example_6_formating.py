# examples for gavin
# formatting with fstrings , .format() , and case manipulation


full_name = input('enter your full name\n')  # \n is a line break breaks of to a new line in the output
print(full_name.lower())  # makes lower case
print(full_name.upper())  # makes upper case
print(full_name.title())  # makes title case ie. first letter of each word is upper case

print("hello, {} how are you?".format(full_name.title()))  # this is a formatted string using .format()
# the {} are place holders whatever is in the .format() function is put printed on output


full_name = input('enter your full name\n')  # \n is a line break breaks of to a new line in the output
print(full_name.lower())  # makes lower case
print(full_name.upper())  # makes upper case
print(full_name.title())  # makes title case ie. first letter of each word is upper case

print(f"hello, {full_name.title()} how are you?")  # this is a fstring fstrings are nice
# ftrings are a bit different but easier to read and work with
# to use a fstring place a f before your string
# then use the {} with the variable you would like to fill in inside of the {}
