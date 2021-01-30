from Contact import Contact
import mysql.connector



class AddingToBook:
    def create_new_contact(name, phone, email, address):
        contact = Contact(name, phone, email, address)
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            database="my_contact_book")

        mycursor = mydb.cursor()
        sql = "INSERT INTO contacts (Name, Phone, EmailID, Address) VALUES (%s, %s, %s, %s)"
        val = (contact.name, contact.phone, contact.email, contact.address)
        mycursor.execute(sql, val)

        mydb.commit()
    def update_existing_contact(finder_keys, finder_values, tbc_keys, new_values):
        # still need to work on this
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            database="my_contact_book")

        mycursor = mydb.cursor()
        command = "UPDATE contacts set "
        for tbc_key in tbc_keys:
            command += tbc_key
            command += '='
            command += '\''
            command += new_values[tbc_keys.index(tbc_key)]
            command += '\''
            if tbc_keys[-1] != tbc_key:
                command += ', '
        command += ' WHERE '
        for finder_key in finder_keys:
            command += finder_key
            command += '='
            command += '\''
            command += finder_values[finder_keys.index(finder_key)]
            command += '\''
            if tbc_keys[-1] != tbc_key:
                command += ', '
            else:
                command += ';'
        mycursor.execute(command)
        mydb.commit()

