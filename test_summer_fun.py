from datetime import date, datetime
from decimal import Decimal
import pytest
from summer_fun import Customer, Product, Rating

p1 = Product("5901234567890", "Beach Ball",
             "A classic and colorful inflatable ball that's great for beach games like volleyball or simply tossing "
             "around for fun.", Decimal("19.9"))
p2 = Product("8712345678905", "Sandcastle Building Set",
             "A set of plastic shovels, buckets, and molds designed for building elaborate sandcastles and sculptures "
             "on the beach.", Decimal("32.7"))
p3 = Product("9345678901234", "Boogie Board",
             "A lightweight, small surfboard-like float that allows you to catch waves and ride them in shallow "
             "waters, providing hours of fun in the waves.", Decimal("112"), Decimal("0.1"))
p4 = Product("3425345435230", "Aqua-Glider Foam Surfboard Brochure",
             "The Aqua-Glider Foam Surfboard Brochure is not just your ordinary brochure; it's a unique and "
             "interactive beach toy designed for endless fun in the waves. Made from high-quality, buoyant foam "
             "material, this brochure is shaped like a mini surfboard, making it perfect for gliding across the "
             "water's surface. Its compact size and lightweight design make it easy to carry, making it a great "
             "companion for beach trips.", Decimal("0"))

product1 = Product("9780201379624", "IPhone", "Orange", Decimal(19.99), Decimal(0.1))#price 19.99 , base_discount 10%
product2 = Product("4006381333963", "Coffee Beans", "Aromatic", Decimal(19.99), Decimal(0.5))
product3 = Product("7351350379856", "Horse", "Friendly", Decimal(19.99), Decimal(0.01))
product4 = Product("7351350999856", "Straw", "Long", Decimal(19.99), Decimal(0.00))

customer1 = Customer("Szilvi", Rating.REGULAR)
customer2 = Customer("Bob", Rating.REGULAR)
customer3 = Customer("Joy", Rating.SUPER_DUPER)
customer4 = Customer("Dora", Rating.FIRST_TIME)
customer5 = Customer("Rachel", Rating.SUPER_DUPER)
customer6 = Customer("Eric", Rating.FIRST_TIME)

# Example call
price = p1.calculate_price_for_customer(customer1, date(2024, 7, 12))


customer_list = Customer.create_customer_list(customer1, customer2, customer3, customer4, customer5, customer6)
Customer.print_customers(customer_list)

purchase_date = date(2024, 7, 22)  #date object for July 22, 2024
price = product1.calculate_price_for_customer(customer1, purchase_date)#10%discount, Monday, Price:1000, 10%Discount

print(price)


# testing with pytest starts here

#*************NOT FINAL VERSION!!!!*************TEST CASES ARE NOT IMPLEMENTED CORRECTLY******************

#FIRST_TIME CUSTOMER
#First Time customer outside sale period
#Border values: 2024.06.31=MIN
#             : 2024.09.01=MAX

#MIN:
def test_calculate_price_for_first_time_customer_outside_sale_period_MIN():
    # Arrange

    product1 = Product("9780201379624", "IPhone", "Orange", Decimal(19.99), Decimal(0))
    customer1 = Customer("Dora", Rating.FIRST_TIME)
    date_string = "2024-06-31"
    purchase_date_outside_sale_MIN = datetime.strptime(date_string, "%Y-%m-%d").date()

    # Act
    result = product1.calculate_price_for_customer(customer1, purchase_date_outside_sale_MIN)

    # Assert
    assert result == Decimal("19.99"), "First Time customer outside sale period"

#MAX:
def test_calculate_price_for_first_time_customer_outside_sale_period_MAX():
    # Arrange

    product1 = Product("9780201379624", "IPhone", "Orange", Decimal(19.99), Decimal(0))
    customer1 = Customer("Dora", Rating.FIRST_TIME)
    date_string = "2024-09-01"
    purchase_date_outside_sale_MIN = datetime.strptime(date_string, "%Y-%m-%d").date()

    # Act
    result = product1.calculate_price_for_customer(customer1, purchase_date_outside_sale_MIN)

    # Assert
    assert result == Decimal("19.99"), "First Time customer outside sale period"


