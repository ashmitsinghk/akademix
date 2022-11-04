import database, generateQR, sendQR, getStudentID
import tkinter as tk
from tkinter import *
import tkinter.messagebox as MessageBox

cursorObject = database.cursorObject
dataBase = database.dataBase

# def addStudent():

#     # Take input from user
#     firstName = input("First Name:  ")
#     lastName = input("Last Name:  ")
#     grade = input("Class (1-12):  ")
#     section = input("Section/Stream:  ")
#     dob = input("Date of Birth (yyyy-mm-dd):  ")
#     contact = input("Contact Number:  ")
#     email = input("E-mail Address:  ")
#     motherName = input("Mother's Name:  ")
#     fatherName = input("Father's Name:  ")
#     address = input("Address: ")

#     # Insert new student record into STUDENT
#     sql = "INSERT INTO STUDENT (FIRST_NAME, LAST_NAME, CLASS, SECTION, DOB, CONTACT_NO, EMAIL, MOTHER_NAME, FATHER_NAME, ADDRESS)\
#     VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
#     val = (firstName, lastName, grade, section, dob,
#            contact, email, motherName, fatherName, address)
#     cursorObject.execute(sql, val)
#     dataBase.commit()

#     studentID = getStudentID.getStudentID(firstName, dob, fatherName)
#     generateQR.generateQR(studentID)
#     sendQR.sendQR(studentID, email)

# Function to create a new record in STUDENT

def insert():
       firstName = e_firstName.get()
       lastName = e_lastName.get()
       grade = e_grade.get()
       section = e_section.get()
       dob = e_dob.get()
       contact = e_contact.get()
       email = e_email.get()
       motherName = e_motherName.get()
       fatherName = e_fatherName.get()
       address = e_address.get()

    # Insert new student record into STUDENT
       sql = "INSERT INTO STUDENT (FIRST_NAME, LAST_NAME, CLASS, SECTION, DOB, CONTACT_NO, EMAIL, MOTHER_NAME, FATHER_NAME, ADDRESS)\
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
       val = (firstName, lastName, grade, section, dob,
           contact, email, motherName, fatherName, address)
       cursorObject.execute(sql, val)
       dataBase.commit()
       studentID = getStudentID.getStudentID(firstName, dob, fatherName)
       generateQR.generateQR(studentID)
       sendQR.sendQR(studentID, email)

   
window = tk.Tk()
window.geometry("600x500")
window.title("Add Student")


variable = StringVar(window)
variable.set("1") 

firstName = Label(window, text = "Enter First Name:", font = ('bold', 10))
firstName.place(x=20, y=30)
lastName = Label(window, text = "Enter Last Name:", font = ('bold', 10))
lastName.place(x=20, y=60)
grade = Label(window, text = "Enter Class:", font = ('bold', 10))
grade.place(x=20, y=90)
section = Label(window, text = "Enter Section:", font = ('bold', 10))
section.place(x=20, y=120)
dob = Label(window, text = "Enter Date of Birth:", font = ('bold', 10))
dob.place(x=20, y=150)
contact = Label(window, text = "Enter Contact No.:", font = ('bold', 10))
contact.place(x=20, y=180)
email = Label(window, text = "Enter Email Address:", font = ('bold', 10))
email.place(x=20, y=210)
motherName = Label(window, text = "Enter Mother's Name:", font = ('bold', 10))
motherName.place(x=20, y=240)
fatherName = Label(window, text = "Enter Father's Name:", font = ('bold', 10))
fatherName.place(x=20, y=270)
address = Label(window, text = "Enter Address:", font = ('bold', 10))
address.place(x=20, y=300)

e_firstName = Entry()
e_firstName.place(x=200, y=30)
e_lastName = Entry()
e_lastName.place(x=200, y=60)
e_grade = OptionMenu(window, variable, "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12")
e_grade.pack()
e_grade.place(x=200, y=90)
e_section = Entry()
e_section.place(x=200, y=120)
e_dob = Entry()
e_dob.place(x=200, y=150)
e_contact = Entry()
e_contact.place(x=200, y=180)
e_email = Entry()
e_email.place(x=200, y=210)
e_motherName = Entry()
e_motherName.place(x=200, y=240)
e_fatherName = Entry()
e_fatherName.place(x=200, y=270)
e_address = Entry()
e_address.place(x=200, y=300)

insertbtn = Button(window, text="Add Student to Database", font=('italic', 10), bg="white", command=insert)
insertbtn.place(x=200, y = 330)




window.mainloop()