from abc import ABC, abstractmethod

class computer(ABC):
    @abstractmethod
    def process(self):
        pass
    
    
class laptop(computer):
    def process(self):
        print('It is running')
        
#Objects of the above classes
# com = computer()
com1 = laptop()

# com.process()
com1.process()

# abstract method is a method which only has declaration and doesn't have definition.
# a class is called abstract class only if it has at least one abstract method.
# when you inherit a abstract class as a parent to the child class, 
# the child class should define all the abstract method present in parent class.
# if it is not done then child class also becomes abstract class automatically.
# at last, python by default doesn't support abstract class and abstract method,
# so there is a package called ABC(abstract base classes) by which we can make a class or method abstract.
