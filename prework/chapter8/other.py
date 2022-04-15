def print_models(x, y):
    """Simulate printing each design, until none are left.
       Move each design to y after printing."""
    while x:
        current_design = x.pop()
        print("Printing model: " + current_design)
        y.append(current_design)

def show_completed_models(y):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in y:
        print(completed_model)