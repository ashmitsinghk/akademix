# run this file on a new mysql server.

import mysql.connector

dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1234",
    database="School"
)

cursorObject = dataBase.cursor()

studentRecord = """CREATE TABLE STUDENT (
                   STUDENT_ID INT NOT NULL AUTO_INCREMENT,
                   FIRST_NAME  VARCHAR(15) NOT NULL,
                   LAST_NAME VARCHAR(15) NOT NULL,
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

attendanceRecord = """CREATE TABLE ATTENDANCE (
                   STUDENT_ID INT NOT NULL,
                   DATE DATE NOT NULL,
                   TIME TIME NOT NULL
                   )"""
  
# table created
cursorObject.execute(studentRecord)
cursorObject.execute(attendanceRecord)