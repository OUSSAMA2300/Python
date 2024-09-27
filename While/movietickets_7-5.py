

while True:
   age = input("Please enter your age (enter quit to stop) ")
   if age == 'quit':
      break
   
   age = int(age)

   if age < 3:
      print("Your ticket costs $0")
   elif (age >= 3) and (age < 12):
      print("Your ticket costs $10")
   elif age >= 12:
      print("Your ticket costs $15")
 