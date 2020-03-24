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
    assert(nthKaprekarNumber(0) == 1)
    assert(nthKaprekarNumber(1) == 9)
    assert(nthKaprekarNumber(2) == 45)
    assert(nthKaprekarNumber(3) == 55)
    assert(nthKaprekarNumber(4) == 99)
    assert(nthKaprekarNumber(5) == 297)
    assert(nthKaprekarNumber(6) == 703)
    assert(nthKaprekarNumber(7) == 999)
    print('Problem 1 all tests Passed-------------')

testNthKaprekarNumber()