def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")
def add_item():
    item = input("Enter the item to add: ")
    shopping_list.append(item)
def remove_item():
    item = input("Enter the item to remove: ")
    if item in shopping_list:
        shopping_list.remove(item)
def view_list():
    if not shopping_list:
        print("The shopping list is empty.")
    else:
        print("Shopping List:")
        for i, item in enumerate(shopping_list, 1):
            print(f"{i}. {item}")
def main():
    global shopping_list
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_item()
            pass
        elif choice == '2':
            remove_item()
            pass
        elif choice == '3':
            view_list()
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()