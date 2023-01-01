# run this file on a new mysql server.

from functionalities import database
cursorObject = database.cursorObject
dataBase = database.dataBase

def createTables():
    studentRecord = """CREATE TABLE IF NOT EXISTS STUDENT (
                    STUDENT_ID INT NOT NULL AUTO_INCREMENT,
                    FIRST_NAME  VARCHAR(15) NOT NULL,
                    LAST_NAME VARCHAR(15) NOT NULL,
                    GENDER VARCHAR(6) NOT NULL,
                    CLASS INT NOT NULL,
                    SECTION VARCHAR(10) NOT NULL,
                    DOB DATE NOT NULL,
                    CONTACT_NO BIGINT NOT NULL,
                    EMAIL VARCHAR(50) NOT NULL,
                    ATTENDANCE INT DEFAULT 0,
                    MOTHER_NAME VARCHAR(30) NOT NULL,
                    FATHER_NAME VARCHAR(30) NOT NULL,
                    ADDRESS VARCHAR(150) NOT NULL,
                    PRIMARY KEY(STUDENT_ID)
                    )"""

    attendanceRecord = """CREATE TABLE IF NOT EXISTS ATTENDANCE (
                    STUDENT_ID INT NOT NULL,
                    DATE DATE NOT NULL,
                    TIME TIME NOT NULL
                    )"""
    
    # table created
    cursorObject.execute(studentRecord)
    cursorObject.execute(attendanceRecord)