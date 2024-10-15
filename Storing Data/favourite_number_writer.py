# 10-11
import json
fav_number = input("What is your favourtie number? ")

filename = 'favourite_number.json'

with open(filename, 'w') as f_obj:
        json.dump(fav_number, f_obj)