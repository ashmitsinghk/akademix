import database

cursorObject = database.cursorObject
dataBase = database.dataBase

def getStudentID(firstName, dob, fatherName):
    sql = "SELECT * FROM STUDENT WHERE FIRST_NAME = %s AND DOB = %s AND FATHER_NAME = %s;"
    val = (firstName, dob, fatherName)

    cursorObject.execute(sql, val)
    lastRow = cursorObject.fetchone()
    studentID = str(lastRow[0])

    return studentID