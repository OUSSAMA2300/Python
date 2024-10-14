# 9-4
class Restaurant():
    """A class describing the resturant"""
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0 

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, num_inc):
        self.number_served += num_inc

    def describe_restuarnt(self):
        """Prints the info of the restaurant"""
        print(f"Restaurant name: {self.restaurant_name.title()}")
        print(f"Cuisine type: {self.cuisine_type.title()}")

    def open_restaurant(self):
        """Prints when the restaurant opens"""
        print(f"{self.restaurant_name} opens at 9 AM.")
    
    def served_customers(self):
        print(f"We have served {self.number_served} customers \n")

# First task
restaurant = Restaurant('The Bear', 'Italian')
restaurant.describe_restuarnt()
restaurant.served_customers()

# second adding the method set_number_served
restaurant = Restaurant('nobu', 'japanese')
restaurant.describe_restuarnt()
restaurant.set_number_served(8)
restaurant.served_customers()

# Third adding the incement method 
restaurant = Restaurant('taco bell', 'mexican')
restaurant.describe_restuarnt()
restaurant.set_number_served(8)
restaurant.served_customers()
restaurant.increment_number_served(2)
restaurant.served_customers()