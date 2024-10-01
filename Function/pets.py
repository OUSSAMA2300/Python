def describe_pet(animal_type, animal_name):
    """"Display information about a pet."""
    print("\nI have a", animal_type + ".")
    print("My", animal_type + "'s name is", animal_name.title() + ".")


# Postional arguments
describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

# Order matters
describe_pet('harry', 'hamster')

# Keyword arguments
describe_pet(animal_name='harry', animal_type="hamster")
describe_pet(animal_type='hamster', animal_name='harry')

# Assinging a default value to a parameter
def describe_pet(animal_name, animal_type='dog'):
    """"Display information about a pet."""
    print("\nI have a", animal_type + ".")
    print("My", animal_type + "'s name is", animal_name.title() + ".")

describe_pet(animal_name='willie')
describe_pet('willie')

# It will explicit the default value when you enter a value
describe_pet(animal_name='harry', animal_type="hamster")
describe_pet('harry', 'hamster') # Equivalent function calls

# A dog named Willie.
describe_pet('willie')

describe_pet(animal_name='willie')
# A hamster named Harry.
describe_pet('harry', 'hamster')
describe_pet(animal_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', animal_name='harry')

describe_pet()