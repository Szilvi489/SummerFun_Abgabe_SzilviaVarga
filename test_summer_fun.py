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

def test_calculate_price_for_customer():

    #SETTING UP TEST DATA
    # a product with the price: 19.99, and a 10% base discount
    p1 = Product("9780201379624", "IPhone", "Orange", Decimal(19.99), Decimal(0.1))

    # the different rating test cases
    purchase_date = date(2024, 7, 22)  #date object for July 22, 2024

    #customers with different ratings
    customer1 = Customer("Dora", Rating.FIRST_TIME)
    customer2 = Customer("Szilvi", Rating.REGULAR)
    customer3 = Customer("Rachel", Rating.SUPER_DUPER)

    assert p1.calculate_price_for_customer(customer1, date(2024, 6, 12)) == Decimal("19.9")  #                   test case 1
    assert p1.calculate_price_for_customer(customer1, date(2024, 7, 12)) == Decimal("19.9") * Decimal("0.95")  #           2
    assert p1.calculate_price_for_customer(customer1, date(2024, 7, 12)) == Decimal("19.9") * Decimal("0.90")  #           3
    assert p1.calculate_price_for_customer(customer2, date(2024, 6, 12)) == Decimal("19.9")  #                             4
    assert p1.calculate_price_for_customer(customer2, date(2024, 7, 12)) == Decimal("19.9") * Decimal("0.90")  #           5
    assert p1.calculate_price_for_customer(customer2, date(2024, 7, 12)) == Decimal("19.9") * Decimal("0.80")  #           6
    assert p1.calculate_price_for_customer(customer3, date(2024, 6, 12)) == Decimal("19.9")  #                             7
    assert p1.calculate_price_for_customer(customer3, date(2024, 7, 12)) == Decimal("19.9") * Decimal("0.85")  #           8
    assert p1.calculate_price_for_customer(customer3, date(2024, 7, 12)) == Decimal("19.9") * Decimal("0.70")  #           9

    # Test cases with invalid inputs
    with pytest.raises(ValueError):
        p1.calculate_price_for_customer("Invalid Customer", date(2024, 7, 12))  # Test case 10
    with pytest.raises(ValueError):
        p1.calculate_price_for_customer(customer1, "Invalid Date")  #                       11




def test_calculate_price_for_first_time_customer_outside_sale_period():
    # Arrange

    product1 = Product("9780201379624", "IPhone", "Orange", Decimal(19.99), Decimal(0.0))
    customer1 = Customer("Dora", Rating.FIRST_TIME)
    date_string = "2024-06-30"
    purchase_date_outside_sale_MIN = datetime.strptime(date_string, "%Y-%m-%d").date()

    # Act
    result = p1.calculate_price_for_customer(customer1, purchase_date_outside_sale_MIN)

    # Assert
    assert result == Decimal("19.9"), "First Time customer outside sale period"

