# run this file on a new mysql server.

import mysql.connector

dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123",
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
                   ATTENDANCE INT,
                   MOTHER_NAME VARCHAR(30) NOT NULL,
                   FATHER_NAME VARCHAR(30) NOT NULL,
                   ADDRESS VARCHAR(150) NOT NULL,
                   PRIMARY KEY(STUDENT_ID)
                   )"""
  
# table created
cursorObject.execute(studentRecord)