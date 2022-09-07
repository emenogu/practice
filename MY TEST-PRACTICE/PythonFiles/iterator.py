nums = [3, 5, 6, 7, 9]


# for i in nums:
#     print(i)
# print()
# print(nums[3])

it = iter(nums)
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())

# print(next(it))
print()


## ITERATORS
class iterators:
    def __init__(self):
        self.num = 1
        
    def __iter__(self):
        return self
    def __next__(self):
        if self.num <= 10:
            val = self.num
            self.num += 1
            return val
        else:
            raise StopIteration
        
values = iterators()  #This is the object of class iterators
# print(next(values))
# print(next(values))
# print(next(values))

for i in values:
    print(i, end=' ')
