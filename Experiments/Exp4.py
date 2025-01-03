class User:
    def __init__(self, user_id, name, address, phone_number):
        self.ShoppingList = {}
        self.user_id = user_id
        self.name = name
        self.address = address
        self.phone_number = phone_number

    def check_if_shopping_list_empty(self):
        return len(self.ShoppingList) > 0

    def print_user_and_shopping_details(self):
        output = "\nUser Details\n"
        output += f"ID >> {self.user_id}\n"
        output += f"Name >> {self.name}\n"
        output += f"Address >> {self.address}\n"
        output += f"Phone Number >> {self.phone_number}\n"
        output += "Shopping List >> \n"
        
        total = 0
        for item, price in self.ShoppingList.items():
            output += f"  - {item}: ${price}\n"
            total += price

        output += f"\nTotal Price: ${total}"
        return output

    def insert_items(self):
        while True:
            item = input("Enter Item (or type 'Exit' to stop) >> ").capitalize()
            if item == 'Exit':
                break
            price = input(f"Enter price for {item} >> ")
            if price.replace('.', '', 1).isdigit():  # Check for valid price format
                self.ShoppingList[item] = float(price)
            else:
                print("Invalid price. Please enter a valid number.")

    def remove_items(self):
        if not self.check_if_shopping_list_empty():
            print("\nYour Shopping List is Empty. Try Adding Some Items!")
            return
        print(f"Current List: {self.ShoppingList}")
        item = input("Enter item name to remove >> ").capitalize()
        if item in self.ShoppingList:
            del self.ShoppingList[item]
            print(f"{item} has been removed from your list")
        else:
            print(f"{item} doesn't exist on the shopping list")

    def update_items(self):
        if not self.check_if_shopping_list_empty():
            print("\nYour Shopping List is Empty. Try Adding Some Items!")
            return
        print(f"Current List: {self.ShoppingList}")
        prev_item = input("Enter the item to replace >> ").capitalize()
        updated_item = input("Enter the new item name >> ").capitalize()
        updated_price = input(f"Enter the price for {updated_item} >> ")
        
        if prev_item in self.ShoppingList and updated_price.replace('.', '', 1).isdigit():
            del self.ShoppingList[prev_item]
            self.ShoppingList[updated_item] = float(updated_price)
            print(f"Updated List >> {self.ShoppingList}")
        else:
            print("Invalid input or item does not exist in the list")


class UserManager:
    def __init__(self):
        self.users = []
        self.next_id = 1  # Simple integer ID for users

    def add_user(self, name, address, phone_number):
        if validate_phone_number(phone_number):
            new_user = User(self.next_id, name, address, phone_number)
            self.users.append(new_user)
            print(f"User {name} added successfully with ID {self.next_id}!")
            self.next_id += 1  # Increment the ID for the next user
        else:
            print("Invalid phone number. Please try again.")

    def show_users(self):
        if not self.users:
            print("No users found.")
            return
        for user in self.users:
            print(user.print_user_and_shopping_details())

    def find_user(self, user_id):
        for user in self.users:
            if user.user_id == user_id:
                return user
        print("User not found.")
        return None


def validate_phone_number(phone_number):
    # Validate if phone number is numeric and 10 or more digits
    return phone_number.isdigit() and len(phone_number) >= 10


# Main Program Execution
if __name__ == "__main__":
    manager = UserManager()
    while True:
        action = input("\nChoose an action: [Add User, Show Users, Exit] >> ").strip().lower()
        
        if action == 'add user':
            name = input("Enter Name: ")
            address = input("Enter Address: ")
            phone_number = input("Enter Phone Number: ")
            manager.add_user(name, address, phone_number)
            
        elif action == 'show users':
            manager.show_users()
            user_id_input = input("Enter User ID to manage their shopping list (or type 'back' to go back): ")
            
            if user_id_input.lower() == 'back':
                continue
            elif user_id_input.isdigit():
                user_id = int(user_id_input)
                user = manager.find_user(user_id)
                if user:
                    while True:
                        user_action = input(f"\nManaging {user.name}'s shopping list: [Insert, Remove, Update, Show, Back] >> ").strip().lower()
                        if user_action == 'insert':
                            user.insert_items()
                        elif user_action == 'remove':
                            user.remove_items()
                        elif user_action == 'update':
                            user.update_items()
                        elif user_action == 'show':
                            print(user.print_user_and_shopping_details())
                        elif user_action == 'back':
                            break
                        else:
                            print("Invalid action. Please try again.")
            else:
                print("Invalid User ID format.")
        
        elif action == 'exit':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid action. Please try again.")
