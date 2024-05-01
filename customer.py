def handle_customer():
    print("Welcome to the Customer Page")

handle_customer()

import logging

logging.basicConfig(filename='customer_page.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Customer:
    def __init__(self, first_and_last_name, date_of_birth, address, phone_number):
        self.name = first_and_last_name
        self.date_of_birth = date_of_birth
        self.address = address
        self.phone_number = phone_number
        self.documents = []

        # Log the creation of a new customer
        logging.info(f"New customer created - Name: {self.name}")

    def upload_document(self, document):
        self.documents.append(document)
        logging.info(f"Document uploaded for customer {self.name}: {document}")


# Add Customer 

customer_choice = input("Are you a new customer? (yes/no): ").lower()
if customer_choice == "yes":
    first_and_last_name = input("Enter your First and Last name: ")
    date_of_birth = input("Enter your date of birth: ")
    address = input("Enter your address: ")
    phone_number = input("Enter your phone number: ")
    new_customer = Customer(first_and_last_name, date_of_birth, address, phone_number)
    upload_documents = int(input("Upload your document: "))
    for i in range(upload_documents):
        document = input(f"Enter document {i+1}: ")
        new_customer.upload_document(document)
    
    print("Documents uploaded successfully! Wait for the confirmation. We are contacting you as soon is possible")
    exit()

elif customer_choice == "no":
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    # Here you can implement login logic to retrieve existing customer information and perform actions

else:
    print("Invalid choice.")

# Customer info
customer_information = {
"user1": {"username": "Spange Bob", "password": "1111", "date_of_birth": "01.01.2000", "address": "Bikini Bottom","phone_number": "1234" }} 

def login_customer( username, password):
    if username == "Spange Bob" and password == "1111":
        print("Welcome back, Spange Bob!")
    else:
        print("Incorrect username or password.")

login_customer(username, password)