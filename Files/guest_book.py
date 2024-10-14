filename = 'guest_book.txt'

names = []
while True:
        name = input("Plesae enter your name (q to quit): ")
        if name.lower() == 'q':
                break
        print(f"Warm welcomes to our guest {name.title()}!")
        names.append(name)
        
with open(filename, 'a') as file_object:
        for name in names:
            file_object.write(f"{name.title()} visited us\n")