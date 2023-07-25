import re
from enum import Enum
from decimal import Decimal
from datetime import date
from datetime import date
import calendar

# product: calculate_price_customer is inside in a class.It is inside an object
#they are depending also on how the class object is depicted
#

class Rating(Enum):
    FIRST_TIME = "First time"
    REGULAR = "Regular"
    SUPER_DUPER = "Super-duper"

    def __str__(self):
        return self.name


class Customer:
    def __init__(self, name: str, rating: Rating):
        if not isinstance(name, str):
            raise ValueError(f"Customer name must be a string.")
        if len(name) == 0:
            raise ValueError(f"Customer name must be non-empty.")
        if not isinstance(rating, Rating):
            raise ValueError(f"Customer rating must be of type Rating, but is of type {type(rating)}.")

        self.name = name
        self.rating = rating

    def __str__(self):
        return f"{self.name} ({self.rating})"


class Product:
    _EAN_PATTERN = re.compile(r"^\d{13}$")

    def __init__(self, ean: str, name: str, description: str, base_price: Decimal, base_discount=Decimal(0)):
        if not Product._EAN_PATTERN.match(ean):
            raise ValueError(f"Given ean {ean} is not valid. An ean has exactly 13 digits.")
        if not isinstance(name, str):
            raise ValueError(f"Product name must be a string.")
        if len(name) == 0:
            raise ValueError(f"Product name must be non-empty.")
        if not (isinstance(description, str) or description is None):
            raise ValueError(f"Product description must be a string or None, but is '{description}'")
        if not isinstance(base_price, Decimal):
            raise ValueError(f"Product base price must be of type Decimal.")
        if not base_price >= 0:
            raise ValueError(f"Product base price must be greater or equal to zero.")
        if not isinstance(base_discount, Decimal):
            raise ValueError(f"Product discount must be of type Decimal.")
        if base_discount < 0 or base_discount > 1:
            raise ValueError(f"Product discount must be between 0 and 1.")

        self.ean = ean
        self.name = name
        self.description = description
        self.base_price = base_price
        self.base_discount = base_discount



    def calculate_price_for_customer(self, customer: Customer, date_of_purchase: date) -> Decimal:
        # Define the discounts
        discount_mapping = {
            Rating.FIRST_TIME: Decimal('0.05'),
            Rating.REGULAR: Decimal('0.10'),
            Rating.SUPER_DUPER: Decimal('0.15'),
        }

        # Get the customer discount
        discount = discount_mapping[customer.rating]

        # Check if the date is in the special summer sale period
        if date_of_purchase.year == 2024 and date_of_purchase.month in [7, 8]:
            # Check if the date is Friday or Saturday
            if date_of_purchase.weekday() in [4, 5]: # 4 and 5 corresponds to Friday and Saturday
                discount *= 2  # double the discount

        # Apply the customer discount on top of the base discount
        price_after_base_discount = self.base_price * (1 - self.base_discount)
        price_after_additional_discount = price_after_base_discount * (1 - discount)

        return price_after_additional_discount


customer1 = Customer("Szilvi", Rating.REGULAR)
customer2 = Customer("Bob", Rating.REGULAR)
customer3 = Customer("Joy", Rating.SUPER_DUPER)
customer4 = Customer("Dora", Rating.FIRST_TIME)
customer5 = Customer("Rachel", Rating.SUPER_DUPER)
customer6 = Customer("Eric", Rating.FIRST_TIME)

#name, description, base price, base discount
product1 = Product("9780201379624", "IPhone", "Orange", Decimal(1000), Decimal(0.1))
product2 = Product("4006381333963", "Coffee Beans", "Aromatic", Decimal(50), Decimal(0.5))
product3 = Product("7351350379856", "Horse", "Friendly", Decimal(13000), Decimal(0.01))
product4 = Product("7351350999856", "Straw", "Long", Decimal(1), Decimal(0.00))

def create_customer_list(*customers):
    return list(customers)

def print_customers(customers):
    for customer in customers:
        print(f"Name: {customer.name}, Rating: {customer.rating}")


customer_list = create_customer_list(customer1, customer2, customer3, customer4, customer5, customer6)

print_customers(customer_list)

purchase_date = date(2024, 7, 22)  #date object for July 22, 2024
price = product1.calculate_price_for_customer(customer1, purchase_date)#10%discount, Monday, Price:1000, 10%Discount

print(price)
