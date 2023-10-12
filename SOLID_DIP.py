# Demonstrating the SOLID Principles
## Dependency Inversion Principle (DIP): DIP advises NOT to depend on low-level details, but rather to dependo n abstractions.
## High-level modules should not depend on low-level modules. Both should depend on abstractions (e.g. interfaces) 

# ###-> client components should depend on abstractions, not on implementers.###

## Abstractions should not depend on details. Specializiations should depend on abstractions.
## Problem: A high-level component that uses functionality frequently depends on an interface defined by a low-level component. However, if something changes in the lower layers of your system, you may need to modify high-level components, which is not desirable at all
## Solution: Instead of provided interface (API), use Service Programming Interface / required interface (SPI) 
## Achieved by: Separate the component's implementation of functionality and its interface for using its functionaities 
## -> The component implements the functionality, but not its interface
## -> Let components who are using the functionality define the interface to use it.
## -> The dependency is inverted to: Components who are offering functionalities depend on componentes who are using functionalities
##promotes loose coupling and emphasizes the use of interfaces or abstract classes to decouple high-level and low-level components.

#Dependecy Injection: 
##The main idea follows the dependency inversion principle.
##Defer dependency-resolution from compile-time to runtime
##In software engineering, dependency injection is a programming technique in which an object or function receives other objects or functions that it requires, 
# as opposed to creating them internally

from abc import ABC, abstractmethod

# Abstraction for SalaryCalculator
class SalaryCalculator(ABC):
    """
    abstract class with an abstract method for calculating an employee's salary.
    """
    @abstractmethod
    def calculate_salary(self, employee):
        pass

"""
We have two low-level modules, FixedSalaryCalculator and HourlySalaryCalculator, which implement the SalaryCalculator interface to provide specific salary calculation methods.
"""
# Low-level module for calculating salaries based on a fixed rate
class FixedSalaryCalculator(SalaryCalculator):
    def calculate_salary(self, employee):
        return 50000  # A fixed salary for all employees

# Low-level module for calculating salaries based on hourly rate and hours worked
class HourlySalaryCalculator(SalaryCalculator):
    def calculate_salary(self, employee):
        return employee.hourly_rate * employee.hours_worked        

# High-level module for managing employees and their salaries
class EmployeeManager:
    """
    The high-level module, EmployeeManager, accepts a SalaryCalculator object in its constructor, making it dependent on the SalaryCalculator interface rather than concrete details.
    The EmployeeManager uses the injected salary_calculator object to calculate an employee's salary. 
    By switching the implementation of salary_calculator, you can easily change how salaries are calculated without modifying the EmployeeManager.
    """
    def __init__(self, salary_calculator):
        self.salary_calculator = salary_calculator

    def calculate_employee_salary(self, employee):
        return self.salary_calculator.calculate_salary(employee)

# Employee class
class Employee:
    def __init__(self, name, hourly_rate=0, hours_worked=0):
        self.name = name
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked            

# This design adheres to the Dependency Inversion Principle, as the high-level module is decoupled from the low-level salary calculation details, 
# and it depends on the SalaryCalculator abstraction. 
# This makes it easy to switch to different salary calculation mechanisms while keeping the high-level module intact.

# Usage
fixed_calculator = FixedSalaryCalculator() #implementation of SalaryCalculator
hourly_calculator = HourlySalaryCalculator() # implementation of SalaryCalculator

employee_manager_fixed = EmployeeManager(fixed_calculator) # composition -> "EmployeeManager" is composite of component "SalaryCalculator" -> can access method "calculate_employee_salary"
employee_manager_hourly = EmployeeManager(hourly_calculator) # composition -> "EmployeeManager" is composite of component "SalaryCalculator" -> can access method "calculate_employee_salary"

employee1 = Employee("Alice") # create an Employee object
employee2 = Employee("Bob", hourly_rate=15, hours_worked=160) # create an Employee object

salary1 = employee_manager_fixed.calculate_employee_salary(employee1) 
salary2 = employee_manager_hourly.calculate_employee_salary(employee2)

print(f"{employee1.name}'s salary: ${salary1}")
print(f"{employee2.name}'s salary: ${salary2}")





#####
#In contrast, the code below contradicts the dependency inversion principle
###
# High-level module for managing employees and their salaries
class EmployeeManager0:
    def __init__(self):
        pass

    def calculate_employee_salary(self, employee):
        return FixedSalaryCalculator0.calculate_salary(employee)  # Directly depending on a specific low-level module

# Low-level module for calculating salaries based on a fixed rate
class FixedSalaryCalculator0:
    @staticmethod
    def calculate_salary(employee):
        return 50000  # A fixed salary for all employees

# Low-level module for calculating salaries based on hourly rate and hours worked
class HourlySalaryCalculator0:
    @staticmethod
    def calculate_salary(employee):
        return employee.hourly_rate * employee.hours_worked

# Employee class
class Employee0:
    def __init__(self, name, hourly_rate=0, hours_worked=0):
        self.name = name
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

# Usage
employee_manager = EmployeeManager0()

employee1 = Employee("Alice")
employee2 = Employee("Bob", hourly_rate=15, hours_worked=160)

salary1 = employee_manager.calculate_employee_salary(employee1)
salary2 = employee_manager.calculate_employee_salary(employee2)

print(f"{employee1.name}'s salary: ${salary1}")
print(f"{employee2.name}'s salary: ${salary2}")

# In this example:

# The high-level module EmployeeManager directly depends on the low-level modules FixedSalaryCalculator and HourlySalaryCalculator for salary calculations. It doesn't use an abstraction or interface (SalaryCalculator), violating the Dependency Inversion Principle.

# The EmployeeManager class directly calls the static methods of the low-level salary calculators, making it tightly coupled to specific implementations.

# This design goes against the Dependency Inversion Principle, as the high-level module directly relies on low-level details, making it less flexible and harder to switch between different salary calculation mechanisms.
