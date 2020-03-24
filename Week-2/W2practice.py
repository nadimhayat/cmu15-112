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

#problem 6

def isPerfectNumber(n):
    if (n <= 1): return False
    divisorSum = 0
    maxFactor = round(n**1/2)
    for divisor in range(1, maxFactor+1):
        if (n % divisor == 0):
            divisorSum += divisor
    return (divisorSum == n)

def nthPerfectNumber(n):
    guess = 0 # all numbers starting from 0
    found = 0 # perfect number
    count = 0 # counts perfect numbers
    while (count < n):
        guess += 1
        if (isPerfectNumber(guess)):
            found = guess
            count += 1
    return found


print(nthPerfectNumber(2))

#problem 7
def longestDigitRun(n):
    highest_streak = 0
    highest_digit = 0
    streak = 0
    while (n > 0): 
        last_digit = n % 10
        n //= 10
        if (last_digit == n % 10):
            streak += 1
            if streak > highest_streak:
                highest_streak = streak
                highest_digit = last_digit
            elif highest_streak == streak:
                highest_digit = min(highest_digit, last_digit)
        else:
            streak = 0

    return highest_digit

print(longestDigitRun(233113))

#problem 8
def longestIncreasingRun(n):
    highest_streak = 0
    increasing_digit = 0
    streak = 0
    p = 1
    while (n > 0): #1232
        last_digit = n % 10 #3
        n //= 10 
        if (last_digit > n % 10):
            streak += 1
            if streak > highest_streak:
                highest_streak = streak
                increasing_digit = ((n % 10)*10**p) + last_digit
                p += 1
            last_digit = increasing_digit
        else:
            streak = 0

    return increasing_digit

print(longestDigitRun(12355456))

#problem 9
n = int(input("Input N: "))
def palindrome(n):
    num = n
    rev = 0
    d = 0
    while n > 0:
        d = n%10
        n = n//10
        rev = rev*10 + d
    if num == rev:
        return True
    else: return False
        
def prime(n):
    if (n < 2):
        return False
    if (n == 2):
        return True
    if (n % 2 == 0):
        return False
    maxFactor = round(n**0.5)
    for factor in range(3,maxFactor+1,2):
        if (n % factor == 0):
            return False
    return True
def nthPalindromePrime(n):
    found = 0
    guess = 0
    while (found <= n):
        guess += 1
        if (palindrome(guess) and prime(guess)):
            found += 1
    return guess
print(nthPalindromePrime(n))

#problem 10
def prime(n):
    if (n < 2):
        return False
    if (n == 2):
        return True
    if (n % 2 == 0):
        return False
    maxFactor = round(n**0.5)
    for factor in range(3,maxFactor+1,2):
        if (n % factor == 0):
            return False
    return True


def digitCount(n):
    count = 0
    n = abs(n)
    while (n>=10):
        n = n//10
        count += 1
    return count + 1   


def leftTruncatable(n):
    d = 0 
    dcount = digitCount(n) - 1                
    while n > 0:  
        if (prime(n)): #4 6773 = (10**4)*4 % 10**4--> 6773 --> 773 --> 1
            d = n % (10**dcount)
            n = n // 10
            if d > 0: 
                if (prime(d)):
                    return True
                else: return False
            dcount -= 1
        else:
            return False
        return True
def nthLeftTruncatablePrime(n): #10 53
    found = 0
    guess = 0
    while (found <= n):
        guess += 1
        if (leftTruncatable(guess)):
            found += 1
    return guess
 
print(nthLeftTruncatablePrime(10))

#problem 11
def prime(n):
    if (n < 2):
        return False
    if (n == 2):
        return True
    if (n % 2 == 0):
        return False
    maxFactor = round(n**0.5)
    for factor in range(3,maxFactor+1,2):
        if (n % factor == 0):
            return False
    return True

def CarolPrime(k):
    n = ( (((2**k) - 1)**2) - 2) 
    print(n)
    if (prime(n)):
        return True
    else: return False

print(CarolPrime(15))

#Problem 12


def sumOfSquaresOfDigits(n): #777
    num = 0
    while n > 0:
        d = n % 10
        num += d**2
        n //= 10
    return num

def isHappyNumber(a): #97
    a = sumOfSquaresOfDigits(a)
    if a == 0: return 1
    if a == 1: return True
    while a >= 10:
        a = sumOfSquaresOfDigits(a)
        print(a)
    if a == 1: 
        return True
    elif a == 4: 
        return False 


def nthHappyNumber(n):
    found = 0
    guess = 0
    while (found <= n):
        guess += 1
        if (isHappyNumber(guess)):
            found += 1
    return guess

print(nthHappyNumber(5))

#problem 13
def most_frequent_digit(n):
    best_count = 0
    best_digit = 0
    for x in range(10):
        m = n
        count = 0
        print(count)
        while m > 0:
            digit = m % 10
            m //= 10
            if x == digit:
                count += 1
        if count > best_count:
            best_count = count
            best_digit = x
    return best_digit


def test_most_frequent_digit():
    assert(most_frequent_digit(1123) == 1)
    assert(most_frequent_digit(2211) == 1)
    assert(most_frequent_digit(18822) == 2)
    assert(most_frequent_digit(100000) == 0)
    print("Problem 1: Solved!")

test_most_frequent_digit()

#problem 14
import math
def factor(n):
    a = 0
    b = 0
    for i in range(2, n): #12
        if (n % i == 0):
            a = math.sqrt(i)
            b = i**(1/3)
            if int(root + 0.5) ** 2 == i:
                a = root  
                continue
            else: 
                a = 1
            if int(root1 + 0.5) ** 3 == i:
                b = root1
                break
            else: 
                b = 1
    return a, b

print(factor(64))
            

def is_powerful_number(n):
    #n = a**2 * b**3
    a = factor(n)
    if a is None:
        return False
    if (n % a == 0) and (n % a**2 == 0):
        return True
    else:
        return False

def test_is_powerful_number():
    assert(is_powerful_number(4) == True)
    assert(is_powerful_number(8) == True)
    assert(is_powerful_number(46) == False)
    assert(is_powerful_number(0) == False)
    assert(is_powerful_number(12) == False)
    assert(is_powerful_number(288) == True)
    print("is_powerful_number() passed!")


test_is_powerful_number()


def nthPowerfulNumber(n): #10 53
    found = 0
    guess = 0
    while (found <= n):
        guess += 1
        if (is_powerful_number(guess)):
            found += 1
    return guess

print(factor(23))



