# Utility functions for contact management bot application 
from decorators import input_error

def parse_input(user_input: str):
    cmd, *args = user_input.split() # Split input into command and arguments
    cmd = cmd.strip().lower() # Normalize command to lowercase
    return cmd, *args # Return command and arguments

# Function to add a new contact
@input_error
def add_contact(args: list[str], contacts: dict[str, str]) -> str:
    name, phone = args  # This will raise ValueError if not enough arguments
    contacts[name] = phone
    return "Contact added."

# Function to change an existing contact's phone number
@input_error
def change_contact(args: list[str], contacts: dict[str, str]) -> str:
    name, phone = args  # This will raise ValueError if not enough arguments
    contacts[name] = phone
    return "Contact updated."

# Function to show a contact's phone number
@input_error
def show_phone(args: list[str], contacts: dict[str, str]) -> str:
    name = args[0]  # This will raise IndexError if no arguments provided
    return contacts[name]

# Function to show all contacts
@input_error
def show_all(contacts: dict[str, str]) -> str:
    if not contacts:
        return "No contacts found."
    result = ""
    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"
    return result.strip()