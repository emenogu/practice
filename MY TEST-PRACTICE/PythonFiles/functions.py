""""
Docstring for this module
This is where you write important comments 
relevant to be known and other documentation

When importing this module somewhere else, 
you can read up this documentation/comments using 
help(this file name or function name)

"""

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
        
person(Name= 'Emenogu Uchenna', Age= 20, RegNo= '15/CS/MB/962', Dept= 'Medicine & Surgery')
    
# greet()
# result1, result2 = add_sub(4,6)
# print()
# print('Addition is:', result1)
# print('Subtraction is:', result2)
# print()
# a=10
# update(a)
# print(id(a))
# print(update('a is', a))


