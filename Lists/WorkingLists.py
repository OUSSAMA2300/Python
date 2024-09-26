# magicians = ['alice', 'david', 'carolina']
# for magician in magicians:
#     print(magician.title() + ", that was a great trick!")
#     print("I can't wait to see your next trick, " + magician.title() + ".\n")


# print('Thank you, everyone.That was a great magic show!')

#------------------------------

# pizzas = ['pepperoni', 'mixed cheese','ranch']
# for pizza in pizzas:
#     print("I like " + pizza + " pizza")
#     print("I really love pizza\n")


# animals = ['cat', 'dog', 'hamester']
# for animal in animals:
#     print("A " + animal + " would make a great pet.")
#     print("Any of these anilmals would make a great pet.\n")

#------------------------

# for value in range(1,6):
#     print(value)

# numbers = list(range(1,6))
# print(numbers)    

# even_num = list(range(2,12,2))
# print(even_num)


# squares = []
# for value in range (1,11):
#     square = value**2
#     squares.append(square)

# print(squares)

#list conprehension

# squares = [value**2 for value in range (1,11)]
# print(squares)

#--------------try

# for count in range(1,21):
#     print(count)

million= list(range(1,1000001))
# for num in million:
#     print(num)

# print(min(million))
# print(max(million))
# print(sum(million))

# even_num = list(range(2,21,2))
# for even in even_num:
#     print(even)

# threes = list(range(3,31,3))
# for three in threes:
#     print(three)

# for value in range(1,11):
#     cubes = value**3
#     print(cubes)

# cubes = [value**3 for value in range(1,11)]
# print(cubes)

#slicing a list

# plyrs = ['messi','maradona','ronaldo','halland','mbappe','neymar']
# print(plyrs[0:3]) #0, 1 and 2
# print(plyrs[0:2]) # 0 and 1 

# print(plyrs[-4:])# last three

# print("Here the last three legends in the history:")
# for plyr in plyrs[-3:]:
#     print(plyr.title())
    
#copying a list

# my_foods = ['pizza', 'flafel', 'carrot cake']
# friend_food = my_foods[:]

# friend_food = my_foods

# my_foods.append('cannoli')
# friend_food.append('ice cream')

# print("MY favourite foods are:")
# print(my_foods)

# print("\nMy friend's favourite foods are:")
# print(friend_food)


# print("MY favourite foods are:")
# print(my_foods)

# print("\nMy friend's favourite foods are:")
# print(friend_food)

#try
# magicians = ['alice', 'david', 'carolina','kadry','oussama','moii']
# print("The first three items in the list are:")
# print(magicians[:3])

# print("Three items in the middle of the list are:")
# print(magicians[2:5])

# print("The last three items in the list:")
# print(magicians[3:])

my_pizza = ['pepperoni', 'mixed cheese','ranch']
friend_pizza = my_pizza[:]

my_pizza.append('chicken')
friend_pizza.append('beef')

print(my_pizza)
print(friend_pizza)

print("My favourite pizzas are:")
for pizza in my_pizza:
    print(pizza)

print("My friend's favourtie pizzas are:")
for pizza in friend_pizza:  
    print(pizza)

my_foods = ['pizza', 'flafel', 'carrot cake']

print("My fav foods are :")
for food in my_foods[:1]:
    print(food)