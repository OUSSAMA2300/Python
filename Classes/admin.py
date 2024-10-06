# 9-7
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

# 9-8
class Privileges():
    def __init__(self, admin_privileges=[]):
        self.admin_privileges = admin_privileges

    def show_privileges (self):
        print("Admin privileges:")

        for privilege in self.admin_privileges:
            print(f"- {privilege}")

class Admin(Users):
    def __init__(self, first_name, last_name, email, location, age):
        super().__init__(first_name, last_name, email, location, age)

        self.privileges = Privileges()



admin = Admin('ali', 'arab', 'ali@email.com', 'london', 23)

admin.privileges.admin_privileges = ['can add post', 'can delete post', 'can ban user']
admin.greet_user()
admin.privileges.show_privileges()