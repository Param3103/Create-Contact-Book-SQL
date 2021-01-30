from Adding_To_Book import AddingToBook
from Retreiving_From_Book import RetrievingFromBook

task = int(input("What do you want to do?  \nPress 1 for accessing contact. \nPress 2 for updating existing contact. \nPress 3 for creating new contact."))
while task not in range(1, 4):
    task = int(input("Error! \nPress 1 for accessing contact. \nPress 2 for updating existing contact. \nPress 3 for creating new contact. "))
if task == 1:
    print("Accessing contact")
    finding_keys = []
    finding_values = []
    continue_to_find = True
    while continue_to_find:
        type = input("What kind of detail do you have? \nPlz input Name, Phone No, Email ID, or Address.")
        if type == ("Name" or "name") and "Name" not in finding_keys:
            finding_keys.append('Name')
            value = input("Plz input the name. ")
            finding_values.append(value)
        elif type == ("Phone No" or "PhoneNo" or "phone no" or "phoneno" or "Phone no" or "Phoneno" or "phone No" or "phoneNo") and 'Phone No' not in finding_keys:
            finding_keys.append('Phone No')
            value = input("Plz input the phone no. ")
            finding_values.append(value)
        elif type == ("Email ID" or "Email id" or "Email Id" or "Email iD" or "email ID" or "EMAIL ID" or "email id" or "EmailID" or "emailID") and 'Email ID' not in finding_keys:
            finding_keys.append('Email ID')
            value = input("Plz input the email id. ")
            finding_values.append(value)
        elif type == ("Address" or "address") and 'Address' not in finding_keys:
            finding_keys.append('Address')
            value = input("Plz input the address. ")
            finding_values.append(value)
        else:
            print("Error!")
        to_continue = input("do you have any more details you want to give? y/n ")
        while (to_continue != "y") and (to_continue != 'n'):
            to_continue = input("do you have any more details you want to give? y/n ")
        if to_continue == 'n':
            continue_to_find = False
            continue
        else:
            continue
    RetrievingFromBook.find_contact(finding_keys, finding_values)

elif task == 2:
    print("Updating existing contact")
    num_identifying_keys = int(input('How many details do you have to identify the contact you need to update? '))
    identifying_keys = []
    identifying_values = []
    for num in range(num_identifying_keys):
        identifying_key = input('what kind of detail do you have? \nName, Phone, EmailID or Address. Plz input in same form.')
        identifying_keys.append(identifying_key)
        identifying_value = input('Plz input the contact detail now. ')
        identifying_values.append(identifying_value)
    num_tbc_keys = int(input('How many details of this contact do you want to change? '))
    tbc_keys = []
    new_values = []
    for num in range(num_tbc_keys):
        tbc_key = input('what kind of detail do you want to change? \nName, Phone, EmailID or Address. Plz input in same form.')
        tbc_keys.append(tbc_key)
        new_value = input('Plz input the new contact detail now. ')
        new_values.append(new_value)
    AddingToBook.update_existing_contact(identifying_keys, identifying_values, tbc_keys, new_values)
elif task == 3:
    print("Creating new contact")
    print(" ")
    name = input("Plz input name of contact. Plz leave blank if you don't have the name. ")
    phone = input("Plz input phone number of contact. Plz leave blank if you don't have the phone number. ")
    email = input("Plz input email of contact. Plz leave blank if you don't have the email. ")
    address = input("Plz input address of contact. Plz leave blank if you don't have the address. ")
    AddingToBook.create_new_contact(name, phone, email, address)