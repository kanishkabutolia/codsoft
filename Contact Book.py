#Contact Book
#Contact Information: Store name, phone number, email, and address for each contact.
#Add Contact: Allow users to add new contacts with their details.
#View Contact List: Display a list of all saved contacts with names and phone numbers.
#Search Contact: Implement a search function to find contacts by name or phone number.
#Update Contact: Enable users to update contact details.
#Delete Contact: Provide an option to delete a contact.
#User Interface: Design a user-friendly interface for easy interaction.

contacts = []

def add_contact():
    name = input("Enter the name: ")
    phone = input("Enter the phone number: ")
    email = input("Enter the email: ")
    address = input("Enter the address: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }
    contacts.append(contact)
    print("Contact added successfully!")

def view_contacts():
    if not contacts:      
        print("No contacts found!")
    else:
        print("\nContact List:\n")
        for contact in contacts:
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}")

def search_contact():
    search_term = input("Enter name or phone number to search: ")
    found_contacts = [contact for contact in contacts if search_term.lower() in contact['name'].lower() or search_term in contact['phone']]

    if found_contacts:
        print("Search Results:")
        for contact in found_contacts:
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}")
    else:
        print("No matching contacts found!")

def update_contact():
    view_contacts()
    name = input("Enter the name of the contact to update: ")
    found_contact = next((contact for contact in contacts if contact['name'].lower() == name.lower()), None)

    if found_contact:
        print(f"Current details for {name}:")
        print(f"Name: {found_contact['name']}, Phone: {found_contact['phone']}, Email: {found_contact['email']}, Address: {found_contact['address']}")

        new_name = input("Enter the new name (or press Enter to keep current): ") or found_contact['name']
        new_phone = input("Enter the new phone number (or press Enter to keep current): ") or found_contact['phone']
        new_email = input("Enter the new email (or press Enter to keep current): ") or found_contact['email']
        new_address = input("Enter the new address (or press Enter to keep current): ") or found_contact['address']

        found_contact['name'] = new_name
        found_contact['phone'] = new_phone
        found_contact['email'] = new_email
        found_contact['address'] = new_address
        print("Contact updated successfully!")
    else:
        print("Contact not found!")

def delete_contact():
    view_contacts()
    name = input("Enter the name of the contact to delete: ")
    found_contact = next((contact for contact in contacts if contact['name'].lower() == name.lower()), None)

    if found_contact:
        contacts.remove(found_contact)
        print("Contact deleted successfully!")
    else:
        print("Contact not found!")

def main():
    while True:
        print("\nContact Manager")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Thank you for using the Contact Manager!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
