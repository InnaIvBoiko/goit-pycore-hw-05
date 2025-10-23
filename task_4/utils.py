"""Utility functions for contact management bot application."""
from decorators import input_error

def parse_input(user_input: str):
    """Parse user input into command and arguments.
    
    Args:
        user_input (str): Raw user input string
        
    Returns:
        tuple: Command and arguments
    """
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args: list[str], contacts: dict[str, str]) -> str:
    """Add a new contact to the contacts dictionary.
    
    Args:
        args (list[str]): List containing name and phone number
        contacts (dict[str, str]): Dictionary of contacts
        
    Returns:
        str: Success message
        
    Raises:
        ValueError: If not enough arguments provided
    """
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args: list[str], contacts: dict[str, str]) -> str:
    """Change an existing contact's phone number.
    
    Args:
        args (list[str]): List containing name and new phone number
        contacts (dict[str, str]): Dictionary of contacts
        
    Returns:
        str: Success message
        
    Raises:
        ValueError: If not enough arguments provided
    """
    name, phone = args
    contacts[name] = phone
    return "Contact updated."


@input_error
def show_phone(args: list[str], contacts: dict[str, str]) -> str:
    """Show a contact's phone number.
    
    Args:
        args (list[str]): List containing contact name
        contacts (dict[str, str]): Dictionary of contacts
        
    Returns:
        str: Contact's phone number
        
    Raises:
        IndexError: If no arguments provided
        KeyError: If contact not found
    """
    name = args[0]
    return contacts[name]


@input_error
def show_all(contacts: dict[str, str]) -> str:
    """Show all contacts in the contacts dictionary.
    
    Args:
        contacts (dict[str, str]): Dictionary of contacts
        
    Returns:
        str: Formatted string of all contacts or message if no contacts found
    """
    if not contacts:
        return "No contacts found."
    result = ""
    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"
    return result.strip()