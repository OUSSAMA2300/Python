filename = 'alice_in_wonderland.txt'

try:
    with open(filename) as file_obj:
        contents = file_obj.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} doesn't exsit.")
else:
    # Count the approximate number of words in the file.
    words = contents.split()
    num_word = len(words)
    print(f"The file {filename} has about {num_word} words.")