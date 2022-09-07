

#Here, Class A is the super class
class A:
    def __init__(self):
        print('Batch 13')
        
    def name1(self):
        print('Emenogu Uchenna Chisom')
    
    def profession1(self):
        print('Medical Doctor')

#Here, Class B is a subclass of A 
class B(A):
    def __init__(self):
        super().__init__() 
        #super() funtion would call both Class B and its Super class A
        print('Batch 14')
    def name2(self):
        print('Aniebiet Ufiah')
    def profession2(self):
        print('Physics Lecturer')
        
class C():
    def name3(self):
        print('Idongesit Ubon')
    def profession3(self):
        print('Intra-thoracic Surgeon')


#Class D is a subset of class C and A
#According to the Method_Resolution_Order,
#Here, preference is taken from the left of (C, A)
#Preference is given to C which comes first from the left        
class D(C, A):
    def __init__(self):
        super().__init__()
        print('Batch 15')
    def name4(self):
        print('Vincent Mercy')
    def profession4(self):
        print('Cinematographer')

#Objects of the declared classes
a1 = A(); b1 = B()
c1 = C(); d1 = D()

#
a1.name1()
a1.profession1()
print()

b1.name2()
b1.profession2()
print()

c1.name3()
c1.profession3()
print()

d1.name4