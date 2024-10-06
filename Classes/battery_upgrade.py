# 9-9

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
        return long_name.title()  
    
    def read_odometer(self):
        """Print a statment showing the car's milage"""
        print(f"This car has {self.odometer_reading} miles on it.")

class Battery():
    """A simple attempt to model a battery for an electric car."""
    def __init__(self, battery_size=70):
        """Initialize the battery's attributes"""
        self.battery_size = battery_size

    def describe_battery(self):
        """print a statement describing a battery size."""
        print(f"This car has a {self.battery_size}-kwh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        
        message = f"This car can go approximatley {range}"
        message += " miles in a full charge."
        print(message)
    
    def upgrade_battery(self):
        """Upgrading the size of the default"""
        if self.battery_size != 85:
            self.battery_size = 85

class ElectricCar(Cars):
    """Represent aspects of a car, sepecific to electric vechiles."""
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

    # Overriding
    def fill_gas_tank():
        """Electric cats don't have gas tanks."""
        print("This car doesn't need a gas tank!")

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_describtive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()