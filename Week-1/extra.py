# Function for nth Fibonacci number 
'''
a = int(input("Enter the nth number: "))  
def Fibonacci(n): 
    if n<0: 
        print("Incorrect input") 
    # First Fibonacci number is 0 
    elif n==1: 
        return 0
    # Second Fibonacci number is 1 
    elif n==2: 
        return 1
    else: 
        return Fibonacci(n-1)+Fibonacci(n-2) 
  
# Driver Program 
  
print(Fibonacci(a)) 
'''

def	bonusCt2(x,	y):
		return	(x+bonusCt2(x-1,y-1)	if	(y	>	0)	else (2+bonusCt2(x-1,y)	if	(x	>	0)	else	42))
print(bonusCt2(1,	1))
