#problem 1

import string 
def vowelCount(s):
    vowels = 0
    for i in range(len(s)):
        if(s[i]=='a' or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u' or s[i]=='A' or s[i]=='E' or s[i]=='I' or s[i]=='O' or s[i]=='U'):
            vowels=vowels+1
    return vowels

def vowelCount(s): 
    count = 0
    vowel = set("aeiouAEIOU")               #creating a set of vowels 
    for alphabet in s:                      # Loop to traverse the alphabet, in the given string
        if alphabet in vowel:               # If alphabet is present in set vowel 
            count = count + 1
    return count

def test_vowelCount():
    assert(vowelCount("Abc def!!! a? yzyzyz!") == 3)
    assert(vowelCount("abcdefg") == 2)
    assert(vowelCount("ABCDEFG") == 2)
    assert(vowelCount("") == 0)
    assert(vowelCount("This is a test.  12345.") == 4)
    assert(vowelCount(string.ascii_lowercase) == 5)
    assert(vowelCount(string.ascii_lowercase*100) == 500)
    assert(vowelCount(string.ascii_uppercase) == 5)
    assert(vowelCount(string.punctuation) == 0)
    assert(vowelCount(string.whitespace) == 0)
    print("Problem 1 all tests passed")

test_vowelCount()

#problem 2
def eq_interleave(s1, s2):
    i = 0
    s12 = ""
    add = ""
    num = len(s1) 
    while num>0: 
        s12 = s1[i] + s2[i] 
        add += s12
        i +=1 
        num -= 1  
    return add

def uneq_interleave(s1, s2):
    num = 0
    initial = ""
    latter = ""
    if len(s1) == len(s2): 
        return eq_interleave(s1, s2)
    elif len(s2) > len(s1): 
        num = len(s2) - len(s1) 
        s2 = (s2[0:len(s2)-num])
        initial = eq_interleave(s1, s2) 
        latter = s2[len(s2)-num:len(s2)]
        final = initial + latter
    elif len(s1) > len(s2):
        num = len(s1) - len(s2)
        s1 = (s1[0:len(s1)-num])
        initial = eq_interleave(s1, s2) 
        latter = s1[len(s1)-num:len(s1)]
        final = initial + latter
    
    return final
print(uneq_interleave("abcde", "abcdefgh"))

'''
def test_Interleave():
    assert(uneq_interleave("abcdefg", "abcdefg") == "aabbccddeeffgg")
    assert(uneq_interleave("abcde", "abcdefgh") == "aabbccddeefgh")
    assert(uneq_interleave("abcdefgh","abcde") == "aabbccddeefgh")
    assert(uneq_interleave("Smlksgeneg n a!", "a ie re gsadhm") ==
                      "Sam likes green eggs and ham!")
    assert(uneq_interleave("","") == "")
    print("Problem 2 all tests Passed!")

test_Interleave()
'''
#problem 3
def hasBalancedParentheses(s):