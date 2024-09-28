responses = {}

# Set a flag to indicate that polling is acitve 
polling_active = True

while polling_active:
    # Prompt for the person's name and response
    name = input("\nWhat's your name? ")
    response = input("Which mountain would you like to climb someday? ")

    # Store the response in the dictionary 
    responses[name] = response

    # Find out if someone else is going to take the poll.
    repeat = input("Would you like to let another person respond? ")
    if repeat == 'no':
        polling_active = False

# Polling is complete. Show results.
print("\n--- Poll Results ---")
for name ,response in responses.items():
    print(name.title(), "would like to climb", 
          response.title() + ".")