# Coupling via creation (Factory Design Pattern)
## The Factory Method pattern suggests that you replace direct object construction calls with calls to a special factory method (superclass).
## Factory approach provides an interface for creating objects in a superclass, but allows subclasses to alter the type of objects that will be created.

class Vehicle:
    '''
    Base class Vehicle with a method display_info, which will be overridden by the concrete classes.
    '''
    def display_info(self):
        pass

class Car(Vehicle): #inherit from vehicle -> implement display_info()
    def display_info(self):
        return "I am a Car"

class Motorcycle(Vehicle): #inherit from vehicle -> implement display_info()
    def display_info(self):
        return "I am a Motorcycle"

class VehicleFactory:
    '''
    VehicleFactory class is responsible for creating instances of different vehicles based on the vehicle_type provided.
    It encapsulates the object creation logic.
    '''
    def create_vehicle(self, vehicle_type):
        if vehicle_type == "car":
            return Car()
        elif vehicle_type == "motorcycle":
            return Motorcycle()
        else:
            return None

# Client code
factory = VehicleFactory() #In the client code, we create a VehicleFactory instance and use it to create specific vehicle objects, such as a car or a motorcycle.

vehicle1 = factory.create_vehicle("car")
vehicle2 = factory.create_vehicle("motorcycle")

print(vehicle1.display_info())  # Output: I am a Car
print(vehicle2.display_info())  # Output: I am a Motorcycle
