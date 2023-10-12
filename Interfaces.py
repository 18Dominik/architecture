# Composition vs. Inheritance -> Composition over Inherithance Principle

#In this example, we use inheritance. 
# Both Car and Motorcycle inherit the Engine class. 
# This allows them to access the start method from the Engine class, which is shared among all vehicles. 
# However, this might not be the best approach because not all vehicles should inherit an engine.

class Engine_I:
    def start(self):
        print("Engine started")

class Car_I(Engine_I):
    def drive(self):
        print("Car is driving")

class Motorcycle_I(Engine_I):
    def ride(self):
        print("Motorcycle is riding")

car = Car_I()
car.start()
car.drive()

motorcycle = Motorcycle_I()
motorcycle.start()
motorcycle.ride()
########################
#In this example, we use composition. The Car and Motorcycle classes have an instance of the Engine class as an attribute. 
# This allows them to access the engine's start method by delegating the call to the engine object. 
# This approach provides more flexibility and avoids issues like having an engine for vehicles that shouldn't have one.

class Engine:
    def start(self):
        print("Engine started")

class Vehicle:
    def __init__(self, engine): #here we give an instance of the Engine class
        self.engine = engine

    def start(self):
        self.engine.start()

class Car(Vehicle):
    def drive(self):
        print("Car is driving")

class Motorcycle(Vehicle):
    def ride(self):
        print("Motorcycle is riding")

engine = Engine()
car = Car(engine)
car.start()
car.drive()

motorcycle = Motorcycle(engine)
motorcycle.start()
motorcycle.ride()
