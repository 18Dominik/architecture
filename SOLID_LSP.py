# Demonstrating the SOLID Principles
## Liskov Substitution Principle (LSP): Promote consistency and conceptual integrity. Simply, inherited and superclass objects should be interchangeable
## -> So, the methods in derived classes should at least do their super methods.

class Employee:
    """
    the super class defines the methods which are available for all child classes
    """
    def __init__(self, name, id):
        self.name = name
        self.id = id

class FullTimeEmployee(Employee):
    """
    FullTimeEmployee is child class of parent Employee
    """
    def __init__(self, name, id, salary, taxrate):
        """
        Only child-class specific modifications, but the initialization of the super class is available for the child class
        """
        super().__init__(name, id) #FullTimeEmployee class takes the same method (here for initialization) as super class Employee
        self.salary = salary
        self.taxrate = taxrate

    def tax_calc(self):
        tax = self.salary * self.taxrate  
        return tax

#Usage

bob = FullTimeEmployee("bob", 1, 1500, 0.3) # We can access the initializiation method of the super class by using inheritance. 
print (f" {bob.name} with employee id {bob.id} has gross {bob.salary} Euro income which is taxed by {bob.taxrate}, which is in total  {bob.tax_calc()} Euro.")
