def count_words(filename):
    """Count the approximate number of words in the file."""
    try:
        with open(filename) as file_obj:
             contents = file_obj.read()
    except FileNotFoundError:
          # Failing silently
          pass
    else: 
         words = contents.split()
         num_word = len(words)
         print(f"The file {filename} has about {num_word} words.")

filenames = ['alice_in_wonderland.txt', 'suddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)