#First Time customer inside sale period (not Fri/Sat)
#Border values:One date right before Friday:Thursday:11.07.2024,
#              One date right after a saturday, but on a weekday:Monday:15.07.2024

#Before Friday:
def test_calculate_price_for_first_time_customer_inside_sale_period_NOTFriOrSat():
 # Arrange

    product1 = Product("9780201379624", "IPhone", "Orange", Decimal(19.99), Decimal(0))
    customer1 = Customer("Dora", Rating.FIRST_TIME)
    date_string = "2024-07-11"
    purchase_date_outside_sale_MIN = datetime.strptime(date_string, "%Y-%m-%d").date()
  # Act
    result = product1.calculate_price_for_customer(customer1, purchase_date_outside_sale_MIN)

    # Assert
    assert result == Decimal("19.99"), "First Time customer outside sale period"

#After Saturday:
def test_calculate_price_for_first_time_customer_inside_sale_period_NOTFriOrSat():
    # Arrange

    product1 = Product("9780201379624", "IPhone", "Orange", Decimal(19.99), Decimal(0))
    customer1 = Customer("Dora", Rating.FIRST_TIME)
    date_string = "2024-07-15"
    purchase_date_outside_sale_MIN = datetime.strptime(date_string, "%Y-%m-%d").date()

    # Act
    result = product1.calculate_price_for_customer(customer1, purchase_date_outside_sale_MIN)

    # Assert
    assert result == Decimal("19.99"), "First Time customer outside sale period"


#First Time customer inside sale period (Fri/Sat)
#Border values:Friday:26.07.2024,
#              Saturday:17.08.2024
#Friday:
def test_calculate_price_for_first_time_customer_inside_sale_period_Fri():
    # Arrange

    product1 = Product("9780201379624", "IPhone", "Orange", Decimal(19.99), Decimal(0))
    customer1 = Customer("Dora", Rating.FIRST_TIME)
    date_string = "2024-07-26"
    purchase_date_outside_sale_MIN = datetime.strptime(date_string, "%Y-%m-%d").date()

    # Act
    result = product1.calculate_price_for_customer(customer1, purchase_date_outside_sale_MIN)

    # Assert
    assert result == Decimal("19.99"), "First Time customer outside sale period"

#Saturday:
def test_calculate_price_for_first_time_customer_inside_sale_period_Sat():
    # Arrange

    product1 = Product("9780201379624", "IPhone", "Orange", Decimal(19.99), Decimal(0))
    customer1 = Customer("Dora", Rating.FIRST_TIME)
    date_string = "2024-08-17"
    purchase_date_outside_sale_MIN = datetime.strptime(date_string, "%Y-%m-%d").date()

    # Act
    result = product1.calculate_price_for_customer(customer1, purchase_date_outside_sale_MIN)

    # Assert
    assert result == Decimal("19.99"), "First Time customer outside sale period"


#REGULAR CUSTOMER
#Regular customer outside sale period
#Border values: 2024.06.31=MIN
#             : 2024.09.01=MAX
#MIN
def test_calculate_price_for_regular_customer_outside_sale_period_MIN():
    # Arrange

    product1 = Product("9780201379624", "IPhone", "Orange", Decimal(19.99), Decimal(0))
    customer2 = Customer("Bob", Rating.REGULAR)
    date_string = "2024-06-31"
    purchase_date_outside_sale_MIN = datetime.strptime(date_string, "%Y-%m-%d").date()

    # Act
    result = product1.calculate_price_for_customer(customer2, purchase_date_outside_sale_MIN)

    # Assert
    assert result == Decimal("19.99"), "Regular customer outside sale period"

