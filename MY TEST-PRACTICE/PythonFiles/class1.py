
class car:
    wheels = 6
    def __init__(self):
        self.mil = 10
        self.com = 'BMW'
        
c1 = car()
c2 = car()

c1.mil = 20  # Instance namespace 
c1.mil = 13
car.wheels = 8 # Class namespace. Stores class variables


print(c1.mil, c1.com, c1.wheels)
print(c2.mil, c2.com, c2.wheels)






# There are 2 types of variables
# 1. Instance variables. Variables created with __init__
# 2. Class varibles. Variables created outside __init__

# Namespace is an area where you create and store an object/variable
# Types: 1. Class namespace. Store class variables
    #  2. Object/Instance namespace. Stores object variables