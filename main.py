from contact_manager import ContactManager


def display_contacts(contacts):
    print("Contacts:")
    for contact in contacts:
        print(str(contact))

def main():
    contact_manager = ContactManager()

    while True:
        print("\nOptions:")
        print("1. Display contacts")
        print("2. Add new contact")
        print("3. Update contact")
        print("4. Delete contact")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            contacts = contact_manager.load_contacts()
            display_contacts(contacts)

        elif choice == "2":
            id = input("Enter contact ID: ")
            name = input("Enter name: ")
            email = input("Enter email: ")
            phone = input("Enter phone: ")
            contact = {
                "id": id,
                "name": name,
                "email": email,
                "phone": phone
            }
            contact_manager.add_contact(contact)

        elif choice == "3":
            id = input("Enter the ID of the contact to update: ")
            name = input("Enter name: ")
            email = input("Enter email: ")
            phone = input("Enter phone: ")
            contact_to_update = {
                "id": id,
                "name": name,
                "email": email,
                "phone": phone
            }
            contact_manager.update_contact(contact_to_update)


        elif choice == "4":
            id = input("Enter the ID of the contact to delete: ")
            contact_manager.delete_contact(id)

        elif choice == "5":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
