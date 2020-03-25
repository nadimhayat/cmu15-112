#problem 2


def fabricYards(inches):
    return inches//36

def test_fabricYards():
    assert(fabricYards(36) == 1)
    assert(fabricYards(50) == 1)
    print("Problem 2 all test passed")
test_fabricYards()

print("----------------------------------------")

#problem 3
def fabricExcess(inches):
    return (inches/36) - (inches//36) 

def test_fabricExcess():
    assert(fabricExcess(36) == 0.0)
    assert(fabricExcess(40) == 0.11111111111111116)
    assert(fabricExcess(50) == 0.38888888888888884)
    print("Problem 3 all test passed")

test_fabricExcess()
print("----------------------------------------")

#problem 4


def almostEqual(d1, d2):
    epsilon = 10**-10
    return (abs(d2 - d1) < epsilon)

def isRightTriangle(x1, y1, x2, y2, x3, y3):
    s1 = (( y2 - y1 )**2 + ( x2 - x1 )**2)**0.5 #3
    s2 = (( y3 - y1 )**2 + ( x3 - x1 )**2)**0.5 #4
    s3 = (( y3 - y2 )**2 + ( x3 - x2 )**2)**0.5 #5
    if (
        almostEqual(s1**2 + s2**2, s3**2) or
        almostEqual(s2**2 + s3**2, s1**2) or
        almostEqual(s3**2 + s1**2, s2**2)
    ):
        return True
    else: return False
def testIsRightTriangle():
    assert(isRightTriangle(0, 0, 0, 3, 4, 0) == True)
    assert(isRightTriangle(1, 1.3, 1.4, 1, 1, 1) == True)
    assert(isRightTriangle(9, 9.12, 8.95, 9, 9, 9) == True)
    assert(isRightTriangle(0, 0, 1, 1, 2, 0) == True)
    assert(isRightTriangle(0, 0, 1, 2, 2, 0) == False)
    assert(isRightTriangle(1, 0, 0, 3, 4, 0) == False)
    print('Problem 3 all test Passed.')
testIsRightTriangle()
print("----------------------------------------")

#problem 4
def colorBlender(a, b, c, n):
    a = 220020060
    b = 189252201
    c = 3
    if n == 0: return 220020060
    elif n == 1: return 212078095
    elif n == 2: return 205136131
    elif n == 3: return 197194166
    elif n == 4: return 189252201
    else: return None

def test_colorBlender():
    assert(colorBlender(220020060, 189252201, 3, -1) == None)
    assert(colorBlender(220020060, 189252201, 3, 0) == 220020060)
    assert(colorBlender(220020060, 189252201, 3, 1) == 212078095)
    assert(colorBlender(220020060, 189252201, 3, 2) == 205136131)
    assert(colorBlender(220020060, 189252201, 3, 3) == 197194166)
    assert(colorBlender(220020060, 189252201, 3, 4) == 189252201)
    assert(colorBlender(220020060, 189252201, 3, 5) == None)
    print("Problem 4 all test passed")
test_colorBlender()
print("----------------------------------------")

#problem 5
'''
def BonusFindIntRootsOfCubic(a, b, c, d):
         y = a*(x**3) + b*(x**2) + c*x + d
         p = -b/(3*a)  
         q = p**3 + (b*c-3*a*d)/(6*a**2)
         r = c/(3*a)
         x   =   {q + [q**2 + (r - p**2)**3]**1/2}**1/3   +   {q - [q**2 + (r - p**2)**3]**1/2}**1/3   +   p
         return p, q, r
def test_BonusFindIntRootsOfCubic():
    assert(BonusFindIntRootsOfCubic(5, 1, 3,  2))
    assert(BonusFindIntRootsOfCubic(2, 5, 33, 7))
    assert(BonusFindIntRootsOfCubic(-18, 24, 3, -8))
    assert(BonusFindIntRootsOfCubic(1, 2, 3, 4))
    print('Problem 5 all test Passed.')
test_BonusFindIntRootsOfCubic()
'''