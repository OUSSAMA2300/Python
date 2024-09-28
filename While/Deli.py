# A list of the ordered sandwiches
sandwich_orders = ['tuna', 'pastrami', 'grilled cheese',
                    'garlic', 'pastrami','egg', 'pastrami']

# A list of sandwiches that's been finished 
finished_sandwiches = []

# Removing the occurenses
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print("The Deli ran out of the pastrami")    

# Adding oreders to the finished list
while sandwich_orders:
    finished = sandwich_orders.pop()
    print("I made your", finished + "sandwich.")

    finished_sandwiches.append(finished)

# Looping thru all the finished orders
print("\nFinished sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich, "sandwich")