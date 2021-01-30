import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    database="my_contact_book")


mycursor = mydb.cursor()


mycursor.execute("SELECT * FROM contacts")

for x in mycursor:
    print(x)