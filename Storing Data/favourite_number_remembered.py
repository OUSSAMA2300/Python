# 10-12
import json

def fav_number():
    try:
        filename = 'favourite_number.json'

        with open(filename) as f_obj:  
            fav_number = json.load(f_obj)
    except FileNotFoundError:
        fav_number = input("What is your favourtie number? ")

        filename = 'favourite_number.json'

        with open(filename, 'w') as f_obj:
            json.dump(fav_number, f_obj)
    else:
        print(f"I know your favourite number! It's {fav_number}")

fav_number()