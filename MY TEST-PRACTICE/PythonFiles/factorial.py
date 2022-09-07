
#Recursion. A recursive function is that which calls/repeats itself

def factorial(num):
    if num == 1:
        return num
    else:
        return num * factorial(num-1)
        
def to_get(key):
    for i in l:
        if i == key:
            print(key, 'is found')
        else:
            print(key, 'not found')
            break

#Peradventure, this module is imported anywhere outside here, 
# the statement will not execute outside
if __name__ == '__main__':    
    l = [2,4,6,8,10,12,14,16,18,20]       

     


    
    

result = factorial(5)
print(result)

result2 = to_get(100)