#MAX
def test_calculate_price_for_regular_customer_outside_sale_period_MAX():
    # Arrange

    product1 = Product("9780201379624", "IPhone", "Orange", Decimal(19.99), Decimal(0))
    customer2 = Customer("Bob", Rating.REGULAR)
    date_string = "2024-09-01"
    purchase_date_outside_sale_MIN = datetime.strptime(date_string, "%Y-%m-%d").date()

    # Act
    result = product1.calculate_price_for_customer(customer2, purchase_date_outside_sale_MIN)

    # Assert
    assert result == Decimal("19.99"), "Regular customer outside sale period"


#Regular customer inside sale period (not Fri/Sat)
#Border values:One date right before Friday:Thursday:11.07.2024,
#              One date right after a saturday, but on a weekday:Monday:15.07.2024
#Right before Friday
def test_calculate_price_for_regular_customer_inside_sale_period_NOTFriOrSat():
       # Arrange

    product1 = Product("9780201379624", "IPhone", "Orange", Decimal(19.99), Decimal(0))
    customer2 = Customer("Bob", Rating.REGULAR)
    date_string = "2024-07-11"
    purchase_date_outside_sale_MIN = datetime.strptime(date_string, "%Y-%m-%d").date()

    # Act
    result = product1.calculate_price_for_customer(customer2, purchase_date_outside_sale_MIN)

    # Assert
    assert result == Decimal("19.99"), "Regular customer outside sale period"

#Regular customer inside sale period (Fri/Sat)
#Right after saturday (Weekday:Monday)
def test_calculate_price_for_regular_customer_inside_sale_period_NOTFriOrSat():
       # Arrange

    product1 = Product("9780201379624", "IPhone", "Orange", Decimal(19.99), Decimal(0))
    customer2 = Customer("Bob", Rating.REGULAR)
    date_string = "2024-07-11"
    purchase_date_outside_sale_MIN = datetime.strptime(date_string, "%Y-%m-%d").date()

    # Act
    result = product1.calculate_price_for_customer(customer2, purchase_date_outside_sale_MIN)

    # Assert
    assert result == Decimal("19.99"), "Regular customer outside sale period"

#Regular customer inside sale peirod fri or saturday
#Border values:Friday:26.07.2024,
#              Saturday:17.08.2024
#Friday
def test_calculate_price_for_regular_customer_inside_sale_period_Fri():
         # Arrange

    product1 = Product("9780201379624", "IPhone", "Orange", Decimal(19.99), Decimal(0))
    customer2 = Customer("Bob", Rating.REGULAR)
    date_string = "2024-07-26"
    purchase_date_outside_sale_MIN = datetime.strptime(date_string, "%Y-%m-%d").date()

    # Act
    result = product1.calculate_price_for_customer(customer2, purchase_date_outside_sale_MIN)

    # Assert
    assert result == Decimal("19.99"), "Regular customer outside sale period"

#Saturday
def test_calculate_price_for_regular_customer_inside_sale_period_Fri():
         # Arrange

    product1 = Product("9780201379624", "IPhone", "Orange", Decimal(19.99), Decimal(0))
    customer2 = Customer("Bob", Rating.REGULAR)
    date_string = "2024-08-17"
    purchase_date_outside_sale_MIN = datetime.strptime(date_string, "%Y-%m-%d").date()

    # Act
    result = product1.calculate_price_for_customer(customer2, purchase_date_outside_sale_MIN)

    # Assert
    assert result == Decimal("19.99"), "Regular customer outside sale period"

#Super-Duper Customer
#Super Duper customer outside sale period
#Border values: 2024.06.31=MIN
#             : 2024.09.01=MAX
#MIN
def test_calculate_price_for_superDuper_customer_outside_sale_period_MIN():
    # Arrange

    product1 = Product("9780201379624", "IPhone", "Orange", Decimal(19.99), Decimal(0))
    customer3 = Customer("Joy", Rating.SUPER_DUPER)
    date_string = "2024-06-31"
    purchase_date_outside_sale_MIN = datetime.strptime(date_string, "%Y-%m-%d").date()

    # Act
    result = product1.calculate_price_for_customer(customer3, purchase_date_outside_sale_MIN)

    # Assert
    assert result == Decimal("19.99"), "Super-Duper customer outside sale period"

