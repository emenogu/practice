# Function to calculate factorial
def fact(n):
    if n==0:
        return 1
    return n * fact(n-1)

def greet():
    print('Good Morning')
    print('Hi, How are you?')
    print('How may I help you, please?')
    
def add_sub(a, b):
    c = a+b
    d = a-b
    return c, d ##Here, we are returning two values c and d
    
def update(x):
    x = 8
    print(x)

def person(**data):
    # print(name)
    for i, j in data.items():
        print(i, ':', j)
 
# Fibonacci function       
def fib(n):
    a=0
    b=1
    if n<1:
        print("Invalid Number")
    else:
        print(a)
        print(b)
        
        for i in range(2,n):
            c=a+b
            print(c)
            a=b
            b=c

