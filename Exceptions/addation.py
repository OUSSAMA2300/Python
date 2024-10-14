# # 10-6
def add_numbers():
    try:
        number1 = input("Enter the first number: ")
        num1 = int(number1)

        number2 = int(input("Enter the second number: "))
        num2 = int(number2)
        
        result = num1 + num2
        print(f"The result is: {result}")
    except ValueError:
        print("Error: Please enter valid numbers.")

# Test the program
add_numbers()
