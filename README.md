# File IO Lab

Welcome to the File IO lab!

In this challenge you will build a simple contact manager. A `main.py` main
program file has already been completed, you just need to implement the
methods in the `ContactManager` class in `contact_manager.py`. At the bottom
of this page is a sample session with contact manager program.

```sh
~/unit-1-file-io-lab $ python main.py

Options:
1. Display contacts
2. Add new contact
3. Update contact
4. Delete contact
5. Exit
Enter your choice: 1
Contacts:

Options:
1. Display contacts
2. Add new contact
3. Update contact
4. Delete contact
5. Exit
Enter your choice: 2
Enter contact ID: 1
Enter name: joe
Enter email: joe@bro.com
Enter phone: 111-111-1111

Options:
1. Display contacts
2. Add new contact
3. Update contact
4. Delete contact
5. Exit
Enter your choice: 1
Contacts:
{'id': '1', 'name': 'joe', 'email': 'joe@bro.com', 'phone': '111-111-1111'}

Options:
1. Display contacts
2. Add new contact
3. Update contact
4. Delete contact
5. Exit
Enter your choice: 3
Enter the ID of the contact to update: 1
Enter name: joseph
Enter email: joseph@bro.com
Enter phone: 111-111-1111

Options:
1. Display contacts
2. Add new contact
3. Update contact
4. Delete contact
5. Exit
Enter your choice: 1
Contacts:
{'id': '1', 'name': 'joseph', 'email': 'joseph@bro.com', 'phone': '111-111-1111'}

Options:
1. Display contacts
2. Add new contact
3. Update contact
4. Delete contact
5. Exit
Enter your choice: 4
Enter the ID of the contact to delete: 1

Options:
1. Display contacts
2. Add new contact
3. Update contact
4. Delete contact
5. Exit
Enter your choice: 1
Contacts:

Options:
1. Display contacts
2. Add new contact
3. Update contact
4. Delete contact
5. Exit
Enter your choice: 5
Exiting program.
```
