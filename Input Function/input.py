# A message
# msg = input("Tell me something, and i will repeat it:")
# print(msg)

# name = input("Please enter your name: ")
# print("Hello, " + name + "!")

# You can put in a variable then pass it the input function

# prompt = "\nIf you tell us who you are, we can personalize the messges you see."
# prompt += "\nWhat is your first name?"
# prompt += "\nEnter your name here: "

# name = input(prompt)
# print("\nHello, " + name + "!")


# Using int() to accept numerical inputs

# age = input("How old are you? ")

# age = int(age)
# if age >= 18:
#    print("you're old enough to vote")


# height = input("How tall are you, in inches? ")
# height = int(height)

# if height >= 36:
#    print("\nYou're tall enough to ride!")
# else:
#    print("Be a moii")

# number = input("Enter a number to determine wether it odd or even? ")
# number = int(number)

# if number % 2 == 0:
#     print("\nThe number", number, "is even")  
# else:
#     print("\nThe number", number, "is odd")

# 7-1

# car = input("What kind of car you want to rent? ")

# print("Let me see if I can find a" ,car.title())

# 7-2

# people_to_sit = input("How many people are in the dinner group? ")

# people_to_sit = int(people_to_sit)
# if people_to_sit > 8:
#     print("You will have to wait for a table")
# else:
#     print("Your table is ready!")

# 7-3
num = input("Enter a number and i will tell whether the number is multiple of 10 or not ")

num = int(num)

if num % 10 == 0:
    print("The number is multiple of 10")
else:
    print("The number is not multiple of 10")