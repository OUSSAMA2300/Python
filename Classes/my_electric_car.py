# Importing mutliple classes
from car_classes import Cars, ElectricCar

# my_tesla = ElectricCar('tesla', 'model s', 2016)

# print(my_tesla.get_describtive_name())
# my_tesla.battery.describe_battery()
# my_tesla.battery.get_range()

my_beetle = Cars('volkswagen', 'beetle', 2016)
print(my_beetle.get_describtive_name())

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_describtive_name())