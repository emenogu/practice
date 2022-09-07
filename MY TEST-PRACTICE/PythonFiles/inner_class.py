class student:
    def __init__(self, name, regNo):
        self.name = name
        self.regNo = regNo
        self.lap = self.laptop
        
    def show(self):
        print(self.name, self.regNo)
        #self.lap.show()
        
    class laptop:
        def __init__(self):
            self.brand = 'Hp'
            self.cpu = 'i5'
            self.ram = 4
        def show(self):
            print(self.brand, self.cpu, self.ram)
            

s1 = student('Emenogu', 6)
s2 = student('Uchenna', 8)
s1.show()
s2.show()
lap1 = student.laptop()
