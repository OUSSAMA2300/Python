def make_shirt(size, text):
    print("\nYour T-Shirt size is:", size,
          "\nThe sentence you want to print is:", text)

# Calling using postional arguments    
make_shirt('M', 'Wake up')

# Calling using keyword arguments
make_shirt(size='S', text='its the first of the month')

# Large Shirts 8-4
def make_shirt(text='I love Python', size='XXXL'):
    print("\nYour T-Shirt size is:", size,
          "\nThe sentence you want to print is:", text)

# The large one
make_shirt()

# The medium one
make_shirt(size='M')

# with the any size 
make_shirt(size='S', text='I hate Python')