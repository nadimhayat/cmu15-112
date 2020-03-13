

#Problem 1
# Write the function distance(x1, y1, x2, y2) that takes four int or float values x1, y1, x2, y2 that represent the two points 
#(x1, y1) and (x2, y2), and returns the distance between those points as a float.


# a=(int(input("Enter a number: ")))
# b=(int(input("Enter a number: ")))
# c=(int(input("Enter a number: ")))
# d=(int(input("Enter a number: ")))

def distance(x1,y1,x2,y2):
    return ((y1-y2)**2+(x2-x1)**2)**0.5

def test_distance():
    assert(distance(0, 2, 0, 2) == 0)
    assert(distance(0, 0, 4, 0) == 4)
    print("Problem 1 all tests passed!")

test_distance()

print('-----------------------------------------------------')

#Problem 2
#Write the function circlesIntersect(x1, y1, r1, x2, y2, r2) that takes 6 numbers (ints or floats) -- x1, y1, r1, x2, y2, r2 -- 
# that describe the circle centered at (x1,y1) with radius r1, and the circle centered at (x2,y2) with radius r2, 
# and returns True if the two circles intersect and False otherwise.

a=(int(input("Enter x1: ")))
b=(int(input("Enter y1: ")))
c=(int(input("Enter radius1: ")))
d=(int(input("Enter x2: ")))
e=(int(input("Enter y2: ")))
f=(int(input("Enter radius2: ")))

def distance(x1,y1,x2,y2):
    return ((y1-y2)**2+(x2-x1)**2)**0.5

def circlesIntersect(x1,y1,r1,x2,y2,r2):
    DistanceBetweenCircles = distance(x1,y1,x2,y2)
    return (DistanceBetweenCircles <= (r1 + r2))
    
print(circlesIntersect(a,b,c,d,e,f))
print('------------------------------------------------------')

#Problem 3
#getInRange(x, bound1, bound2)

x=int(input('Enter a number: '))
bound1=int(input('Enter Range 1: '))
bound2=int(input('Enter Range 2: '))
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
    
print(getInRange(x, bound1, bound2))
print('------------------------------------------------------')

#problem 4
#eggcartons

e=int(input('Enter the number of eggs: '))
import math
def eggCartons(eggs):
    egg = abs(eggs)
    C = egg//12
    return C
def eggCartons(eggs):
    eggs = abs(eggs)
    return math.ceil(eggs/12)

print(eggCartons(e))

#problem 5
#pascalsTriangleValue(row, col) 


row=int(input("enter a number: "))
col=int(input("enter another number: "))
import math

def pascalsTriangleValue(row, col):
    if ((row < 0) or (col < 0) or (col>row)): return None
    return (math.factorial(row)/(math.factorial(col)*math.factorial(row-col)))
print(pascalsTriangleValue(row,col))

#problem 6
n=int(input('Input a number: '))
f=int(input('Enter another number: '))

def isFactor(f,n):
    if (n%f == 0): return True
    if (n%f != 0): return False 
print(isFactor(f,n))

#problem 7
a = int(input('Input a number: '))
b = int(input('Enter another number: '))

def isMultiple(m,n):
    if (m%n == 0): 
        return True
    else: 
        return False 
print(isMultiple(a,b))

#problem 8 = #problem 1

#problem 9
s1=int(input("Enter side 1: "))
s2=int(input("Enter side 2: "))
s3=int(input("Enter side 3: "))

        
def isLegalTriangle(s1, s2, s3):
    if (s1<0) or (s2<0) or (s3<0):
        print("Enter a positive number")
    if ((s1 + s2) > s3) and ((s2 + s3)>s1) and ((s1+s3)>s2): return True 
    else: return False

print(isLegalTriangle(s1,s2,s3))

#problem 10
a = int(input("Enter side 1: "))
b = int(input("Enter side 2: "))
c = int(input("Enter side 3: "))

def triangleArea(s1, s2, s3):
    s = (s1 + s2 + s3)/2
    return (s * (s - s1) * (s - s2) * (s - s3))**0.5
    

print(triangleArea(a, b, c))

#problem 11
a = int(input("Enter x1: "))
b = int(input("Enter y1: "))
c = int(input("Enter x2: "))
d = int(input("Enter y2: "))
e = int(input("Enter x3: "))
f = int(input("Enter y3: "))

def triangleArea(x1, y1, x2, y2, x3, y3):
    s1 = ((y2-y1)**2+(x2-x1)**2)**0.5
    print("s1 =", s1)
    s2 = ((y3-y1)**2+(x3-x1)**2)**0.5
    print("s2 =", s2)
    s3 = ((y3-y2)**2+(x3-x2)**2)**0.5
    print("s3 =", s3)
    s = (s1 + s2 + s3)/2
    return (s * (s - s1) * (s - s2) * (s - s3))**0.5
    

print(triangleArea(a, b, c, d, e, f))

print (4.24*(4.24-1.41)*(4.24-4.24)*4.24-2.82)
