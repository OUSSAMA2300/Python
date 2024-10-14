def file_reader(filename):
    """Reading files""" 
    try:
        with open(filename) as file_obj:
            contents = file_obj.read()
    except FileNotFoundError:
        pass
    else:
        print(contents.split())

files = ['cats.txt', 'dogs.txt']
for file in files:
    file_reader(file)