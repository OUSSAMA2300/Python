# 8-15
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