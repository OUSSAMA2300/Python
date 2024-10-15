from name_function import get_foramtted_name

print("Enter 'q' to quit.")
while True:
    first = input("\nPlease enter your first name: ")
    if first == 'q':
        break 

    last = input("Please enter your last name: ")
    if last == 'q':
        break

    formatted_name = get_foramtted_name(first, last)
    print(f"Neatly formatted name: {formatted_name}")