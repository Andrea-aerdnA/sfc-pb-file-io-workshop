import json


class ContactManager:
    def __init__(self, file="data.json"):
        self.file = file

    def load_contacts(self):
        return self._load_contacts_from_file()

    def add_contact(self, contact):
        pass

    def update_contact(self, contact_to_update):
        pass

    def delete_contact(self, id_to_delete):
        pass

    # these are "private" methods below. They are not meant to be called
    # from outside the class, but are likely useful in the methods above.
    def _load_contacts_from_file(self):
        return []

    def _save_contacts_to_file(self, contacts):
        pass
