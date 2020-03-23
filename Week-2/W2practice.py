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