#MAX
def test_calculate_price_for_superDuper_customer_outside_sale_period_MAX():
    # Arrange

    product1 = Product("9780201379624", "IPhone", "Orange", Decimal(19.99), Decimal(0))
    customer3 = Customer("Joy", Rating.SUPER_DUPER)
    date_string = "2024-09-01"
    purchase_date_outside_sale_MIN = datetime.strptime(date_string, "%Y-%m-%d").date()

    # Act
    result = product1.calculate_price_for_customer(customer3, purchase_date_outside_sale_MIN)

    # Assert
    assert result == Decimal("19.99"), "Super-Duper customer outside sale period"


#Regular customer inside sale period (not Fri/Sat)
#Border values:One date right before Friday:Thursday:11.07.2024,
#              One date right after a saturday, but on a weekday:Monday:15.07.2024
#Right before Friday
def test_calculate_price_for_superDuper_customer_inside_sale_period_NOTFriOrSat():
       # Arrange

    product1 = Product("9780201379624", "IPhone", "Orange", Decimal(19.99), Decimal(0))
    customer3 = Customer("Joy", Rating.SUPER_DUPER)
    date_string = "2024-07-11"
    purchase_date_outside_sale_MIN = datetime.strptime(date_string, "%Y-%m-%d").date()

    # Act
    result = product1.calculate_price_for_customer(customer3, purchase_date_outside_sale_MIN)

    # Assert
    assert result == Decimal("19.99"), "Super-Duper customer outside sale period"

#Regular customer inside sale period (Fri/Sat)
#Right after saturday (Weekday:Monday)
def test_calculate_price_for_regular_customer_inside_sale_period_NOTFriOrSat():
       # Arrange

    product1 = Product("9780201379624", "IPhone", "Orange", Decimal(19.99), Decimal(0))
    customer3 = Customer("Joy", Rating.SUPER_DUPER)
    date_string = "2024-07-11"
    purchase_date_outside_sale_MIN = datetime.strptime(date_string, "%Y-%m-%d").date()

    # Act
    result = product1.calculate_price_for_customer(customer3, purchase_date_outside_sale_MIN)

    # Assert
    assert result == Decimal("19.99"), "Super-Duper customer outside sale period"

#Regular customer inside sale peirod fri or saturday
#Border values:Friday:26.07.2024,
#              Saturday:17.08.2024
#Friday
def test_calculate_price_for_superDuper_customer_inside_sale_period_Fri():
         # Arrange

    product1 = Product("9780201379624", "IPhone", "Orange", Decimal(19.99), Decimal(0))
    customer3 = Customer("Joy", Rating.SUPER_DUPER)
    date_string = "2024-07-26"
    purchase_date_outside_sale_MIN = datetime.strptime(date_string, "%Y-%m-%d").date()

    # Act
    result = product1.calculate_price_for_customer(customer3, purchase_date_outside_sale_MIN)

    # Assert
    assert result == Decimal("19.99"), "Super-Duper customer outside sale period"

#Saturday
def test_calculate_price_for_superDuper_customer_inside_sale_period_Fri():
         # Arrange

    product1 = Product("9780201379624", "IPhone", "Orange", Decimal(19.99), Decimal(0))
    customer3 = Customer("Joy", Rating.SUPER_DUPER)
    date_string = "2024-08-17"
    purchase_date_outside_sale_MIN = datetime.strptime(date_string, "%Y-%m-%d").date()

    # Act
    result = product1.calculate_price_for_customer(customer3, purchase_date_outside_sale_MIN)

    # Assert
    assert result == Decimal("19.99"), "Super-Duper customer outside sale period"


