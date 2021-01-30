import mysql.connector

class RetrievingFromBook:
    def find_contact(finder_keys, finder_values):

        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            database="my_contact_book")

        mycursor = mydb.cursor()

        for finder_value in finder_values:
            if finder_value is not None:
                if finder_keys[finder_values.index(finder_value)] == 'Name':
                    mycursor.execute("SELECT * FROM contacts WHERE Name = '{0}';".format(finder_value))
                elif finder_keys[finder_values.index(finder_value)] == 'Phone':
                    mycursor.execute("SELECT * FROM contacts WHERE Phone = '{0}';".format(finder_value))
                elif finder_keys[finder_values.index(finder_value)] == 'EmailID':
                    mycursor.execute("SELECT * FROM contacts WHERE emailid = '{0}';".format(finder_value))
                elif finder_keys[finder_values.index(finder_value)] == 'Address':
                    mycursor.execute("SELECT * FROM contacts WHERE address = '{0}';".format(finder_value))
            else:
                if finder_keys[finder_values.index(finder_value)] == 'Name':
                    mycursor.execute("SELECT * FROM contacts WHERE Name is NULL;")
                elif finder_keys[finder_values.index(finder_value)] == 'Phone':
                    mycursor.execute("SELECT * FROM contacts WHERE Phone is NULL;")
                elif finder_keys[finder_values.index(finder_value)] == 'EmailID':
                    mycursor.execute("SELECT * FROM contacts WHERE emailid is NULL;")
                elif finder_keys[finder_values.index(finder_value)] == 'Address':
                    mycursor.execute("SELECT * FROM contacts WHERE address is NULL;")

        for x in mycursor:
            print(x)