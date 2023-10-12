# By defining an abstract base class, you can define a common Application Program Interface(API) for a set of subclasses. 
# This capability is especially useful in situations where a third party is going to provide implementations, 
# such as with plugins, but can also help you when working in a large team or with a large code base where keeping all classes in your mind is difficult or not possible. 


# An abstract class can be considered a blueprint for other classes. An Abstract class cannot be instantiated on its own. 
# Abstract classes can have fields (instance variables) that can be inherited by subclasses.

# There are only slight difference in the terms "Abstract Class" and "Interface". Likely the biggest difference is that abstract classes can have fields (instance variables) and interfaces do not.  
# In an interface you can not implement any of the declared methods. Only the class that "implements" the interface can implement the methods (compare keywords "extends" -> Inheritance and "implements" -> Interface in Java Code).
#"An interface is always an abstract class, but an abstract class is not always an interface."

# It allows you to create a set of methods that must be created within any child classes built from the abstract class. 
# A class that contains one or more abstract methods is called an abstract class. 
# An abstract method is a method that has a declaration but does not have an implementation. 
# While we are designing large functional units we use an abstract class. 
# When we want to provide a common interface for different implementations of a component, we use an abstract class. 
# https://www.geeksforgeeks.org/abstract-classes-in-python/
#Example
from abc import ABC, abstractmethod

class Flour(ABC):
  @abstractmethod
  def make_bread(self):
    print ("this is base bread")

class Toast(Flour):
    # overriding abstract method
  def make_bread(self):
    super().make_bread()
    print ("this is a delicious toast")

#Usage
x = Toast()
x.make_bread()
#========================
#this is base bread
#this is a delicious toast


###
#Another Example#
###
###With Abstract Class###
from abc import ABC, abstractmethod

class Engine:
    def start(self):
        print("Engine started")

class Vehicle(ABC):
    def __init__(self, engine):
        self.engine = engine

    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        self.engine.start()
        print("Car is starting")

    def drive(self):
        print("Car is driving")

class Motorcycle(Vehicle):
    def start(self):
        self.engine.start()
        print("Motorcycle is starting")
    
    def ride(self):
        print("Motorcycle is riding")
#Usage
engine = Engine()
car = Car(engine)
car.start()
car.drive()

motorcycle = Motorcycle(engine)
motorcycle.start()
motorcycle.ride()


###Without Abstract Class and only normal inheritance (super-class, sub-class), this Example looks like:###

class Engine0:
    def start(self):
        print("Engine started")

class Vehicle0:
    def __init__(self, engine):
        self.engine = engine

    def start(self):
        self.engine.start()

class Car0(Vehicle0):
    def drive(self):
        print("Car is driving")

class Motorcycle0(Vehicle0):
    def ride(self):
        print("Motorcycle is riding")

#Usage
engine = Engine()
car = Car0(engine)
car.start()
car.drive()

motorcycle = Motorcycle0(engine)
motorcycle.start()
motorcycle.ride()

