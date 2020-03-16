

#Problem 1


def distance(x1,y1,x2,y2):
    return ((y1-y2)**2+(x2-x1)**2)**0.5

def test_distance():
    assert(distance(0, 2, 0, 2) == 0)
    assert(distance(0, 0, 4, 0) == 4)
    print("Problem 1 all tests passed!")

test_distance()

print('-----------------------------------------------------')

#Problem 2



def circlesIntersect(x1,y1,r1,x2,y2,r2):
    DistanceBetweenCircles = ((y2-y1)**2+(x2-x1)**2)**0.5
    return (DistanceBetweenCircles <= (r1 + r2))
    
def test_circlesIntersect():
    assert(circlesIntersect(0,0,2,4,0,2) == True)
    assert(circlesIntersect(0,0,2,6,6,1) == False)
    print("Problem 2 all tests passed")

test_circlesIntersect()    

print('-----------------------------------------------------')

#Problem 3


#type1
def getInRange(x, bound1, bound2):
    if ((x > bound1) and (x<bound2)):
        return x
    elif ((bound1<bound2) and (x<bound1)):
        return bound1
    elif ((bound2<bound1) and (x<bound2)):
        return bound2
    elif ((bound1>bound2) and (x>bound1)):
        return bound1
    else: 
        return bound2
#type2
def getInRange(x, bound1, bound2):
    low = min(bound1, bound2)
    high = max(bound1, bound2)
    if x<low: x=low
    if x>high: x=high
    return x
#type3
def getInRange(x, bound1, bound2):
    low = min(bound1, bound2)
    high = max(bound1, bound2)
    return min(max(x,low), high)

def test_getInRange():
    assert(getInRange(1,3,5) == 3)
    assert(getInRange(4,3,5) == 4)
    assert(getInRange(6,5,3) == 5)
    print("Problem 3 all tests passed")

test_getInRange()
    
print('-----------------------------------------------------')

#problem 4

import math 
def eggCartons(eggs):
    egg = abs(eggs)
    C = egg//12
    return C
def eggCartons(eggs):
    eggs = abs(eggs)
    return math.ceil(eggs/12)
def test_eggCartons():
    assert(eggCartons(24) == 2)
    assert(eggCartons(25) == 3)
    assert(eggCartons(23) == 2)
    print("Problem 4 all tests passed")
test_eggCartons()
print('-----------------------------------------------------')

#problem 5
#pascalsTriangleValue(row, col) 

import math

def pascalsTriangleValue(row, col):
    if ((row < 0) or (col < 0) or (col>row) or (col==row)): return None
    return (math.factorial(row)/(math.factorial(col)*math.factorial(row-col)))

def test_pascalsTriangleValue():
    assert(pascalsTriangleValue(4,2) == 6)
    assert(pascalsTriangleValue(4,4) == None)
    assert(pascalsTriangleValue(2,4) == None)
    print("Problem 5 all tests passed")

test_pascalsTriangleValue()
print('-----------------------------------------------------')

#problem 6

def isFactor(f,n):
    if (n%f == 0): return True
    if (n%f != 0): return False 
def test_isFactor():
    assert(isFactor(2,10) == True)
    assert(isFactor(7,10) == False)
    print("Problem 6 all tests passed")
test_isFactor()
print('-----------------------------------------------------')

#problem 7

def isMultiple(m,n):
    if (m%n == 0): 
        return True
    else: 
        return False 
def test_isMultiple():
    assert(isMultiple(20,10) == True)
    assert(isMultiple(10,20) == False)
    print("Problem 7 all test passed")
test_isMultiple()
print('-----------------------------------------------------')

print("problem 8 = problem 1")

print('-----------------------------------------------------')

#problem 9
        
def isLegalTriangle(s1, s2, s3):
    if (s1<0) or (s2<0) or (s3<0): return None
    elif ((s1 + s2) > s3) and ((s2 + s3)>s1) and ((s1+s3)>s2): return True 
    else: return False  

def test_isLegalTriangle():
    assert(isLegalTriangle(2,-1,3) == None)
    assert(isLegalTriangle(2,0,3) == False) 
    assert(isLegalTriangle(2,6,5) == True)
    assert(isLegalTriangle(2,6,3) == False)
    print("Problem 9 all test passed")

test_isLegalTriangle()    
print('-----------------------------------------------------')

#problem 10

def triangleArea(s1, s2, s3):
    s = (s1 + s2 + s3)/2
    return (s * (s - s1) * (s - s2) * (s - s3))**0.5
