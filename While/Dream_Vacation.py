dream_vacation = {}

# Setting a flag 
poll_active = True

while poll_active:
    name = input("\nWhat's your name? ")
    place = input("If you could visit one place in the world, where would you go? ")

    dream_vacation[name] = place

    repeat = input("Would you like to let another person respond? (yes/no)" )

    if repeat.lower() == 'no':
        poll_active = False    

print("\n--- Poll Results ---")
for name, place in dream_vacation.items():
    print(name, "would like to visit", place)