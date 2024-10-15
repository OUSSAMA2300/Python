import json

def get_stored_username():
    """Get stored username if available"""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username
    
def get_new_username():
    """Prompt for username"""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username
# Load the username, if it has been strored previously.
# Otherwise, prompt for the username to store it.
def greet_user():
    """Greet the user by name"""
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}!")
    else:
       get_new_username()
       print(f"Next time we'll remember you {username}!")

greet_user()