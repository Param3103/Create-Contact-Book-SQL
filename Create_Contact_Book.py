import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    database="my_contact_book")


mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE my_contact_book")

# new database created dont run this code again


# mycursor.execute("CREATE TABLE contacts(Name varchar(200), Phone varchar(50), EmailID varchar(1000), Address varchar(1000));")
# new table created dont run this code again

mycursor.execute("SHOW TABLES")

for x in mycursor:
    print(x)

    # done