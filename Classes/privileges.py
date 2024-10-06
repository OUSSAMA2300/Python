from users_class import Users
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
admin.privileges.admin_privileges = ['can delete post', 'can ban user']
admin.privileges.show_privileges()