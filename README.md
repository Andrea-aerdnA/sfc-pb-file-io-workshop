# File IO Lab

Welcome to the File IO lab!

In this challenge you'll have a runner file (`main.py`) that keeps track of
emails and uses an `Email` class and a `DataLoader` class. The runner and the
`Email` class are already implemented for you. Your job is to implement the
`DataLoader` class so that the runner works as expected. Below is a sample of a
session with the runner class working for you to use as a test case:

```sh
15:37:55 ~/unit-1-file-io-lab $ python main.py

Options:
1. Display emails
2. Add new email
3. Update email
4. Delete email
5. Exit
Enter your choice: 1
Emails:

Options:
1. Display emails
2. Add new email
3. Update email
4. Delete email
5. Exit
Enter your choice: 2
Enter email ID: 1
Enter sender: me@email.com
Enter recipient: you@email.com
Enter subject: file io
Enter body: daaannnngggg! you got this whole thing working! nice work

Options:
1. Display emails
2. Add new email
3. Update email
4. Delete email
5. Exit
Enter your choice: 1
Emails:
{'id': '1', 'sender': 'me@email.com', 'recipient': 'you@email.com', 'subject': 'file io', 'body': 'daaannnngggg! you got this whole thing working! nice work'}

Options:
1. Display emails
2. Add new email
3. Update email
4. Delete email
5. Exit
Enter your choice: 3
Enter the email ID of the email to update: 1
Enter new sender: me@email.com
Enter new recipient: you@email.com
Enter new subject: file io
Enter new body: daaannnngggg! you got this whole thing working! nice work!!!!!!!

Options:
1. Display emails
2. Add new email
3. Update email
4. Delete email
5. Exit
Enter your choice: 1
Emails:
{'id': '1', 'sender': 'me@email.com', 'recipient': 'you@email.com', 'subject': 'file io', 'body': 'daaannnngggg! you got this whole thing working! nice work!!!!!!!'}

Options:
1. Display emails
2. Add new email
3. Update email
4. Delete email
5. Exit
Enter your choice: 4
Enter the email ID of the email to delete: 1

Options:
1. Display emails
2. Add new email
3. Update email
4. Delete email
5. Exit
Enter your choice: 1
Emails:

Options:
1. Display emails
2. Add new email
3. Update email
4. Delete email
5. Exit
Enter your choice: 5
Exiting program.
```
