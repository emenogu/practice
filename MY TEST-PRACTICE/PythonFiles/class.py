class computer:
  def config(self):
      print('core i5 6th Gen, 12gb RAM, 500GB HDD')
#   special methods
  def __init__(self):
      print('Print init')    
  
class owner:
    def config(self):
        print('It belongs to Emenogu Uchenna Chisom')
    
    
com1 = computer()
com2 = owner()

# computer.config(com1)
com1.config()
com2.config()
print()





#   Special methods using __init__
class computer:
  def __init__(self, cpu, ram):
      self.cpu = cpu
      self.ram = ram
      
  def config(self):
        print('Configuration of this PC is', self.cpu, self.ram)
    
    
com1 = computer('core i5,', '16gb Ram')
com2 = computer('dual core,', '2gb Ram')

# computer.config(com1)
com1.config()
com2.config()
