# By defining an abstract base class, you can define a common Application Program Interface(API) for a set of subclasses. 
# This capability is especially useful in situations where a third party is going to provide implementations, 
# such as with plugins, but can also help you when working in a large team or with a large code base where keeping all classes in your mind is difficult or not possible. 


# An abstract class can be considered a blueprint for other classes. 
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