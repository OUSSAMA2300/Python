from car_class import Cars

my_new_car = Cars('bmw', 'X8', 2024)
print(my_new_car.get_describtive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

my_used_car = Cars('audi', 'a4', 2016)
print(my_used_car.get_describtive_name())

my_new_car.odometer_reading = 2300
my_new_car.read_odometer()