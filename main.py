
def welcome_message():
    print("Welcome to BARAKUDA bank!")

def main_menu():
    while True:
        print("Main Menu")
        print("1. Customer")
        print("2. Admin")
        print("3. Exit")
        
        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == '1':
            customer.handle_customer()
        elif choice == '2':
            admin.handle_admin()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Error, please choose 1, 2, or 3.")

if __name__ == "__main__":
    main_menu()

import admin 

import customer 