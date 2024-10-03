class Cars:
    """A simple attempt t respresent a car."""

    def __init__(self, make, model, year):
        """Initialze attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    # Modifying an attribute’s Value through a Method
    def update_odometer(self, milage):
        """Set the odometer reading to the given value"""
        if milage >= self.odometer_reading:
           self.odometer_reading = milage
        else:
            print("You can't roll back an odometer!")

    def inc_odometer(slef, miles):
        """(third approach) by increment"""
        """Add the given amount to the odometer reading"""
        if miles > 0:
           slef.odometer_reading += miles
        else:
            print("You can't roll back an odometer or enter negative values") 

    def get_describtive_name(self):
        """Return a neatly foramtted descibtive name"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name    
    
    def read_odometer(self):
        """Print a statment showing the car's milage"""
        print(f"This car has {self.odometer_reading} miles on it.")
    
my_new_car = Cars('audi', 'a4', 2016)
print(my_new_car.get_describtive_name())
my_new_car.read_odometer()

# (first approach) Modifying the value of the instance directly
#  by accessing the attribute
my_new_car.odometer_reading = 32
my_new_car.read_odometer()

# (second approach) By the method 
my_new_car.update_odometer(32)
my_new_car.read_odometer()

# (third)   
my_used_car = Cars('subaru', 'outback', 2013)
print(my_used_car.get_describtive_name())

my_used_car.update_odometer(23500)
my_used_car.read_odometer()

my_used_car.inc_odometer(-100)
my_used_car.read_odometer()