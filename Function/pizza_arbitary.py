# Arbitary
def make_pizza(*toppings):
    """Print the list of the toppings that have been requsted"""
    print("\nMaking a pizza with the following topping:")
    for topping in toppings:
        print("- " + topping)

# make_pizza('pepperoni')
# make_pizza('mushrooms', 'green peppers', 'extra cheese')

# Mixing arbitary with postional
#  Python stores the first value it receives in 
# the parameter size. All other values 
# that come after are stored in the tuple     
def make_pizza(size, *toppings):
    """Summerize the pizza order"""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

# make_pizza(16, 'pepperoni')
# make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
