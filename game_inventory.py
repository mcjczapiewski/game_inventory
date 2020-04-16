
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
    the_longest_key = 0
    for key in inventory:
        if len(key) > the_longest_key:
            the_longest_key = len(key)
    if the_longest_key < len("item name"):
        the_longest_key = len("item name")
    number_of_dashes = the_longest_key + len(" | count")
    print("-" * number_of_dashes)
    print("item name".rjust(the_longest_key) + " | count")
    print("-" * number_of_dashes)
    if order.lower() == "count,desc":
        inventory = {
            key: value for key, value
            in sorted(inventory.items(), key=lambda x: x[1], reverse=True)
        }
    elif order.lower() == "count,asc":
        inventory = {
            key: value for key, value
            in sorted(inventory.items(), key=lambda x: x[1])
        }
    for item in inventory:
        print(
            item.rjust(the_longest_key)
            + " | "
            + str(inventory[item]).rjust(len("count"))
        )
    print("-" * number_of_dashes)
    pass


def import_inventory(inventory, filename):
    """Import new inventory items from a CSV file."""

    pass


def export_inventory(inventory, filename):
    """Export the inventory into a CSV file."""

    pass


if __name__ == "__main__":
    inventory = {"raz": 1, "dwa": 2, "osiem": 11, "dwadzieścia": 1948}
    display_inventory(inventory)
    print('TTT')
    add_to_inventory(inventory, ["raz", "dwa", "trzy", "trzy", "cztery", "trzy", "trzy"])
    display_inventory(inventory)
    print('TTT')
    remove_from_inventory(inventory, ["pięć"])
    display_inventory(inventory)
    print_table(inventory, "count,asc")
