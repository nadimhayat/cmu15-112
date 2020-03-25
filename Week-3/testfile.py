#Problem 1 
'''
def digitCount(n):
    count = 0
    n = abs(n)
    while (n>=10):
        n = n//10
        count += 1
    return count + 1

print(digitCount(-5000))

#problem 2

a = int(input("n= "))
        
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

print(hasConsecutiveDigits(a))
'''


'''
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
'''

###### n = int(input("Input N: "))
'''
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
            else: 
                a = 1
            if int(root1 + 0.5) ** 3 == i:
                b = root1
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
'''


s1 = 'pyt'
s2 = 'hon'

s3 = "" + s2
print(s3)

def test_Interleave():
    assert(uneq_interleave("abcdefg", "abcdefg") == "aabbccddeeffgg")
    assert(uneq_interleave("abcde", "abcdefgh") == "aabbccddeefgh")
    assert(uneq_interleave("abcdefgh","abcde") == "aabbccddeefgh")
    assert(uneq_interleave("Smlksgeneg n a!", "a ie re gsadhm") ==
                      "Sam likes green eggs and ham!")
    assert(uneq_interleave("","") == "")
    print("Problem 2 all tests Passed!")

test_Interleave()