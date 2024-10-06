# 9-6 
class Restaurant():
    """A class describing the resturant"""
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restuarnt(self):
        """Prints the info of the restaurant"""
        print(f"Restaurant name: {self.restaurant_name.title()}")
        print(f"Cuisine type: {self.cuisine_type.title()}")

    def open_restaurant(self):
        """Prints when the restaurant opens"""
        print(f"{self.restaurant_name} opens at 9 AM.")

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors
    
    def display_flavor(self):
        print("We have the following falvors:")
        for flavor in self.flavors:
            print(f"- {flavor.title()}.")

icecream = IceCreamStand('sweet treat', 'ice cream', ['vanilla', 'chocolate', 'mint'])

icecream.describe_restuarnt()
icecream.display_flavor()