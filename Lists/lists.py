# bicycles = ['trek', 'cannondale', 'redline', 'specialized']
# print(bicycles[1].title())

# print(bicycles[0].upper())
# print(bicycles[3].upper())
# print(bicycles[-2]) #بتجيب الليست بالعكس

# msg = "My first bike was a " + bicycles[0].title() + "."
# print(msg)

# frens = ['katie', 'kemo', 'ahmed', 'hamdy', 'habrahim', 'abdoo']
# print(frens[-2].title())


# msg1 = "I Love YOU <3 " + frens[0].title()
# msg2 = "Hello my friend " + frens[1].title()
# msg3 = "Hello my friend " + frens[2].title()
# msg4 = "Hello my friend " + frens[3].title()
# msg5 = "Hello my friend " + frens[4].title()

# print(msg1)
# print(msg2)
# print(msg3)
# print(msg4)

# ownlist= ['mercedes', 'honda', 'kia', 'toyota']

# msg = "I would like to own a " + ownlist[2].title() + " car."
# print(msg)

# -----------
# Modifiying the list

# cars = ['Kia', 'ford', 'toyota']
# print(cars) 

# cars[0]= 'mazda'
# print(cars)

# appending elemnts to the list 

# cars.append('hyundai')
# print(cars)

# adding elements to empty list with append 

# motorcycle = []

# motorcycle.append('honda')
# motorcycle.append('yamaha')
# motorcycle.append('suzuki')

# print(motorcycle)

# -----------------

# inserting elements 

# motorcycle.insert(3, 'ducati')
# print(motorcycle)
#------------------------

# removing with del delete for instant like someone cancelling them order or card

# del motorcycle[3]
# print(motorcycle)

#---------------------
# removing with pop() u may use that value like

# popped_moto = motorcycle.pop()
# print(motorcycle)
# print(popped_moto)

# last_owned = motorcycle.pop()
# print("The last motorcycle i owned was a " + last_owned.title() + ".")

#popping form any postion
# 

# -----------------------------------------

# cars = ['kia', 'ford', 'toyota', 'mazda']
# print(cars)

# cars.remove('mazda')
# print(cars)

# too_exp = 'ford'
# cars.remove(too_exp)
# print(cars)
# print("\nA " + too_exp.title() + " is too expensive for me")
# --------

#Exercises

guests = ['kemo', 'hamdy', 'ahmed']

# cant = 'kemo'  #can't make it to the dinner
# print(cant.title())

# guests[0]= 'Monsef'


# print("I found a bigger dinner table!")

guests.insert(3, 'monsef')
guests.insert(4, 'habrahim')
guests.append('abdoo')

# print("Hi! " + guests[0].title() +" Don't be late to the dinner.")
# print("Hi! " + guests[1].title() +" Bring some pizza to the game after the dinner.")
# print("Hi! " + guests[2].title() +" Come over to watch the game and have some dinner")
# print("Hi! " + guests[3].title() +" Don't be late to the dinner.")
# print("Hi! " + guests[4].title() +" Don't be late to the dinner.")
# print("Hi! " + guests[5].title() +" Don't be late to the dinner.")

print("Sorry friends i can only invite two guests")

popped_gst = guests.pop()
print("Sorry, " + popped_gst.title())

popped_gst = guests.pop()
print("Sorry, " + popped_gst.title())

popped_gst = guests.pop()
print("Sorry, " + popped_gst.title())

popped_gst = guests.pop()
print("Sorry, " + popped_gst.title())

print("Hi! " + guests[0].title() +" Don't be late to the dinner.")
print("Hi! " + guests[1].title() +" Bring some pizza to the game after the dinner.")

del guests[1]
del guests[0]
print(guests)