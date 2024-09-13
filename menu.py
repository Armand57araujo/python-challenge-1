# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": 0.99,
        "Banana": 0.69,
        "Apple": 0.49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

# 1. Initialize the order list (2 points)
customer_order = []

# Launch the store and present a greeting to the customer
print("Welcome to the variety food truck.")

# Main loop to handle the customer's order process
place_order = True
while place_order:
    # Ask the customer from which menu category they want to order
    print("\nFrom which menu would you like to order?")

    # Display menu categories and store them in a dictionary
    i = 1
    menu_items = {}
    for key in menu.keys():
        print(f"{i}: {key}")
        menu_items[i] = key
        i += 1

    # 2. User prompted for menu selection and input saved (4 points)
    menu_selection = input("Type menu number: ")

    # 3. Check if the customer's input is a number (4 points)
    if menu_selection.isdigit():
        # 4. Convert menu_selection to integer (2 points)
        menu_selection = int(menu_selection)

        # 5. Check if the input is in the menu_items keys (4 points)
        if menu_selection in menu_items.keys():
            # Save the menu category name to a variable
            menu_category_name = menu_items[menu_selection]
            print(f"You selected {menu_category_name}")

            # Display menu items in the selected category
            print(f"What {menu_category_name} item would you like to order?")
            i = 1
            menu_selection_items = {}
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")
            for key, value in menu[menu_category_name].items():
                if isinstance(value, dict):  # Nested dictionary for some items
                    for subkey, subvalue in value.items():
                        num_item_spaces = 24 - len(f"{key} - {subkey}")
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {key} - {subkey}{item_spaces} | ${subvalue}")
                        menu_selection_items[i] = {
                            "Item name": f"{key} - {subkey}",
                            "Price": subvalue
                        }
                        i += 1
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value}")
                    menu_selection_items[i] = {
                        "Item name": key,
                        "Price": value
                    }
                    i += 1

            # 6. Ask customer to input menu item number
            menu_item_selection = input("Please select an item number: ")

            # Check if the customer typed a number
            if menu_item_selection.isdigit():
                menu_item_selection = int(menu_item_selection)

                # Check if the menu selection is in the menu items
                if menu_item_selection in menu_selection_items.keys():
                    # 7. Extract item name from the selected item (4 points)
                    selected_item = menu_selection_items[menu_item_selection]
                    item_name = selected_item["Item name"]
                    item_price = selected_item["Price"]

                    # 8. Prompt for quantity, default to 1 if invalid (10 points)
                    quantity = input(f"How many {item_name}(s) would you like? (default 1): ")

                    # Validate quantity input, default to 1 if invalid
                    if not quantity.isdigit():
                        quantity = 1
                    else:
                        quantity = int(quantity)

                    # 9. Append the item, price, and quantity to the order list (10 points)
                    customer_order.append({
                        "Item name": item_name,
                        "Price": item_price,
                        "Quantity": quantity
                    })
                    print(f"{quantity} {item_name}(s) added to your order.")
                else:
                    print("Invalid selection. Please select a valid menu item number.")
            else:
                print("You didn't select a number.")
        else:
            print("You didn't select a valid menu option.")
    else:
        print("You didn't select a number.")

    # 10. Ask the customer if they would like to keep ordering (10 points)
    while True:
        keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o: ").lower()

        # 11. Use match-case statement to check the user's input (10 points)
        match keep_ordering:
            case 'y':
                break  # Continue ordering
            case 'n':
                place_order = False  # Stop ordering
                print("Thank you for your order.")
                break
            case _:
                print("Invalid input. Please type 'Y' or 'N'.")

# 12. Order Receipt
print("\nThis is what we are preparing for you:")
print("Item name                 | Price  | Quantity")
print("--------------------------|--------|----------")

# 13. Loop through the items in the customer's order and print receipt (10 points)
for item in customer_order:
    # 14. Save dictionary values as variables (6 points)
    item_name = item["Item name"]
    price = item["Price"]
    quantity = item["Quantity"]

    # 15. Calculate spaces for formatted printing (6 points)
    item_space = " " * (26 - len(item_name))
    price_space = " " * (6 - len(f"{price:.2f}"))

    # 16. Print the item name, price, and quantity (6 points)
    print(f"{item_name}{item_space}| ${price:.2f}{price_space}| {quantity}")

# 17. Calculate total price using list comprehension (10 points)
total = sum(item['Price'] * item['Quantity'] for item in customer_order)
print("--------------------------|--------|----------")
# 18. Print total price (4 points)
print(f"Total: ${total:.2f}")
