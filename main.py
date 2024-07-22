from data_loader import DataLoader
from email import Email


def display_emails(emails):
    print("Emails:")
    for email in emails:
        print(email)

def main():
    data_loader = DataLoader()

    while True:
        print("\nOptions:")
        print("1. Display emails")
        print("2. Add new email")
        print("3. Update email")
        print("4. Delete email")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            emails = data_loader.load()
            display_emails(emails)

        elif choice == "2":
            id = input("Enter email ID: ")
            sender = input("Enter sender: ")
            recipient = input("Enter recipient: ")
            subject = input("Enter subject: ")
            body = input("Enter body: ")
            new_email = Email(id, sender, recipient, subject, body)
            data_loader.create(new_email.to_dict())

        elif choice == "3":
            id = input("Enter the email ID of the email to update: ")
            new_sender = input("Enter new sender: ")
            new_recipient = input("Enter new recipient: ")
            new_subject = input("Enter new subject: ")
            new_body = input("Enter new body: ")
            new_email = Email(id, new_sender, new_recipient, new_subject, new_body) # sanitize data
            data_loader.update_by_id(id, new_email.sender, new_email.recipient, new_email.subject, new_email.body)

        elif choice == "4":
            id = input("Enter the email ID of the email to delete: ")
            data_loader.delete_by_id(id)

        elif choice == "5":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
