class Users():
    """Making a profile"""
    def __init__(self, first_name, last_name, email, location, age):

        self.first_name = first_name    
        self.last_name = last_name
        self.email = email
        self.location = location
        self.age = age
        self.login_attempts = 0
    
    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

    def describe_user(self):
        """Summerize user profile"""
        print(f"\nFull Name: {self.first_name.title()} {self.last_name.title()}")
        print(f"Location: {self.location.title()}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")

    def greet_user(self):
        print(f"Hello, {self.first_name.title()} {self.last_name.title()}!")