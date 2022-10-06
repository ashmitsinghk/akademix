import mysql.connector

# Connecting python to MySQL server, database
dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1234",
    database="School"
)

cursorObject = dataBase.cursor()