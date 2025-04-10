contacts = {'1234': 'abcd', '3456': 'defg', '7890': 'ghij'}

def show_contacts():
    if len(contacts) == 0:
        print("\nNO CONTACTS TO SHOW...")
    else:
        print("\nSR  MONO     NAME")
        srno = 1
        for mono, name in contacts.items():
            print(f"{srno:<3} {mono:<8} {name}")
            srno += 1

def add_contact():
    mono = input("Enter Mobile Number To Add: ")
    if mono in contacts:
        print("\nCONTACT ALREADY EXISTS...")
    else:
        name = input("Enter Name To Add: ")
        contacts[mono] = name
        print("\nCONTACT ADDED SUCCESSFULLY...")

def delete_contact():
    mono = input("Enter Mobile Number To Delete: ")
    if mono in contacts:
        contacts.pop(mono)
        print("\nCONTACT DELETED SUCCESSFULLY...")
    else:
        print("\nCONTACT NOT FOUND...")

def update_contact():
    mono = input("Enter Mobile Number To Update: ")
    if mono in contacts:
        name = input("Enter Updated Name: ")
        contacts[mono] = name
        print("\nCONTACT UPDATED SUCCESSFULLY...")
    else:
        print("\nCONTACT NOT FOUND...")
def search_contact():
    query = input("Enter Number or Name to Search: ").lower()
    found = False
    for mono, name in contacts.items():
        if query in mono or query in name.lower():
            print(f"\nFound: {mono} - {name}")
            found = True
    if not found:
        print("\nNO MATCH FOUND...")

# Menu-driven loop
try:
    while True:
        print("\n------ CONTACT MANAGER ------")
        print("1. Show Contacts")
        print("2. Add Contact")
        print("3. Delete Contact")
        print("4. Update Contact")
        print("5. Search Contact")
        print("6. Exit")
        choice = input("Enter Your Choice (1-5): ")

        if choice == '1':
            show_contacts()
        elif choice == '2':
            add_contact()
        elif choice == '3':
            delete_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            search_contact()
        elif choice == '6':
            print("\nExiting Contact Manager... Goodbye!")
            break
        else:
            print("\nINVALID CHOICE. PLEASE TRY AGAIN.")
except KeyboardInterrupt:
    print("\n\nProgram interrupted. Exiting Contact Manager... Goodbye!")
