# requested_toppings = ['mushrooms','green peppers','extra chees']

# for requsted_topping in requested_toppings:
#     if requsted_topping == 'green peppers':
#         print("Sorry we are out of green peppers.")
#     else:
#         print("Adding " + requsted_topping + ".")

# print("Your pizza is done")

# #checking if the list is empty or not
# requested_toppings=[]

# if requested_toppings: #if this true it will proceeds in the for loop
#     for requsted_topping in requested_toppings:
#         print("Adding " + requsted_topping + ".")
# else:
#     print("Do you want a plain pizza?")  


# available_toppings= ['mushrooms','olives','green peppers',
#                      'pepperoni','pinapple','extra cheese']

# requested_toppings = ['mushrooms','french fries','extra cheese']

# for requested_topping in requested_toppings:
#     if requested_topping in available_toppings:
#         print("Adding " + requested_topping + ".")
#     else:
#         print("Sorry we don't have " + requested_topping + ".")


# print("Your pizza is done")

#Exercises

#5.8
# usernames = ['admin','ouss80','rana78','fawazi88'
#              ,'halland09','messi1']

# for username in usernames:
#     if username == 'admin':
#         print("Hello Mr.admin")
#     else:
#         print("Warm welcoms to our user " + username + "!")

#5.9
# users = []
# if users:
#     for user in users:
#          if user == 'admin':
#             print("Hello Mr.admin")
#          else:
#             print("Warm welcoms to our user " + user + "!")
# else:
#     print("We need to find some users!")


#5.10
# current_users = ['admin','ouss80','rana78','fawazi88'
#               ,'halland09','messi1']
# new_users = ['Ouss80','rana78','vivian90','jota60','pele79']

# for new in new_users:
#     if new.lower() in current_users:
#        print("This username is already taken")
#     else:
#         print("Hello our new user " + new +"!")

#5.11
ranks = list(range(1,10))

for rank in ranks:
    if rank == 1:
        print("1st")
    elif rank == 2:
        print("2nd")
    elif rank == 3:
        print("3rd")
    else:
        print(f"{rank}th")