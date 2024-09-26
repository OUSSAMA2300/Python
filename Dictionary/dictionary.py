# alien_0 = {'color':'green', 'points': 5}
# print(alien_0['color'])
# print(alien_0['points'])

# new_points = alien_0['points']
# print("You earned", new_points ,"points!")

# #adding new values to dictionaries
# print(alien_0)
# alien_0['x_pos'] = 0
# alien_0['y_pos'] = 25
# print(alien_0)

# alien_0 = {}
# alien_0['color'] = 'red'
# alien_0['points'] = 6
# print(alien_0) 

# #modifiying 
# alien_0 = {'color':'green'}
# print(alien_0['color'])
# alien_0['color'] = 'yellow'
# print(alien_0['color'])

# alien_0 = {'x_pos': 0, 'y_pos': 25, 'speed': 'medium'}
# print("Original x-position",alien_0['x_pos'])

# #Move alien to the right
# #determine how far is the alien based on its current speed

# if alien_0['speed'] == 'slow':
#     x_inc = 1
# elif alien_0['speed'] == 'medium':
#     x_inc = 2
# else:
#     #this must be a fast alien
#     x_inc = 3

# alien_0['x_pos'] = alien_0['x_pos'] + x_inc
# print("New x-position", alien_0['x_pos'])

# alien_0['speed'] = 'fast'

#removing a key-value
# alien_0 = {'color':'green', 'points': 5}
# del alien_0['points']
# print(alien_0)

# fav_langs = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python'
# }

# print("Sarah's favorite language is",
#        fav_langs['sarah'].title(),".")

#6-1

# person = {'f_name': 'kemo', 'l_name':'ahmed',
#            'city':'mallawi'}
# print(person['f_name'])
# print(person['l_name'])
# print(person['city'])

# #6-2
# fav_num = {
#     'ahmed': 4,
#     'alaa': 7,
#     'hamdy': 9,
#     'abdo': 8,
#     'oussama': 10
# }

# print("Ahemd's favorite number is", fav_num['ahmed'])
# print("Alaa's favorite number is", fav_num['alaa'])
# print("Hamdy's favorite number is", fav_num['hamdy'])
# print("Abdo's favorite number is", fav_num['abdo'])
# print("Oussama's favorite number is", fav_num['oussama'])


#6-3
# glossery = {
#     'variable': 'A name that refers to a value stored in memory.',
#     'tuple': 'An immutable collection of items in a particular order.',
#     'loop': 'A control flow statement that repeats a block of code multiple times.',
#     'list': 'A collection of items in a particular order, mutable and allows duplicate entries.',
#     'dictionary': 'A collection of key-value pairs, where each key is unique and maps to a value.'
# }

# print("A variable is,",glossery['variable'])
# print("\nA tuple is,",glossery['tuple'])
# print("\nA loop is,",glossery['loop'])
# print("\nA list is,",glossery['list'])
# print("\nA dictionary is,",glossery['dictionary'])

