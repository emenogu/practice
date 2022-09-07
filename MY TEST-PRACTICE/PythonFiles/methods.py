#  class methods 

class student:
    school = 'SolidRock Academy'
    
    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        
    def avg(self):
        return(self.m1+self.m2+self.m3)/3
    
    @classmethod #decorator
    def getSchool(cls):
        return cls.school
    
    def info():
        print('Class A...')
    
s1 = student(23, 46, 74)
s2 = student(53, 24, 52)

print(s1.avg())
print(student.getSchool())
student.info()





#Class----->Objects---->Values