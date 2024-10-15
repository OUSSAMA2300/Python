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
    username = input("Enter your username: ")
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
        correct_user = input(f"Is this the correct username {username} (y/n): ")
        if correct_user.lower() == 'y':
            print(f"Welcome back, {username}!")
       
        else:
            username = get_new_username()
            print(f"We'll remember you when you come back, {username}!")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")
greet_user()