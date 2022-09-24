import mysql.connector

# Connecting python to MySQL server, database
dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123",
    database="School"
)

cursorObject = dataBase.cursor()