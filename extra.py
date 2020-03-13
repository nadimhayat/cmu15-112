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


