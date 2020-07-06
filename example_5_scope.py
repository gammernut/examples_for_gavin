# examples for gavin
# scope

# a variable in a function is in the "scope" of the function and not affected by variables outside of its scope
# Global scope: The names that you define in this scope are available to all your code
# Local scope: The names that you define in this scope are only available or visible to the code within the scope
# ie. the function it was made it

# scope is confusing

same_var = 'piss'


def fun_1(same_var):
    print(same_var)


fun_1('shit')

print(same_var)
