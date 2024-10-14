def add_numbers():
    while True:
        try:
            number1 = input("Enter the first number: ")
            if number1 == 'q':
              break
            num1 = int(number1)

            number2 = int(input("Enter the second number: "))
            if number2 == 'q':
                break

            num2 = int(number2)
        
            result = num1 + num2
            print(f"The result is: {result}")

        except ValueError:
            print("Error: Please enter valid numbers.")
        
# Test the program
add_numbers()
