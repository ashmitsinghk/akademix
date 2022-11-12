import database
import generateQR
import sendQR
import getStudentID
from checkEmail import checkEmail
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkcalendar import Calendar
import datetime
import akademix


cursorObject = database.cursorObject
dataBase = database.dataBase


def addStudent():
    def setDate():
        def grad_date():
            date.config(text=cal.get_date())
            root.destroy()
        root = Toplevel(window)
        root.geometry("300x300")
        root.title("Date Selector")
        cal = Calendar(root, selectmode='day')
        cal.pack(pady=20)
        Button(root, text="Set Date", font=('italic', 15),
               command=grad_date).pack(pady=20)

    def back():
        window.destroy()
        akademix.homeScreen()

    def clear():
        window.destroy()
        addStudent()

    def insert():
        root2 = Toplevel(window)
        root2.geometry("300x200")
        root2.title("Enter Database Password")

        def submit():
            if passEntry.get() == database.dataBase._password:
                firstName = e_firstName.get()
                lastName = e_lastName.get()
                grade = dropdown_grade.get()
                section = dropdown_section.get()
                dob = datetime.datetime.strptime(
                    date.cget("text"), '%m/%d/%y').strftime('%y-%m-%d')
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
                studentID = getStudentID.getStudentID(
                    firstName, dob, fatherName)
                generateQR.generateQR(studentID)
                sendQR.sendQR(studentID, email)
                messagebox.showinfo("Operation Successful", "Student Data Added Successfully.")
                root2.destroy()
                clear()
            else:
                errorLabel = Label(
                    root2, text="Incorrect Password, Please try again.", foreground='Red')
                errorLabel.place(x=20, y=130)

        passLabel = Label(root2, text="Enter your MySQL Password:")
        passLabel.place(x=20, y=20)

        passEntry = Entry(root2)
        passEntry.place(x=20, y=50)

        submitbtn = Button(root2, text="Submit", font=(
            'italic', 10), command=submit)
        submitbtn.place(x=20, y=80)
        root2.mainloop()

    window = tk.Tk()
    window.geometry("600x500")
    window.title("Add Student")

    dropdown_section = StringVar(window)
    dropdown_section.set("Select Section")

    def callback(*args):
        if int(dropdown_grade.get()) <= 10:
            e_section = OptionMenu(window, dropdown_section, "A", "B")

        else:
            e_section = OptionMenu(
                window, dropdown_section, "Arts", "Commerce", "Science")
        e_section.pack()
        e_section.place(x=200, y=150)
    
    def validateEmail(*args):
        if checkEmail(e_email.get()):
            emailLabel = Label(window, text="   ", width=200)
        else:
            emailLabel = Label(window, text="Please enter a valid Email Address.", foreground='Red')
        emailLabel.place(x=340, y=240)

    def validatePhone(*args):
        if len(e_contact.get()) == 10:
           phoneLabel = Label(window, text="   ", width=200)
        else:
            phoneLabel = Label(window, text="Please enter a valid Contact No.", foreground='Red')
        phoneLabel.place(x=340, y=210)


    # Add Button and Label

    dropdown_grade = StringVar()
    dropdown_grade.trace("w", callback)
    dropdown_grade.set("1")


    firstName = Label(window, text="Enter First Name:", font=('bold', 10))
    firstName.place(x=20, y=60)
    lastName = Label(window, text="Enter Last Name:", font=('bold', 10))
    lastName.place(x=20, y=90)
    grade = Label(window, text="Enter Class:", font=('bold', 10))
    grade.place(x=20, y=120)
    section = Label(window, text="Enter Section:", font=('bold', 10))
    section.place(x=20, y=150)
    dob = Label(window, text="Enter Date of Birth:", font=('bold', 10))
    dob.place(x=20, y=180)
    contact = Label(window, text="Enter Contact No.:", font=('bold', 10))
    contact.place(x=20, y=210)
    email = Label(window, text="Enter Email Address:", font=('bold', 10))
    email.place(x=20, y=240)
    motherName = Label(window, text="Enter Mother's Name:", font=('bold', 10))
    motherName.place(x=20, y=270)
    fatherName = Label(window, text="Enter Father's Name:", font=('bold', 10))
    fatherName.place(x=20, y=300)
    address = Label(window, text="Enter Address:", font=('bold', 10))
    address.place(x=20, y=330)
    date = Label(window, text="")
    date.place(x=300, y=180)

    e_firstName = Entry()
    e_firstName.place(x=200, y=60)
    e_lastName = Entry()
    e_lastName.place(x=200, y=90)
    e_grade = OptionMenu(window, dropdown_grade, "1", "2",
                         "3", "4", "5", "6", "7", "8", "9", "10", "11", "12")
    e_grade.pack()
    e_grade.place(x=200, y=120)
    dobbtn = Button(window, text="Select Date", font=(
        'italic', 8), bg="white", command=setDate)
    dobbtn.place(x=200, y=180)
    contactVar = StringVar()
    contactVar.trace("w", validatePhone)
    e_contact = Entry(textvariable=contactVar)
    e_contact.place(x=200, y=210)
    emailVar = StringVar()
    emailVar.trace("w", validateEmail)
    e_email = Entry(textvariable=emailVar)
    e_email.place(x=200, y=240)
    e_motherName = Entry()
    e_motherName.place(x=200, y=270)
    e_fatherName = Entry()
    e_fatherName.place(x=200, y=300)
    e_address = Entry()
    e_address.place(x=200, y=330)

    insertbtn = Button(window, text="Add Student to Database", font=(
        'italic', 10), bg="white", command=insert)
    insertbtn.place(x=200, y=360)
    clearbtn = Button(window, text="Clear", font=(
        'italic', 10), bg="white", command=clear)
    clearbtn.place(x=450, y=360)
    homebtn = Button(window, text="< Back", font=(
        'italic', 10), bg="white", command=back)
    homebtn.place(x=20, y=20)

    window.mainloop()
