

x = [4, 6, 7, 8, 24]
y = range(0,100,10)
key = 20

sum = 0
for n in x:
    sum = sum + n
    print(sum, end=', ')
print()
print('>>>')
print()


for index,value in enumerate(x):
    # print(index, n)
    if value==key:
        print('Element', key, 'found at index', index)
        break
    else:
        continue
        # print('Statement after')
else:
    print('Element', key, 'not found')
    
print(len(x))
print()

d= x.append(79)
x.add(86)
print(x)

## REVERSE
def reverse_val(value):
    reverse = value[::-1]
    print('The reverse of', value, 'is', reverse)
    print('There are', len(reverse), 'numbers present')

s= 'python'

result = reverse_val(s)