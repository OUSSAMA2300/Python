# 10-11
import json

filename = 'favourite_number.json'

with open(filename) as f_obj:
    fav_number = json.load(f_obj)
    print(f"I know your favourite number! It's {fav_number}")