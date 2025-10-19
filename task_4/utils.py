# Utility functions for contact management bot application 

def parse_input(user_input: str):
    cmd, *args = user_input.split() # Split input into command and arguments
    cmd = cmd.strip().lower() # Normalize command to lowercase
    return cmd, *args # Return command and arguments

# Function to add a new contact
def add_contact(args: list[str], contacts: dict[str, str]) -> str:
    if len(args) != 2: # Check for exactly two arguments
        return "Invalid number of arguments."
    
    name, phone = args
    contacts[name] = phone
    return "Contact added."

# Function to change an existing contact's phone number
def change_contact(args: list[str], contacts: dict[str, str]) -> str:
    if len(args) != 2: # Check for exactly two arguments
        return "Invalid number of arguments."
    
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Contact not found."

# Function to show a contact's phone number
def show_phone(args: list[str], contacts: dict[str, str]) -> str:
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return "Contact not found."

# Function to show all contacts
def show_all(contacts: dict[str, str]) -> str:
    if not contacts:
        return "No contacts found."
    result = ""
    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"
    return result.strip()