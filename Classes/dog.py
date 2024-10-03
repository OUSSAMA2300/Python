#1
class Dog():
    #2
    """A simple attempt to model a dog."""
    #3
    def __init__(self, name, age):
        """Intiliaze name and age attributes"""
        #4
        self.name = name
        self.age = age
#5
    def sit(self):
        """Simulate a dog sitting in response to a command"""
        print(f"{self.name.title()} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command"""
        print(f"{self.name.title()} rolled over.")


# Making an istance form a class
my_dog = Dog('willie', 6) # Storing the instance that created by __init__
your_dog = Dog('lucy', 3) # Creating multiple instances

print(f"My dog's name is {my_dog.name.title()}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()
my_dog.roll_over()

print(f"\nYour dog's name is {your_dog.name.title()}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()
your_dog.roll_over()