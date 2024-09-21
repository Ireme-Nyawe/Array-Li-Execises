# Program to create a shopping list and remove an item from the list

shopping_list = ["Rice", "Potato", "Beans"]

print("Current Shopping List:")
for item in shopping_list:
    print(item)

item_to_remove = input("Enter an Item to remove,:")
if item_to_remove in shopping_list:
    shopping_list.remove(item_to_remove)
    print(f"\n{item_to_remove} has been removed from the shopping list.")
else:
    print(f"\n{item_to_remove} is not in the shopping list.")

print("\nUpdated Shopping List:")
for item in shopping_list:
    print(item)
