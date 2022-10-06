import database, generateQR, sendQR, getStudentID

cursorObject = database.cursorObject
dataBase = database.dataBase

# Function to create a new record in STUDENT

def addStudent():

    # Take input from user
    firstName = input("First Name:  ")
    lastName = input("Last Name:  ")
    grade = input("Class (1-12):  ")
    section = input("Section/Stream:  ")
    dob = input("Date of Birth (yyyy-mm-dd):  ")
    contact = input("Contact Number:  ")
    email = input("E-mail Address:  ")
    motherName = input("Mother's Name:  ")
    fatherName = input("Father's Name:  ")
    address = input("Address: ")

    # Insert new student record into STUDENT
    sql = "INSERT INTO STUDENT (FIRST_NAME, LAST_NAME, CLASS, SECTION, DOB, CONTACT_NO, EMAIL, MOTHER_NAME, FATHER_NAME, ADDRESS)\
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (firstName, lastName, grade, section, dob,
           contact, email, motherName, fatherName, address)
    cursorObject.execute(sql, val)
    dataBase.commit()

    studentID = getStudentID(firstName, dob, fatherName)
    generateQR(studentID)
    sendQR(studentID, email)
