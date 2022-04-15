def print_models(x, y):
    """
    Simulate printing each design, until non are left.
    Move each design to completed_models after printing.
    """
    while x:
        current_design = x.pop()
        print("Printing model: " + current_design)
        y.append(current_design)

def show_completed_models(y):
    """Show all the movels that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in y:
        print(completed_model)