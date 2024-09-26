current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue  # Igonre the rest to just copy the odd numbers and 
                  # and return to the beginning

    print(current_number)

