# 11-3 
class Employee():
    def __init__(self, f_name, l_name, annual_salary):
        """Raising employee salary"""
        self.f_name = f_name
        self.l_name = l_name
        self.annual_salary = annual_salary
    
    def give_raise(self, default=5000):
        """Raising employee salary with $5000 as a default"""
        self.annual_salary += default