# 8-9
magicians = ['harry potter', 'gandalf', 'merlin', 'doctor strange']

def show_magicians(names):
    """"Display the names of the magicians"""
    for name in names:
        print(name)

# show_magicians(magicians)

# 8-10
def make_great(magicians):
    """"Adding 'the Great' to each name"""
    great_magicians = []
    for magician in magicians:
        great_magician = "the Great " + magician.title()
        great_magicians.append(great_magician)
    return great_magicians

great_magician = make_great(magicians[:])

show_magicians(great_magician)

# 8-11

print("\nPrint the original list:")
show_magicians(magicians)

print("\nPrint the modified list:")
show_magicians(great_magician)







# Another solution
# def make_great(magicians):
#     for i in range(len(magicians)):
#         magicians[i] = f"the Great {magicians[i].title()}"

# make_great(magicians)

# show_magicians(magicians)
