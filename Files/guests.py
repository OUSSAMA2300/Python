# 10-3
name = input("Please enter your name: ")

filename = 'guests.txt'

with open(filename, 'w') as file_object:
        file_object.write(f"{name.title()}\n")