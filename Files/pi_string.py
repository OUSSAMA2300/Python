# filename = 'pi_digits.txt'

# with open(filename) as file_object:
#     lines = file_object.readlines()

# pi_string = ''
# for line in lines:
#     pi_string += line.strip()

# print(pi_string)
# print(len(pi_string))


filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string[:52] + "...")
print(len(pi_string))

# Checking if my birthday is in the pi digits

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the pi's first million digits.")
else:
    print("Your birthday doesn't appear in the first million digits of pi.")

