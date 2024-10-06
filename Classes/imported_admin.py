from admin_class import Admin

admin = Admin('ali', 'arab', 'ali@email.com', 'london', 23)
admin.privileges.admin_privileges = ['can delete post', 'can ban user']
admin.privileges.show_privileges()