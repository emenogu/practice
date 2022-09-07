


l = [12, 5, 14, 7, 6, 9, 8, 11, 10]
print('l = ', l)

#MAP FUNCTION
def sqr(num):
    return num**2

# result = map(sqr, l)
# for value in result:
#     print('', value, end='')
# print()    

#OR
l1 = list(map(sqr,l)) #Note that list was used
print('l1 = ', l1)
print()

# OR USING LAMBDA with map()
# syntax lambda arguments : expression
l_1 = list(map(lambda num:num**2 ,l)) #Note that list was used
print('l1 = ', l_1)


### ADDING L TO L1 AND PRINTING AS LIST
def add(l1, l2):
    return l1+l2

result1 = list(map(add, l, l1))    
print('l+l1 = ', result1)
print()


##FILTER
# Syntax >>> filter(names, pattern). 
# Note: name= function while pattern= iterables
def check_num(num):
    if num%2==0:
        return True
    else:
        return False

result2= list(filter(check_num, l))
print('Filtered Even No. = ', result2)
print()

#OR USING LAMBDA
result3= list(filter(lambda num1 : num1%2==0 , l))
result4 = list(filter(lambda num2: num2 %2 !=0, l))
print('FIltered Even No. = ',result3)
print('FIltered Odd No. = ',result4)
print()

##SORTED
#This function sorts the list of values automatically
# syntax >>> sorted(iterable, key=key, reverse=reverse)
l2 = sorted(l)
print(l2)
print()


###
# Sorting a dictionary
# Syntax  >> sorted(iterable, key=key, reverse=reverse)
l3 = {98:5, 100:2, 99:9, 97:1, 104:8}
print('l3', l3)

l4= sorted(l3)
print('l4 = ',l4)
l5 = sorted(l3.items())
print('l5 = ',l5) #Sorted into a list containing the lists and values of the dictionary
l6 = sorted(l3.items(), key=lambda x:x[1]) # x[0] sorts based on key, x[1] sorts based on value
print('l6 = ', l6)
l7 = dict(sorted(l3.items(), key=lambda x:x[1])) #Presenting as dictionary
print('l7 = ',l7, 'As Dictionary')


