import json


class ContactManager:
    def __init__(self, file="data.json"):
        self.file = file

    def load_contacts(self):
        return self._load_contacts_from_file()
    
    def add_contact(self, contact):
        contacts = self.load_contacts()
        contacts.append(contact)
        self._save_contacts_to_file(contacts)

    def update_contact(self, contact_to_update):
        contacts = self._load_contacts_from_file()
        for i, contact in enumerate(contacts):
            if contact["id"] == contact_to_update["id"]:
                contacts[i] = contact_to_update
                break
        self._save_contacts_to_file(contacts)

    def delete_contact(self, id_to_delete):
        contacts = self._load_contacts_from_file()
        contacts = [
            contact for contact in contacts if contact["id"] != id_to_delete
        ]
        self._save_contacts_to_file(contacts)

    # these are "private" methods below. They are not meant to be called
    # from outside the class
    def _load_contacts_from_file(self):
        contacts = []
        with open(self.file, "r") as f:
            contacts = json.load(f)        
        return contacts

    def _save_contacts_to_file(self, contacts):
        with open(self.file, "w") as f:
            json.dump(contacts, f)
