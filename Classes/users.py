class Users():
    """Making a profile"""
    def __init__(self, first_name, last_name, location, field):

        self.first_name = first_name    
        self.last_name = last_name
        self.location = location
        self.field = field

    def describe_user(self):
        """Summerize user profile"""
        print(f"\nFull Name: {self.first_name.title()} {self.last_name.title()}")
        print(f"Location: {self.location.title()}")
        print(f"Field: {self.field.title()}")

    def greet_user(self):
        print(f"Hello, {self.first_name.title()} {self.last_name.title()}!")
        
user = Users('ali', 'arab', 'london', 'medicine')
user.describe_user()
user.greet_user()

user = Users('hossam', 'ahmed', 'cairo', 'NLP')
user.describe_user()
user.greet_user()

user = Users('hamdy', 'alaa', 'india', 'chemistry')
user.describe_user()
user.greet_user()