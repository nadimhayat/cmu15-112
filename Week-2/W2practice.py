#Problem 1 

def digitCount(n):
    count = 0
    n = abs(n)
    while (n>=10):
        n = n//10
        count += 1
    return count + 1

def test_digitCount():
    assert(digitCount(0) == 1)
    assert(digitCount(-5) == 1)
    assert(digitCount(42) == 2)
    assert(digitCount(-42) == 2)
    assert(digitCount(121) == 3)
    assert(digitCount(-10002000) == 8)
    print('Problem 1 all tests Passed')
test_digitCount()
print("-------------------------------------------")
#problem 2
        
def hasConsecutiveDigits(n):
    prevDigit = -1
    n = abs(n) 
    while (n>0): 
        onesDigit = n%10
        if (prevDigit == onesDigit): 
            return True
        prevDigit = onesDigit
        n //= 10
    return False

def test_hasConsecutiveDigits():
    assert(hasConsecutiveDigits(0) == False)
    assert(hasConsecutiveDigits(123456789) == False)
    assert(hasConsecutiveDigits(1212) == False)
    assert(hasConsecutiveDigits(1212111212) == True)
    assert(hasConsecutiveDigits(33) == True)
    assert(hasConsecutiveDigits(330) == True)
    assert(hasConsecutiveDigits(3003) == True)
    assert(hasConsecutiveDigits(-1212111212) == True)
    print('Problem 2 all tests Passed.')
test_hasConsecutiveDigits()
print("-------------------------------------------")

#problem 3
def gcd(x,y):
    while(y>0):
        temp = x
        x = y
        y = temp%y
    return x

def test_gcd():
    assert(gcd(270,250) == 10)
    assert(gcd(3, 3) == 3)
    assert(gcd(3**6, 3**6) == 3**6)
    assert(gcd(3**6, 2**6) == 1)
    assert (gcd(2*3*4*5,3*5) == 15)
    print('Problem 3 all tests Passed.')
test_gcd()
print("-------------------------------------------")

#problem 4 - counting prime
#4a
a=int(input("a: ")) #10
def pi(n):
    if (n < 2):
        count = 0
    if (n % 2 == 0):
        count = 0
    
    count = 1
    for i in range(3, n+1, 2): 
        if (n%i != 0): 
            count += 1
    return count
print(pi(a))

#4b
def harmonic(x):
    h = 1
    for i in range(2, x+1):
        h += 1/i
    return h

print(harmonic(8))

#problem 5 
def isPrime(n): #113
    if (n < 2):
        return False
    for factor in range(2,n):
        if (n % factor == 0):
            return False
    return True


def addPrime(x):
    nextDigit = 0
    num = x
    while (num > 0): 
        onesDigit = num % 10
        num //= 10
        nextDigit += onesDigit
    return isPrime(nextDigit) and isPrime(x)

print(addPrime(14))

