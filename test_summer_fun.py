from datetime import date
from decimal import Decimal
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

c1 = Customer("Jane Doe", Rating.REGULAR)
c2 = Customer("Mike Smith", Rating.SUPER_DUPER)
c2 = Customer("Emily Williams", Rating.FIRST_TIME)

# Example call
price = p1.calculate_price_for_customer(c1, date(2024, 7, 12))



