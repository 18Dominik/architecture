# A usage or delegation is a method or function call that originiates in one component and is handled by another

## 1. Very bad: Component 'Car' uses some interal details of Component 'Engine'. If these details of 'Engine' are ever modified, then 'Car' is likely to break


class Engine:
    def start(self):
        print("Engine starts")
    

class Car:
    '''
    The Car class has a tight coupling with the Engine class. 
    It creates an instance of the Engine class inside its constructor and directly calls the start method of the Engine instance within its own start method.
    '''
    def __init__(self):
        self.engine = Engine() # Car class tightly couples itself to the Engine class.  If you were to change the Engine class or use a different engine type, you would need to modify the Car class. This makes the code less flexible and harder to maintain. 
    
    def start(self):
        print("Car is starting the engine")
        self.engine.start()
            

# Usage
## Creating a car instance
my_car = Car()

## Starting the car
my_car.start()


###########

## 2: Better: Dependency Injection (DI) allows you to inject a specific engine into the Car class, reducing the coupling and making it easier to replace or extend components without modifying the Car class.


class Engine1:
    def start(self):
        print("Engine starts")

class Car1:
    def __init__(self, engine): # Instead of tightly coupling the Car class with the Engine class, we use Dependency Injection. The Car class's constructor takes an instance of the Engine class as a parameter.
        self.engine = engine

    def start(self):
        print("Car is starting the engine")
        self.engine.start()

# Usage
## Creating an Engine instance
car_engine = Engine1() # We create an Engine instance separately and inject it into the Car instance when we create the Car.

## Creating a Car instance and injecting the Engine instance
my_car = Car1(car_engine)

## Starting the car
my_car.start()
   
