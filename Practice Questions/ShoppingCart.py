preset_prices = {
    "Apples": 3.50,
    "Bananas": 2.25,
    "Milk": 1.50,
    "Bread": 2.75,
    "Eggs": 4.00,
    "Rice": 5.00
}

def show_menu():
    print("\nOptions:")
    print("1. Add an item")
    print("2. Remove an item")
    print("3. View shopping list")
    print("4. Submit and get the bill")
    print("5. Exit")

def add_item(shopping_list):
    print("\nAvailable items and their prices:")
    for item, price in preset_prices.items():
        print(f"{item}: ${price:.2f}")

    item = input("\nEnter the item name to add: ")
    if item in preset_prices:
        shopping_list[item] = preset_prices[item]
        print(f"{item} added to your shopping list.")
    else:
        print(f"Sorry, {item} is not available.")

def remove_item(shopping_list):
    item = input("Enter the item name to remove: ")
    if item in shopping_list:
        del shopping_list[item]
        print(f"{item} removed from your shopping list.")
    else:
        print(f"{item} is not in your list.")

def view_list(shopping_list):
    if shopping_list:
        print("\nYour Shopping List:")
        for item, price in shopping_list.items():
            print(f"{item}: ${price:.2f}")
    else:
        print("\nYour shopping list is empty.")

def get_total_bill(shopping_list):
    total = sum(shopping_list.values())
    print("\nFinal Shopping List:")
    for item, price in shopping_list.items():
        print(f"{item}: ${price:.2f}")
    print(f"\nTotal bill: ${total:.2f}")
    print("Thank you for shopping!")

def main():
    shopping_list = {}
    while True:
        show_menu()
        choice = input("\nEnter your choice (1-5): ")

        if choice == '1':
            add_item(shopping_list)
        elif choice == '2':
            remove_item(shopping_list)
        elif choice == '3':
            view_list(shopping_list)
        elif choice == '4':
            if shopping_list:
                view_list(shopping_list)
                get_total_bill(shopping_list)
            else:
                print("\nYour shopping list is empty. Nothing to bill.")
            break
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please choose again.")

main()