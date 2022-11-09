import searchStudent, database
import tkinter as tk
from tkinter import *
from tkinter import ttk

cursorObject = database.cursorObject
dataBase = database.dataBase

def viewStudent(admission_no):
    sql = f"SELECT * FROM STUDENT WHERE STUDENT_ID = {admission_no};"

    cursorObject.execute(sql)
    lastRow = cursorObject.fetchone()
    firstName = str(lastRow[1])
    lastName = str(lastRow[2])
    grade = str(lastRow[3])
    section = str(lastRow[4])
    dob = str(lastRow[5])
    contact = str(lastRow[6])
    email = str(lastRow[7])
    attendance = str(lastRow[8])
    motherName = str(lastRow[9])
    fatherName = str(lastRow[10])
    address = str(lastRow[11])

    root = tk.Tk()
    root.geometry("400x500")
    root.title(f"{firstName}'s Student Profile")

    label_admission = Label(root, text="Admission No.:")
    label_admission.place(x=50, y=50)
    label_firstName = Label(root, text="First Name:")
    label_firstName.place(x=50, y=70)
    label_lastName = Label(root, text="Last Name:")
    label_lastName.place(x=50, y=90)
    label_grade = Label(root, text="Class:")
    label_grade.place(x=50, y=110)
    label_section = Label(root, text="Section:")
    label_section.place(x=50, y=130)
    label_dob = Label(root, text="Date of Birth:")
    label_dob.place(x=50, y=150)
    label_contact = Label(root, text="Contact:")
    label_contact.place(x=50, y=170)
    label_email = Label(root, text="Email:")
    label_email.place(x=50, y=190)
    label_attendance = Label(root, text="Attendance:")
    label_attendance.place(x=50, y=210)
    label_motherName = Label(root, text="Mother's Name:")
    label_motherName.place(x=50, y=230)
    label_fatherName = Label(root, text="Father's Name:")
    label_fatherName.place(x=50, y=250)
    label_address = Label(root, text="Address:")
    label_address.place(x=50, y=270)

    value_admission = Label(root, text=admission_no)
    value_admission.place(x=150, y=50)
    value_firstName = Label(root, text=firstName)
    value_firstName.place(x=150, y=70)
    value_lastName = Label(root, text=lastName)
    value_lastName.place(x=150, y=90)
    value_grade = Label(root, text=grade)
    value_grade.place(x=150, y=110)
    value_section = Label(root, text=section)
    value_section.place(x=150, y=130)
    value_dob = Label(root, text=dob)
    value_dob.place(x=150, y=150)
    value_contact = Label(root, text=contact)
    value_contact.place(x=150, y=170)
    value_email = Label(root, text=email)
    value_email.place(x=150, y=190)
    value_attendance = Label(root, text=attendance)
    value_attendance.place(x=150, y=210)
    value_motherName = Label(root, text=motherName)
    value_motherName.place(x=150, y=230)
    value_fatherName = Label(root, text=fatherName)
    value_fatherName.place(x=150, y=250)
    value_address = Label(root, text=address)
    value_address.place(x=150, y=270)

    

    root.mainloop()

if __name__ == '__main__':
    viewStudent(3)