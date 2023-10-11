# Demonstrating the SOLID Principles
# Single Responsibility Principle/Separation of Concern Principle: -> a component/class should only have ONE reason to change


class Meal:
    """
    class Meal with input title (name), price and taxrate
    """

    def __init__(self, title, price, taxrate):
        self.title = title
        self. price = price
        self.taxrate = taxrate

    def calctax(self):
        """
        calcualate tax
        """
        tax = self.price * self.taxrate
        return tax

### Example Usage ###
pizza = Meal("Pizza", 10, 0.19)

print(pizza.calctax())
print(pizza.title)

# %s for string, %d for integer, %f for floating-point number
print("The tax for meal %s with net price %d Euro plus %.2f taxrate is %.2f." % (
    # option 1 string formatting: %
    pizza.title, pizza.price, pizza.taxrate, pizza.calctax()))
print(f"The tax for meal {pizza.title} with net price {pizza.price} Euro plus {
      pizza.taxrate} taxrate is {pizza.calctax()}")  # otion 2 string formatting: f-string

# The problem with this class Meal in terms of single responsibility principle is: it mixex constant and internally set meal attributes (title, price) with dynamic and externally set meal attributes (taxrate). We want to avoid chaning the whole meal class whenever a taxrate changes or the tax calculation changes a whole. Therefore we separate tax calculation and meal class.
###############################
#Singe Responsibility Principle
###############################
class Meal1:
    """
    class Meal1 with input title (name), price - but this time without taxrate
    """

    def __init__(self, title, price):
        self.title = title
        self. price = price

    def getPrice(self):
        """
        return price for encapsulating the function for tax calculation
        """
        return self.price
        
    def getTitle(self):
        """
        return title for encapsulating the function for tax calculation
        """
        return self.title
 
class TaxCalculator:
    """
    class TaxCalculator encapsulates tax calculation from Meal class to fulfill Single Responsibility Principle in SOLID
    """
    def __init__(self, meal, tax_rates):
        """
        Initialize the TaxCalculator with a meal and tax_rates.
        """
        self.meal = meal
        self.tax_rates = tax_rates  # TaxRates dictionary should be provided as an argument

    def calctax(self):
        """
        Calculate tax based on getPrice function from class Meal1 and tax rates.
        """
        tax_rate = TaxRates[self.meal.getTitle()] # Get the tax rate from the dictionary
        tax = self.meal.getPrice() * tax_rate
        return tax

# Define a dictionary of tax rates
TaxRates = {"Pizza": 0.2, "Burger": 0.1}

### Example of usage
meal1 = Meal1("Burger", 10)
calculator = TaxCalculator(meal1, TaxRates)
tax = calculator.calctax()
print("Tax:", tax)