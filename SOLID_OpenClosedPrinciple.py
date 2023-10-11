from abc import ABC, abstractmethod
## Demonstrating the SOLID Principles
### Open-Closed Principle: Components should be open for extension, but closed for modification. You want to be able to EXTEND their functionality WITHOUT modifying the component itself. 
### Achieved by dependency inversion principle/use of dependency injection frameworks & inheritance


"""
In this example, the SalaryCalculator class is responsible for calculating the salary of different staff types, but it violates the Open-Closed Principle because it needs to be modified every time a new staff type is introduced.
"""
class FullTimeEmployee:
    def __init__(self, salary, bonus):
        self.salary = 1000
        self.bonus = 0.5
        self.pension = 2000

class PartTimeEmployee:
    def __init__(self, salary, ):
        self.salary = 500

class SalaryCalculator:
    def calculate_salary(self, type):
        if isinstance(type, FullTimeEmployee):
            return type.salary* (type.bonus+1)
        elif isinstance(type, PartTimeEmployee):
            return type.salary

"""
To make this adherent to the OCP, you can use polymorphism and abstractions
Then, you can extend for additional staff types like contractor etc. and calculate their salarries without having to modify the existing classes.
"""


class Type(ABC):
    @abstractmethod
    """
    In the abstract class, we define the function that is crucial for extending the component "Salary Calculation for various types of staff" 
    """
    def calculate_salary(self):
        pass

class FullTimeEmployee1(Type):
    def __init__(self, salary, bonus):
        self.salary = 1000
        self.bonus = 0.5
        self.pension = 2000

    def calculate_salary(self):
        return self.salary*(1+self.bonus)

class PartTimeEmployee1(Type):
    def __init__(self, salary):
        self.salary = 500

    def calculate_salary(self):
        return self.salary

class SalaryCalculator1:
    def calculate_salary(self, type):
        return type.calculate_salary()      

# Usage
bob = FullTimeEmployee1(9000, 0.2)
alice = PartTimeEmployee1(5000)

calculator = SalaryCalculator1()

salary_bob = calculator.calculate_salary(bob)
salary_alice = calculator.calculate_salary(alice)

print(f"Salary of Bob: {salary_bob}")
print(f"Salary of Alice: {salary_alice}")        