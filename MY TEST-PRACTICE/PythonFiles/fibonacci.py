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
        
      
         

fib(9)