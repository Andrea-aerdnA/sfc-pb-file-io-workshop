import json

"""
Note: This is designed to hold a list of contacts as a list of dictionaries.
An alternative approach is to build a "Contact" class to represent a contact.
If you would like to do that as a Bonus exercise, that would be good way
to practice using OOP and composition!
"""


class ContactManager:
    """Class to do CRUD operations on the list of contacts"""

    def __init__(self, file="data.json"):
        self.file = file
        # _contacts is protected because we don't want to
        # access it directly from main.py
        self._contacts: list[dict[str, str]] = []

    def load_contacts(self) -> list[dict[str, str]]:
        """Public method to load the contacts into the class"""
        return self._load_contacts_from_file()

    def add_contact(self, contact: dict[str, str]) -> None:
        """Adds a contact to the list, and saves the file"""
        pass

    def update_contact(self, contact_to_update: dict[str, str]) -> None:
        """
        Updates a contact an saves the file

        Bonus: What happens when the id doesn't exist?
        """
        pass

    def delete_contact(self, id_to_delete: str) -> None:
        """
        Deletes a contact and saves the file

        Bonus: What happens when the id doesn't exist?
        """
        pass

    # these are "protected" methods below. They are not meant to be called
    # from outside the class, but are likely useful in the methods above.
    def _load_contacts_from_file(self) -> list[dict[str, str]]:
        """
        Loads contacts from a JSON file and converts them to a dictionary

        Bonus: What should happen if the file isn't there?
               What should happen if the file has invalid JSON in it?
        """
        return []

    def _save_contacts_to_file(self, contacts: list[dict[str, str]]) -> None:
        """
        Converts a dictionary into JSON and writes it to a file

        Bonus: What happens if the file can't be written to?
               Check the list of dictionaries for valid data before
               saving it to the file
        """
        pass
