# user_0 = {
#   'username': 'efermi',
#   'first': 'enrico',
#   'last': 'fermi'
#  }

# for key, value in user_0.items():
#     print('\nKey:', key)
#     print('Value:',value)

fav_langs = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

# for n, lang in fav_langs.items():
#     print(n.title()+ "'s favorite language is" , 
#           lang.title())

#key() method you can use it or not 
# for n in fav_langs.keys():
#     print(n.title())


#accessing the value using keys 

# friends = ['sarah', 'phil']
# for n in fav_langs.keys():
#     print(n.title())

#     if n in friends:
#         print("\tHi", n.title(),
#                ", I see your favorite langauge is"
#                ,fav_langs[n].title())
        

# if 'erin' not in fav_langs.keys():
#     print("Erin, please take our poll")

#sorted order of dictionary

# for name in sorted(fav_langs.keys()):
#     print(name.title()+ ", thanks for taking the poll!")

#looping through all the values in a dic
print("The following languages has been mentioned:")
# for lang in fav_langs.values():
#     print(lang.title())

#to just use the unique value in the dic

for lang in set(fav_langs.values()):
    print(lang.title()) #This results to nonrepeatitve list



#6-4
# glossery2 = {
#     'variable': 'A name that refers to a value stored in memory.',
#     'tuple': 'An immutable collection of items in a particular order.',
#     'loop': 'A control flow statement that repeats a block of code multiple times.',
#     'list': 'A collection of items in a particular order, mutable and allows duplicate entries.',
#     'dictionary': 'A collection of key-value pairs, where each key is unique and maps to a value.'
# }

# for k, v in glossery2.items():
#     print("\nTerm:",k.title())
#     print("Defintions:", v)


# glossery2.update({
#     'items()': 'A method that returns a list of the key-vlaue pair',
#     'keys()': 'A method that returns just the key',
#     'value()': 'A method that returns just the value',
#     'sorted()': 'A function that make the dictioanry orderd',
#     'set()': 'A method that makes the dictionary returns a list of unique vlaues'
# })

# for k, v in glossery2.items():
#     print("\nTerm:",k.title())
#     print("Defintions:", v)

#6-5
rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'missisipi': 'usa'
}

for k, v in rivers.items():
    print("The", k.title(), "runs thruogh", v.title())
print('\n')
for riv in rivers.keys():
    print(riv.title())
print('\n')
for country in rivers.values():
    print(country.upper())

#6-6
 
poll = ['ahemd', 'kemo', 'oussama','sarah', 'jen', 'edward']

for name in poll:
    if name in fav_langs:
        print("Thanks for taking the poll", name.title())
    else:
        print("Please take our poll", name.title())