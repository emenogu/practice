class laptop:
    def code(self, ide):
        ide.execute()
        
class pycharmide:
    def execute(self):
        print('Compiling')
        print('Running')

class rockide:
    def execute(self):
        print('Spell check')
        print('Convention check')
        print('Compiling')
        print('Running')

#Method Overloading (Polymorphism)
class student:
    def sum(self, a=None, b=None, c=None):
        s = 0
        if a!=None and b!=None and c!=None:
            s = a + b + c
        elif a!=None and b!=None:
            s = a + b
        else:
            s = a
        return s
    
#Method Oveririding (Polymorphism)
class A:
    def show(self):
        print('In A show')
class B(A): #Class A is effected cause B has no method(functiob)
    pass
class C(A): #Class A has a method(function) so, it overides Class A
    def show(self):
        print('In B show')
        

ide = rockide()
lap1 = laptop()        
s1 = student()
a1 = A()
b1 = B()
c1 = C()

lap1.code(ide)
print()

print(s1.sum(4, 9, 7))
a1.show()
b1.show()
c1.show()