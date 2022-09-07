# for i in range(4):
#     for j in range(4-i):
#         print('Jesus ', end='')
#     print()

# print(list(range(4)))

nums = [2, 4, 10, 43, 15,32]
for num in nums:
    if num % 5 ==0:
        print(num)
        break
else:
    print('not found')
    