import searchStudent, database, sendQR, editStudent
import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os

cursorObject = database.cursorObject
dataBase = database.dataBase

def viewStudent(admission_no):

    def back():
        root.destroy()
        searchStudent.searchStudent()
    
    def sendViaEmail():
        sendQR.sendQR(admission_no, email)
    
    def deleteStudent():

        root2 = Toplevel(root)
        root2.geometry("300x200")
        root2.title("Enter Database Password")

        def submit():
            if passEntry.get() == database.dataBase._password:
                cursorObject.execute(f"DELETE FROM STUDENT WHERE STUDENT_ID = {admission_no}")
                dataBase.commit()
                os.remove(f"./QR/QR_STUDENT_{admission_no}.png")
                root.destroy()
                searchStudent.searchStudent()
                root2.destroy()
                back()
            else:
                errorLabel = Label(
                    root2, text="Incorrect Password, Please try again.")
                errorLabel.place(x=20, y=130)

        passLabel = Label(root2, text="Enter your MySQL Password:")
        passLabel.place(x=20, y=20)

        passEntry = Entry(root2)
        passEntry.place(x=20, y=50)

        submitbtn = Button(root2, text="Submit", font=(
            'italic', 10), command=submit)
        submitbtn.place(x=20, y=80)
        root2.mainloop()

        

    def edit():
        root.destroy()
        editStudent.editStudent(admission_no, firstName, lastName, grade, section, dob, contact, email, motherName, fatherName, address)


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
    label_admission.place(x=50, y=80)
    label_firstName = Label(root, text="First Name:")
    label_firstName.place(x=50, y=100)
    label_lastName = Label(root, text="Last Name:")
    label_lastName.place(x=50, y=120)
    label_grade = Label(root, text="Class:")
    label_grade.place(x=50, y=140)
    label_section = Label(root, text="Section:")
    label_section.place(x=50, y=160)
    label_dob = Label(root, text="Date of Birth:")
    label_dob.place(x=50, y=180)
    label_contact = Label(root, text="Contact:")
    label_contact.place(x=50, y=200)
    label_email = Label(root, text="Email:")
    label_email.place(x=50, y=220)
    label_attendance = Label(root, text="Attendance:")
    label_attendance.place(x=50, y=240)
    label_motherName = Label(root, text="Mother's Name:")
    label_motherName.place(x=50, y=260)
    label_fatherName = Label(root, text="Father's Name:")
    label_fatherName.place(x=50, y=280)
    label_address = Label(root, text="Address:")
    label_address.place(x=50, y=300)

    value_admission = Label(root, text=admission_no)
    value_admission.place(x=150, y=80)
    value_firstName = Label(root, text=firstName)
    value_firstName.place(x=150, y=100)
    value_lastName = Label(root, text=lastName)
    value_lastName.place(x=150, y=120)
    value_grade = Label(root, text=grade)
    value_grade.place(x=150, y=140)
    value_section = Label(root, text=section)
    value_section.place(x=150, y=160)
    value_dob = Label(root, text=dob)
    value_dob.place(x=150, y=180)
    value_contact = Label(root, text=contact)
    value_contact.place(x=150, y=200)
    value_email = Label(root, text=email)
    value_email.place(x=150, y=220)
    value_attendance = Label(root, text=attendance)
    value_attendance.place(x=150, y=240)
    value_motherName = Label(root, text=motherName)
    value_motherName.place(x=150, y=260)
    value_fatherName = Label(root, text=fatherName)
    value_fatherName.place(x=150, y=280)
    value_address = Label(root, text=address)
    value_address.place(x=150, y=300)



    editbtn = Button(root, text="Edit", font=('italic', 10), width=9, height=2, command=edit)
    editbtn.place(x=160, y=400)

    deletebtn = Button(root, text="Delete", font=('italic', 10), width=9, height=2, command=deleteStudent)
    deletebtn.place(x=248, y=400)

    homebtn = Button(root, text="< Back", font=('italic', 10), bg="white", command=back)
    homebtn.place(x=20, y = 20)
    
    QR = Image.open(f"./QR/QR_STUDENT_{admission_no}.png")
    resize_QR = QR.resize((90,90))
    studentQR = ImageTk.PhotoImage(resize_QR)
    label_QR = Label(image=studentQR)
    label_QR.place(x=50,y=350)

    emailbtn = Button(root, text="Send QR via email", font=('italic', 10), width=20, height=2, command=sendViaEmail)
    emailbtn.place(x=160, y=350)
    
    root.mainloop()

if __name__ == '__main__':
    viewStudent(3)