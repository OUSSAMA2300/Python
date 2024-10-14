# 10-1
filename = 'learning_python.txt'
with open(filename) as file_object:
    contents = file_object.read()
    print("Reading the entire file at once:")
    print(contents.strip())


with open(filename) as file_object:
    print("\nLooping over the file object:")
    for line in file_object:
        print(line.strip())

with open(filename) as file_object:
    lines = file_object.readlines()

print("\nStoring lines in a list and working outside the with block:")

sents = ''
for line in lines:
    sents += line

print(sents)

# 10-2
print("\n", sents.replace('Python', 'C'))