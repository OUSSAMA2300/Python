# Start with some designs that need to be printed
# unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
# completed_models = []

# # Simulate printing each desgin, until none are left.
# #  Move each design to compelted_design after printing 

# while unprinted_designs:
#     currnent_design = unprinted_designs.pop()

#     # Simulate creating a 3D print from the design 
#     print("Printing model: " + currnent_design)
#     completed_models.append(currnent_design)

# # Display all completed models
# print("\nThe following models have been printed:")
# for completed_model in completed_models:
#     print(completed_model)


# Doing them as functions that can modify lists
def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each desgin, until none are left.
    Move each design to compelted_design after printing 
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()

         # Simulate creating a 3D print from the design 
        print("Printing model: " + current_design)
        completed_models.append(current_design)

def show_completed(completed_models):
    """
    Display all completed models
    """
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

# print_models(unprinted_designs, completed_models)
# show_completed(completed_models)

# Using import

import printing_functions

printing_functions.print_models(unprinted_designs, completed_models)
printing_functions.show_completed(completed_models)