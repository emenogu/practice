
# print('Code to determine an EVEN or ODD number')
# a = int(input('Enter any Number '))
# b = a%2
# if (b==0):
#     print("Number entered is an EVEN Number")
# else:
#     print("Number entered is an ODD Number")
# print


l = [2, 3,4,5,6,7,8,13,5,8]

for value in l:
    if value<10:
        if value%2==0:
            print(value, 'meets the conditions stated')
        else:
            print(value, 'is an Odd number')
    else:
        print(value, 'is more than 10')
        
            
  
# WHILE LOOP
# x = 1
# i = int(input('How many times do you want to display your name? '))
# while x<= i:
#     print('Emenogu ', end = ' ')
#     y = 1
#     while y <= i:
#         print('Uchenna ', end = '')
#         y = y + 1
#     x = x + 1
# print('Done')

## For Loop
# for x in range(1, 21):
#     if x % 2 != 0:
#         print(x, end=' ')
#     else:
#         print(' Done')

# for x in range(1, 20):
#     if x%2==0:
#         continue
#     # else:
#     print(x)
#     x=x+1
# print('Thank You')