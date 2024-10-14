# # 9-14
from random import randint

x = randint(1, 6)
print(x)

class Die():
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        return randint(1, self.sides)

roll_6 = Die()
print("Rolling the 6-sided die 10 times:")
for _ in range(10):
    print(roll_6.roll_die())

roll_10 = Die(10)
print("\nRolling a 10-sided die 10 times:")
for _ in range(10):
    print(roll_10.roll_die())

roll_20 = Die(20)
print("\nRolling a 20-sided die 10 times:")
for _ in range(10):
    print(roll_20.roll_die())

