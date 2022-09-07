
# Generating 10 perfect squares
def toptenGen():
    n = 1
    while n <= 10:
        sq = n*n
        yield sq
        n += 1
        
values = toptenGen()

for i in values:
    print(i)
    

    
print(6&4)
