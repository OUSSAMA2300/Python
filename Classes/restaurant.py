# 9-1
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

restaurant = Restaurant('The Bear', 'Italian')

restaurant.describe_restuarnt()

print(f"\n{restaurant.restaurant_name} is amazing.")
print(f"{restaurant.cuisine_type} cuisine is so good.")

restaurant.open_restaurant()

# 9-2
print('\n')

restaurant = Restaurant('nobu', 'japanese')
restaurant.describe_restuarnt()
print('\n')

restaurant = Restaurant('taco bell', 'mexican')
restaurant.describe_restuarnt()
print('\n')

restaurant = Restaurant('le bernardin', 'french')
restaurant.describe_restuarnt()