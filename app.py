import mysql.connector

# Connecting python to MySQL server, database
dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123",
    database="School"
)

cursorObject = dataBase.cursor()

cursorObject.execute("SELECT * FROM STUDENT")
records = cursorObject.fetchall()

# Function to create a new record in STUDENT


def addStudent():
    firstName = input("First Name:  ")
    lastName = input("Last Name:  ")
    grade = input("Class (1-12):  ")
    section = input("Section/Stream:  ")
    dob = input("Date of Birth (yyyy-mm-dd):  ")
    contact = input("Contact Number:  ")
    motherName = input("Mother's Name:  ")
    fatherName = input("Father's Name:  ")
    address = input("Address: ")

    sql = "INSERT INTO STUDENT (FIRST_NAME, LAST_NAME, CLASS, SECTION, DOB, CONTACT_NO, MOTHER_NAME, FATHER_NAME, ADDRESS)\
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (firstName, lastName, grade, section, dob,
           contact, motherName, fatherName, address)
    cursorObject.execute(sql, val)
    dataBase.commit()

    sql2 = "SELECT * FROM STUDENT WHERE FIRST_NAME = %s AND DOB = %s AND ADDRESS = %s;"
    val2 = (firstName, dob, address)

    cursorObject.execute(sql2, val2)
    lastRow = cursorObject.fetchone()
    print(lastRow)

    tableName = "STUDENT_" + str(lastRow[0])
    print(tableName)
    cursorObject.execute("CREATE TABLE IF NOT EXISTS " + tableName + " (SR_NO INT AUTO_INCREMENT, DATE DATE UNIQUE, TIME TIME, PRIMARY KEY(SR_NO));")


# Main Menu
print("=======================================================")
print("SELECT YOUR OPERATION")
print("=======================================================")
print("1. Add New Student")
operation = input()

if operation == '1':
    addStudent()

# disconnecting from server
dataBase.close()
