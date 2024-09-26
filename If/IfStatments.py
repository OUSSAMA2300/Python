# cars = ['audi', 'bmw', 'suaru', 'toyota']

# for car in cars:
#     if car == 'bmw':
#         print(car.upper())
#     else:
#         print(car.title())

# age1 = 22
# age2 = 18

# if (age1 >= 21) or (age2 >= 21):  #& and | can be used also
#     print(True)
# else:
#     print(False)

# requested_toppings = ['mushrooms', 'onions', 'pineapple']
# if 'mushrooms' in requested_toppings:
#     print(True)
# if 'pepporoni' not in requested_toppings:
#     print("Hold the Pepporoni")

# banned_users = ["andrew", 'carolina', 'david','ousama']
# user = 'marie'

# if user != banned_users:
#     print(user.title()+ ", you can post a response if you wish.")
#--------------------------------



# car = 'subaru'
# print("Is car = 'subaru'? i predict True.")
# print (car == 'subaru')

# print("\nIs car = 'audi'? i predict False.")
# print (car == 'audi')

# guests = 'marie'
# print('\ni predict true')
# print (guests=='marie')

# halawa = 'malban'
# print('\ni predict true')
# print(halawa=='malban')

# rises = 'moon'
# print('\ni predict right')
# print(rises=='moon')



#mine
# astro = ['earth','jupyter']
# not_astro  = ['moon','sun']
# planets = ['earth','mars','auranus','jupyter']
# not_planet = 'moon'
# if any(planet in astro for planet in planets) and not_planet not in planets:
#     print("the astro is a planet" )
#     print([planet for planet in planets if planet in astro ])
# elif not_planet in not_astro:
#     print("it's an object")

# laptop = ['hp','lenovo','asus','aser']
# brand = 'HP'
# if brand.lower() not in laptop:
#     print(brand.title() + " is not in the list")
    
# else:
#     print("it's in the list")

# age = 16
# if age >17 and age<20  :
#    print("you're young")

# elif age==16:
#     print("your age is "+ str(age))

# #1
# string1 = 'if'
# string2 = 'elif'
# print(string1 == string2)
# print(string1 != string2)

# #2
# string3 = 'oussama'
# string4 = 'OUSSAMA'
# print(string3.lower() == string4.lower() ,  'pred true')
# print(string3.lower() != string4.lower() , "pred false")

# #3
# num1 = 10
# num2 = 20
# print(num1 == 10)
# print(num1 != num2)
# print(num1 > 5)
# print(num1 < num2)
# print(num1 >= 10)
# print(num1 <= 5)

# #4
# print(num1 >5 and num2 >15)
# print(num1 >15 or num2 >15)

# #5
# fruits = ['apple','banana','cherry']
# print('apple'in fruits)
# print('grape'in fruits)

# print('grape'not in fruits)
# print('banana'not in fruits)
#--------------------------


# age  = 17
# if age >= 18:
#     print("you are old enough to vote")
# else:
#     print("sorry you can't vote, you're young")

# age = 4

# if age<=4:
#     print("your admission costs 0$")

# elif age<18:
#     print("your admission costs 5$")

# else:
#     print('your admission costs 10$')

# if age<5:
#     price = 0

# elif age<18:
#     price = 5

# else:
#     price = 10

# print("your admission cost is $" + str(price) + ".")

#-----------

# extra_topping = ['mushrooms','extra cheese']

# if 'mushrooms' in extra_topping:
#     print("adding mushrooms")
# if 'pepperoni' in extra_topping:
#     print("adding pepperoni")
# if 'extra cheese' in extra_topping:
#     print("adding extra cheese")

# print("\nyour pizza is ready")

#-----------------------

# alien_color = 'red'

# if alien_color == 'green':
#     print("You knocked the alien, you earned 5 points")

# else:
#     print("You earned 10 points")

#v1.0

# alien_color = 'green'

# if alien_color == 'green':
#     print("You knocked the alien, you earned 5 points")

# elif alien_color == 'yellow' :
#     print("You earned 10 points")

# elif alien_color == 'red':
#     print("You earned 15 points")

# #v2.0

# alien_color = 'yellow'

# if alien_color == 'green':
#     print("You knocked the alien, you earned 5 points")

# elif alien_color == 'yellow' :
#     print("You earned 10 points")

# elif alien_color == 'red':
#     print("You earned 15 points")

# #v3.0

# alien_color = 'red'

# if alien_color == 'green':
#     print("You knocked the alien, you earned 5 points")

# elif alien_color == 'yellow' :
#     print("You earned 10 points")

# elif alien_color == 'red':
#     print("You earned 15 points")


# age= 50

# if age < 2:
#     print("This person is a baby")
# elif (age >= 2) and (age < 4):
#     print("This person is a toddler")
# elif (age >= 4) and (age < 13):
#     print("This person is a kid")
# elif (age >=13) and (age < 20):
#     print("This person is a teenager")
# elif (age >= 20) and (age < 65):
#     print("This person is an adult")
# elif age >= 65:
#     print("This person is an elder")   

fav_fruits=['banana','apple','orange']
if 'banana' in fav_fruits:
    print("You really like bananas")
if 'apple' in fav_fruits:
    print("You really like apples")
if 'orange' in fav_fruits:
    print("You really like oranges")
if 'watermelon' in fav_fruits:
    print("You relly like watermelons")
if 'guava' in fav_fruits:
    print("You really like guavas")

