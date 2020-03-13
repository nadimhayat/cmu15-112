import math
def f():
    print("This is a user-defined function")
    return 42

print("Some basic types in Python:")
print(type(2))           # int
print(type(2.2))         # float
print(type("2.2"))       # str  (string)
print(type(2 < 2.2))     # bool (boolean)
print(type(math))        # module
print(type(math.tan))    # builtin_function_or_method ("function" in Brython)
print(type(f))           # function (user-defined function)
print(type(type(42)))    # type

import math
print(math.e)
print(math.pi)

print("#####################")
print("Type conversion functions:")
print(bool(0))   # convert to boolean (True or False)
print(float(42)) # convert to a floating point number
print(int(2.8))  # convert to an integer (int)

print("And some basic math functions:")
print(abs(-5))   # absolute value
print(max(2,3))  # return the max value
print(min(2,3))  # return the min value
print(pow(2,3))  # raise to the given power (pow(x,y) == x**y)
print(round(2.354, 1))

print (5//2)
-----------------------------------------
#Category	Operators
#Arithmetic	+, -, *, /, //, **, %, - (unary), + (unary)
#Relational	<, <=, >=, >, ==, !=
#Assignment	+=, -=, *=, /=, //=, **=, %=, <<=, >>=
#Logical	and, or, not
--------------------------------------