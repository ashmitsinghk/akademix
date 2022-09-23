from audioop import add
import mysql.connector

dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123",
    database="School"
)

cursorObject = dataBase.cursor()

# # creating table
# studentRecord = """CREATE TABLE STUDENT (
#                    STUDENT_ID INT NOT NULL AUTO_INCREMENT,
#                    FIRST_NAME  VARCHAR(15) NOT NULL,
#                    LAST_NAME VARCHAR(15) NOT NULL,
#                    CLASS INT NOT NULL,
#                    SECTION VARCHAR(10) NOT NULL,
#                    DOB DATE NOT NULL,
#                    CONTACT_NO BIGINT NOT NULL,
#                    ATTENDANCE INT,
#                    MOTHER_NAME VARCHAR(30) NOT NULL,
#                    FATHER_NAME VARCHAR(30) NOT NULL,
#                    ADDRESS VARCHAR(150) NOT NULL,
#                    PRIMARY KEY(STUDENT_ID)
#                    )"""

# # table created
# cursorObject.execute(studentRecord)


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


print("=======================================================")
print("SELECT YOUR OPERATION")
print("=======================================================")
print("1. Add New Student")
operation = input()

if operation == '1':
    addStudent()

# disconnecting from server
dataBase.close()
