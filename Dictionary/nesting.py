# A list of dictonaries
# alien_0 = {'color': 'green', 'points': 5}
# alien_1 = {'color': 'yellow', 'points': 10}
# alien_2 = {'color': 'red', 'points': 15}

# aliens = [alien_0, alien_1, alien_2]

# for alien in aliens:
#     print(alien)

# Make an empty list storing aliens
# aliens = []

# # Generate 30 green aliens 

# for alien_num in range(30):
#     new_alien = {'speed': 'slow','color': 'green', 'points': 5}
#     aliens.append(new_alien)

# # Changing colors of the first three aliens 
# for alien in aliens[:3]:
#     if alien['color'] == 'green':
#         alien['color'] = 'yellow'
#         alien['speed'] = 'medium'
#         alien['points'] = 10 
#     elif alien['color'] == 'yellow':
#         alien['color'] = 'red' 
#         alien['speed'] = 'fast'
#         alien['points'] = 15

# # Show the first 5 aliens 
# for alien in aliens[:5]:
#     print(alien)

# print("....")

# # Show the number of the aliens that created so far
# print("Total number of alines:", len(aliens))


# A list in a dictionary

# Store information about a pizza being orderd
# pizza = {
#     'crust': 'thick',
#     'toppings': ['mushroom', 'extra cheese']
# }

# # Summerize the oreder
# print("You orederd a ", pizza['crust'],"curst pizza" 
#       "the following toppings:")


# for topping in pizza['toppings']:
#     print("\3 " + topping + " \3")


# fav_lang = {
#     'jen': ['python', 'ruby'],
#     'sarah': ['c'],
#     'edward': ['ruby', 'go'],
#     'phil': ['python', 'haskell']
# }

# for name, langs in fav_lang.items():
#     print('\n', name.title() + "'s favorite languages are:")
#     for lang in langs:
#         print("\t", lang.title())

# user = {
#     'aeinstien': {
#         'first': 'albert',
#         'last': 'enistien',
#         'location': 'princeton'
#     },
#     'mcurie': {
#         'first': 'marie',
#         'last': 'curie',
#         'location': 'paris'
#     }
# }

# for username, user_info in user.items():
#     print("\nUsername:", username)
#     fullname = user_info['first'] + " " + user_info['last']
#     location = user_info['location']

#     print("\tFull name:", fullname.title())
#     print("\tLocation:",location.title())

#6-7

# person_1 = {
#          'fname': 'kemo', 
#           'lname':'ahmed',
#            'city':'mallawi'}
# person_2 = {
#     'fname': 'oussama',
#     'lname': 'mohamed',
#     'city': 'alex'
# }

# person_3 = {
#     'fname': 'mohamed',
#     'lname': 'hamdy',
#     'city': 'mansoura'
# }


# people = [person_1, person_2, person_3]

# for person in people:
#     fullname = person['fname'] + " " + person['lname']
#     print('\nFull name:', fullname.title())
#     print("City:", person['city'].title()) 

#6-8

# kitty = {
#     'kind': 'cat',
#     'breed': 'siami',
#     'owner': 'sarah'
# }

# lemon = {
#     'kind': 'dog',
#     'breed': 'german',
#     'owner': 'hala'
# }

# hangging = {
#     'kind': 'snake',
#     'breed': 'python',
#     'owner': 'ali'
# }

# pets = [kitty, lemon, hangging]

# for pet in pets:
#     print("\nKind:", pet['kind'].title())
#     print("Breed:", pet['breed'].title())
#     print("Owner:", pet['owner'].title())


#6-9

fav_places = {
    'oussama': ['park', 'farm', 'pool'],
    'ahmed': ['beach', 'pitch', 'club'],
    'kareem': ['cafe', 'resturant']
}

for person, places in fav_places.items():
    print(person.title() + "'s favorite places are:")
    for place in places:
        print("\t-", place.title())


#6-10
fav_nums = {
    'ahmed': [5, 4, 1],
    'alaa': [0, 39, 13],
    'hamdy': [9, 32, 15],
    'abdo': [10, 19, 20],
    'oussama': [8, 6, 2]
}

for name, nums in fav_nums.items():
    print(name.title() + "'s numbers are:")
    for num in nums:
        print("\t-", num)

# 6-11

cities = {
    'tokyo': {
        'country': 'japan',
        'population': '37.1 million',
        'fact': 'Tokyo was a small fishing village called Edo'        
        },
    'delhi': {
        'country': 'india',
        'population': '33.8 million',
        'fact': 'Delhi is home to the Red Fort, UNESCO World Heritage site'
    },
    'shanghai': {
        'country': 'china',
        'population': '29.8 million',
        'fact': 'Shanghai is known for its impressive skyline, featuring the Orinental Pearl Tower'
    }
}

for city, city_info in cities.items():
    print("\n", city.title() +", " +
           city_info['country'].title() + ":")
    print("Population:", city_info['population'])
    print("Fact:", city_info['fact'])


