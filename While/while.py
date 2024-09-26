#

# current_number = 1
# while current_number <= 5:
#     print(current_number)  
#     current_number += 1

prompt = "\nTell me something and i will repeat it:"
prompt += "\nEnter 'quit' to end the program. "

# msg = ""

# while msg != 'quit':
#     msg = input(prompt)

#     if msg != 'quit':  
#        print(msg)
#     else:
#         print("Quitting...")

active = True
while active:
    msg = input(prompt)

    if msg == 'quit':
        active = False
        print("Quitting...")  
    else:
        print(msg)