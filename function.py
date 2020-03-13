x = 5
def f(y, z):
    result = x + y + z
    return result
print(f(1, 2))
print(f(3, 4))

def isPositive(x):
    print("Hello!")   # runs
    print("Goodbye!")
    return (x > 0)
     # does not run ("dead code")

print(isPositive(2))

print('Next function')

def cubed(x):
    return x**3 # Here is the error!

cubed(2)          # seems to work!
print(cubed(3))   # sort of works (but prints None, which is weird)
print(2*cubed(4))

print('Next function')
def hypotenuse(a, b):
    return ((a**2) + (b**2))**0.5

print(hypotenuse(3, 4)) # 5.0 (not 5)
print("---------------------")

def f(w):
    return 10*w

def g(x, y):
    return f(3*x) + y

def h(z):
    return f(g(z, f(z+1)))

print(h(1))

print("---------------------")
def onesDigit(n):
    return n%10

def largerOnesDigit(x, y):
    return max(onesDigit(x), onesDigit(y))

print(largerOnesDigit(134, 672)) # 4
print(largerOnesDigit(132, 674))
print("---------------------")
def f(x):
    print("In f, x =", x)
    x += 5
    return x

def g(x):
    return f(x*2) + f(x*3)

print(g(2))

print("---------------------")
def f(x):
    print("In f, x =", x)
    x += 7
    return round(x / 3)

def g(x):
    x *= 10
    return 2 * f(x)

def h(x):
    x += 3
    return f(x+4) + g(x)

print(h(f(1)))