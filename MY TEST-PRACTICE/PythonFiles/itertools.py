

l = [10,20,30,40,50,60]
m = iter(l)

# #syntax for next next(iterable, default)
# print(next(m))
# print(next(m))
# print(next(m))


# for value in l:
#     print(value)

##Using chain command to iterate several lists
##You first need to import itertools to be able to access the chain command
## syntax itertools.chain(iterables)
import itertools
l1 = [2,3,4,5,6,7]
l2 = [20,30,40,50,60,70]
l3 = [10,12,14,16,18,22]
n = itertools.chain(l1,l2,l3)

# print(next(n))
# print(next(n))  ##next() as a generator is used to generate the result one after the other 
# rather than everythng. This saves memory especially in humungous data
## OR
for value in n:
    print(value, sep=',', end=' ')
print()


###
##USING ITERTOOLS REPEAT FUNCTION
count = 0
for value in itertools.repeat(l1):
    if count<5: ##defines the limit on number of times the iterable should be repeated
        print(value)
    else:
        break
    count+=1
    


#### Itertools.chain
# itertools.chain(*iterables)


###Itertools.tee
# Syntax >>> itertools.tee
i = iter(l)
p = itertools.tee(i)


for value in p[0]:
    print(value, end=' ')
print()
 
###Slicing using itertools. As the name implies, it slices desired portions    
### Syntax >>> itertools.islice(iterable, start,stop)    
for value in itertools.islice(l, 1, 5):
    print(value, end=' ')
print()    
    
### 
print('Itertools.count = ')
range(5,100)   
count = 0
for value in itertools.count():
    if count<10:
        print(value, end=' ')
    else:
        break
    count+=1
    
    