def test_triangleArea():
    assert(triangleArea(12,14,15) == 78.92678569408487)
    assert(triangleArea(1,2,3) == 0)
    print("Problem 10 all test passed")
test_triangleArea()
print('-----------------------------------------------------')

#problem 11

def triangleArea(x1, y1, x2, y2, x3, y3):
    s1 = ((y2-y1)**2+(x2-x1)**2)**0.5
    s2 = ((y3-y1)**2+(x3-x1)**2)**0.5
    s3 = ((y3-y2)**2+(x3-x2)**2)**0.5
    s = (s1 + s2 + s3)/2
    return (s * (s - s1) * (s - s2) * (s - s3))**0.5
def test_triangleArea():
    assert(triangleArea(0,0,5,5,0,5) == 12.5)
    print("Problem 11 all test passed")

test_triangleArea()
print('-----------------------------------------------------')

#problem12


def lineIntersect(m1, b1, m2, b2):
     if (m1 == m2): 
         return None  
     if (m1 != m2):
         x = (b2-b1)/(m1-m2)
         return x
def test_lineIntersect():
    assert(lineIntersect(0,1,-10,5) == 0.4)
    assert(lineIntersect(0,1,0,5) == None)
    assert(lineIntersect(0,1,0,1) == None)
    print("Problem 12 all tests passed")
test_lineIntersect()
print('-----------------------------------------------------')

#problem 13
'''
m1 = int(input("m1="))
b1 = int(input("b1="))
m2 = int(input("m2="))
b2 = int(input("b2="))
m3 = int(input("m3="))
b3 = int(input("b3="))

def threeLinesArea(m1, b1, m2, b2, m3, b3):
    if ((m1 == m2) or (m2 == m3) or (m1 == m3)):
        return None
    else: 
        x1 = (b2-b1)/(m1-m2)
        x2 = (b3-b2)/(m2-m3)
        x3 = (b3-b1)/(m1-m3)
        return x1 
        return x2
        return x3
        
        def triangleArea(m1, b1, m2, b2, m3, b3):
             y1 = (m1*x1) + b1
             y2 = (m2*x2) + b2
             y3 = (m3*x3) + b3
             s1 = ((y2-y1)**2+(x2-x1)**2)**0.5
             s2 = ((y3-y1)**2+(x3-x1)**2)**0.5
             s3 = ((y3-y2)**2+(x3-x2)**2)**0.5
             s = (s1 + s2 + s3)/2
             return (s * (s - s1) * (s - s2) * (s - s3))**0.5

print(threeLinesArea(m1, b1, m2, b2, m3, b3))
'''
#problem 14
# Function for nth Fibonacci number 


def Fibonacci(n): 
    if n<0: 
        print("Incorrect input") 
    elif n==1: 
        return 0
    elif n==2: 
        return 1
    else: 
        return Fibonacci(n-1)+Fibonacci(n-2) 
def test_Fibonacci():
    assert(Fibonacci(2) == 1)
    assert(Fibonacci(4) == 2)
    assert(Fibonacci(8) == 13)
    print("Problem 14 all test passed")
test_Fibonacci()  
print('-----------------------------------------------------')


#problem 15

a = input("Enter a number: ")
import string

def isEvenPositiveInt(x):
    s = "" # declaring empty variable string
    for i in x: # looping through x all string characters ("10" = '1', '0')
        if i in string.digits: # string.digits = "0123456789"
            s += i
        else:
            return False # if input contains non-integer, function ends here
    s = int(s)
    if s > 0 and s % 2 == 0: return True
    else: return False
        

print(isEvenPositiveInt(a))
print('-----------------------------------------------------')

#problem 16

def nearestBusStop(s): 
    return ((s+3)//8)*8

def test_nearestBusStop():
    assert(nearestBusStop(0) == 0)
    assert(nearestBusStop(8) == 8)
    assert(nearestBusStop(12) == 8)
    assert(nearestBusStop(13) == 16)
    print("Problem 16 all test passed")

test_nearestBusStop()
print('-----------------------------------------------------')

#problem 17

def numberOfPoolBalls(r):
    return (r*(r + 1))/2

def test_numberOfPoolBalls():
    assert(numberOfPoolBalls(1) == 1)
    assert(numberOfPoolBalls(2) == 3)
    assert(numberOfPoolBalls(3) == 6)
    print("Problem 17 all test passed")

test_numberOfPoolBalls()

print('-----------------------------------------------------')

#problem 18
a = int(input("Enter number of balls: "))
import math
def numberOfPoolBallRows(b):
    return math.ceil((-1 + math.sqrt(1 + 8 * b)) / 2)


    

print(numberOfPoolBallRows(a)) 