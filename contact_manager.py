import json

"""
Note: This is designed to hold a list of contacts as a list of dictionaries.
An alternative approach is to build a "Contact" class to represent a contact.
If you would like to do that as a Bonus exercise, that would be good way
to practice using OOP and composition!
"""
import io
import json
import os

class ContactManager:
    """Class to do CRUD operations on the list of contacts"""

    def __init__(self, file="data.json"):
        self.file = file
        self.contacts = []
        self.load_contacts()

    def load_contacts(self):
        if not os.path.exists(self.file):
            print(f"Warning: '{self.file}' not found.")
            self.contacts = []
            return self.contacts

        try:
            with io.open(self.file, 'r') as file:
                self.contacts = json.load(file)
        except json.JSONDecodeError:
            print(f"Warning: '{self.file}' invalid JSON")
            self.contacts = []
            self.save_contacts()

        return self.contacts



    def add_contact(self, contact):
        for saved_contact in self.contacts:
            if saved_contact['id'] == contact['id']:
                print('Contact ID already exists.')
                return

        self.contacts.append(contact)
        self.save_contacts()




    def update_contact(self, contact_to_update):
        """
        Updates a contact an saves the file
        Bonus: What happens when the id doesn't exist?
        """
        contacts_to_save = []
        for contact in self.contacts:
            if contact['id'] == contact_to_update['id']:
                contacts_to_save.append(contact_to_update)
            else:
                contacts_to_save.append(contact)

        self.contacts = contacts_to_save
        self.save_contacts()



    def delete_contact(self, id_to_delete):
        """
        Deletes a contact and saves the file
        Bonus: What happens when the id doesn't exist?
        """
        contacts_to_save = []
        for contact in self.contacts:
            if contact['id'] != id_to_delete:
                contacts_to_save.append(contact)

        self.contacts = contacts_to_save
        self.save_contacts()


    def save_contacts(self):
        with io.open(self.file, 'w') as file:
            json.dump(self.contacts, file)

