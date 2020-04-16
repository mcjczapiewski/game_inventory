
# This is the file where you must work.
# Write code in the functions (and create new functions) so that they work
# according to the requirements.


def display_inventory(inventory):
    """Display the contents of the inventory in a simple way."""
    if inventory:
        for key in inventory:
            print(str(key) + ": " + str(inventory[key]))
    pass


def add_to_inventory(inventory, added_items):
    """Add to the inventory dictionary a list of items from added_items."""
    if type(added_items) is not list:
        added_items = [added_items]
    for item in added_items:
        if item not in inventory:
            inventory[item] = 1
        else:
            inventory[item] = inventory[item] + 1
    return inventory


def remove_from_inventory(inventory, removed_items):
    """Remove from the inventory dictionary a list of items from removed_items."""
    if type(removed_items) is not list:
        removed_items = [removed_items]
    for item in removed_items:
        if item in inventory:
            inventory[item] = inventory[item] - 1
            if inventory[item] < 1:
                del inventory[item]
    return inventory


def print_table(inventory, order):
    """
    Display the contents of the inventory in an ordered, well-organized table with
    each column right-aligned.
    """

    pass


def import_inventory(inventory, filename):
    """Import new inventory items from a CSV file."""

    pass


def export_inventory(inventory, filename):
    """Export the inventory into a CSV file."""

    pass


if __name__ == "__main__":
    inventory = {"raz": 1, "dwa": 2}
    display_inventory(inventory)
    print('TTT')
    add_to_inventory(inventory, ["raz", "dwa", "trzy", "raz", "cztery", "raz", "raz"])
    display_inventory(inventory)
    print('TTT')
    remove_from_inventory(inventory, ["pięć"])
    display_inventory(inventory)
