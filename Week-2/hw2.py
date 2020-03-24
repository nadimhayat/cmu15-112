def digitCount(n):
    count = 0
    n = abs(n)
    while (n>=10):
        n = n//10
        count += 1
    return count + 1

def is_KaprekarNumber(n):
    p = digitCount(n)
    b = (n**2) % (10**p)
    c = (n**2 - b)/(10**p)
    if (b+c) == n:
        return True
    else: return False

def nthKaprekarNumber(n):
    found = 0
    guess = 0
    while found <= n:
        guess += 1
        if (is_KaprekarNumber(guess)):
            found += 1
    return guess


def testNthKaprekarNumber():
    print('Testing nthKaprekarNumber()...', end='')
    assert(nthKaprekarNumber(0) == 1)
    assert(nthKaprekarNumber(1) == 9)
    assert(nthKaprekarNumber(2) == 45)
    assert(nthKaprekarNumber(3) == 55)
    assert(nthKaprekarNumber(4) == 99)
    assert(nthKaprekarNumber(5) == 297)
    assert(nthKaprekarNumber(6) == 703)
    assert(nthKaprekarNumber(7) == 999)
    print('Passed')

testNthKaprekarNumber()

#problem 2
def almostEqual(d1, d2, epsilon=10**-7):
    return (abs(d2 - d1) < epsilon)

import math
def f1(x): return 42
def i1(x): return 42*x 
def f2(x): return 2*x  + 1
def i2(x): return x**2 + x
def f3(x): return 9*x**2
def i3(x): return 3*x**3


def integral(f, a, b, N):
    s = (b - a) / N
    return s * ((f(a) + f(b))/2) * N

def testIntegral():
    print('Testing integral()...', end='')
    epsilon = 10**-4
    assert(almostEqual(integral(f1, -5, +5, 1), (i1(+5)-i1(-5)),
                      epsilon=epsilon))
    assert(almostEqual(integral(f1, -5, +5, 10), (i1(+5)-i1(-5)),
                      epsilon=epsilon))
    assert(almostEqual(integral(f2, 1, 2, 1), 4,
                      epsilon=epsilon))
    assert(almostEqual(integral(f2, 1, 2, 250), (i2(2)-i2(1)),
                      epsilon=epsilon))
    print('Passed')

testIntegral()

#problem 3
def nearest_kaprekar_number(n):
    bigger = n
    smaller = n
    counter_up = 0
    counter_down = 0
    while not is_KaprekarNumber(bigger):
        bigger += 1
        counter_up += 1
    while not is_KaprekarNumber(smaller):
        smaller -= 1
        counter_down += 1
    if counter_up < counter_down:
        return bigger
    else:
        return smaller

def test_nearest_kaprekar_number():
    print('Testing nearest_kaprekar_number()...', end='')
    assert(nearest_kaprekar_number(8) == 9)
    assert(nearest_kaprekar_number(50) == 45)
    assert(nearest_kaprekar_number(150) == 99)
    assert(nearest_kaprekar_number(2000) == 2223)
    print('Passed')

test_nearest_kaprekar_number()

#problem 4

def carryless_add(x, y):
    counter = -1
    sum2 = 0
    while max(x, y) > 0:
        counter += 1
        num1 = x % 10
        num2 = y % 10
        sum1 = (num1 + num2) % 10
        sum2 += sum1 * (10 ** counter)
        x //= 10
        y //= 10
    return sum2

def carryless_multiply(x, y):
    counter1 = -1
    num1 = 0
    while y > 0:
        counter1 += 1
        digit1 = y % 10
        y //= 10
        sub_x = x
        counter2 = -1
        i = 0
        while sub_x > 0:
            counter2 += 1
            digit2 = sub_x % 10
            i += digit1 * digit2 % 10 * (10 ** counter2)
            sub_x //= 10
        num2 = i * (10 ** counter1)
        result = carryless_add(num1, num2)
        num1 = num2
    return result

def test_carryless_multiply():
    assert(carryless_multiply(643, 59) == 417)
    print("Problem 4: Solved!")

test_carryless_multiply()

#problem 5 - nthSmithNumber(n)