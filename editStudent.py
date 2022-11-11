import database, generateQR, sendQR, getStudentID, viewStudent
import tkinter as tk
from tkinter import *
import tkinter.messagebox as MessageBox
from tkcalendar import Calendar
import datetime


cursorObject = database.cursorObject
dataBase = database.dataBase

def editStudent(arg_admission_no, arg_firstName, arg_lastName, arg_grade, arg_section, arg_dob, arg_contact, arg_email, arg_motherName, arg_fatherName, arg_address):
   def setDate():
      def grad_date():
         date.config(text = datetime.datetime.strptime(cal.get_date(), '%m/%d/%y').strftime('%y-%m-%d')) 
         root.destroy()
      root = Toplevel(window)
      root.geometry("300x300")
      root.title("Date Selector")
      cal = Calendar(root, selectmode = 'day')
      cal.pack(pady = 20)
      Button(root, text = "Set Date", font= ('italic', 15),
         command = grad_date).pack(pady = 20)
   
   def back():
      window.destroy()
      viewStudent.viewStudent(arg_admission_no)

   def clear():
      window.destroy()
      editStudent()

   def insert():
         firstName = e_firstName.get()
         lastName = e_lastName.get()
         grade = dropdown_grade.get()
         section = dropdown_section.get()
         dob = date.cget("text")
         contact = e_contact.get()
         email = e_email.get()
         motherName = e_motherName.get()
         fatherName = e_fatherName.get()
         address = e_address.get()

      # Insert new student record into STUDENT
         sql = f"UPDATE STUDENT SET FIRST_NAME = '{firstName}', LAST_NAME = '{lastName}', CLASS = {grade}, SECTION = '{section}', DOB = '{dob}', CONTACT_NO = {contact}, EMAIL = '{email}', MOTHER_NAME = '{motherName}', FATHER_NAME = '{fatherName}', ADDRESS = '{address}' WHERE STUDENT_ID = {arg_admission_no};"
         cursorObject.execute(sql)
         dataBase.commit()
         print("Student Data Updated Successfully.")

      
   window = tk.Tk()
   window.geometry("600x500")
   window.title("Edit Student")

   dropdown_section = StringVar(window)
   dropdown_section.set(arg_section) 

   def callback(*args):
      print("dropdown_grade changed!")
      if int(dropdown_grade.get())<=10:
         e_section = OptionMenu(window, dropdown_section, "A", "B")

      else:
         e_section = OptionMenu(window, dropdown_section, "Arts", "Commerce", "Science")
      e_section.pack()
      e_section.place(x=200, y=150)




   

   
   # Add Button and Label


   dropdown_grade = StringVar()
   dropdown_grade.trace("w", callback)
   dropdown_grade.set(arg_grade)


   firstName = Label(window, text = "Enter First Name:", font = ('bold', 10))
   firstName.place(x=20, y=60)
   lastName = Label(window, text = "Enter Last Name:", font = ('bold', 10))
   lastName.place(x=20, y=90)
   grade = Label(window, text = "Enter Class:", font = ('bold', 10))
   grade.place(x=20, y=120)
   section = Label(window, text = "Enter Section:", font = ('bold', 10))
   section.place(x=20, y=150)
   dob = Label(window, text = "Enter Date of Birth:", font = ('bold', 10))
   dob.place(x=20, y=180)
   contact = Label(window, text = "Enter Contact No.:", font = ('bold', 10))
   contact.place(x=20, y=210)
   email = Label(window, text = "Enter Email Address:", font = ('bold', 10))
   email.place(x=20, y=240)
   motherName = Label(window, text = "Enter Mother's Name:", font = ('bold', 10))
   motherName.place(x=20, y=270)
   fatherName = Label(window, text = "Enter Father's Name:", font = ('bold', 10))
   fatherName.place(x=20, y=300)
   address = Label(window, text = "Enter Address:", font = ('bold', 10))
   address.place(x=20, y=330)
   date = Label(window, text = arg_dob)
   date.place(x=300, y=180)

   firstNameVar = StringVar()
   firstNameVar.set(arg_firstName)
   lastNameVar = StringVar()
   lastNameVar.set(arg_lastName)
   contactVar = StringVar()
   contactVar.set(arg_contact)
   emailVar = StringVar()
   emailVar.set(arg_email)
   motherNameVar = StringVar()
   motherNameVar.set(arg_motherName)
   fatherNameVar = StringVar()
   fatherNameVar.set(arg_fatherName)
   addressVar = StringVar()
   addressVar.set(arg_address)


   e_firstName = Entry(textvariable=firstNameVar)
   e_firstName.place(x=200, y=60)
   e_lastName = Entry(textvariable=lastNameVar)
   e_lastName.place(x=200, y=90)
   e_grade = OptionMenu(window, dropdown_grade, "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12")
   e_grade.pack()
   e_grade.place(x=200, y=120)
   dobbtn = Button(window, text="Select Date", font=('italic', 8), bg="white", command=setDate)
   dobbtn.place(x=200, y = 180)
   e_contact = Entry(textvariable=contactVar)
   e_contact.place(x=200, y=210)
   e_email = Entry(textvariable=emailVar)
   e_email.place(x=200, y=240)
   e_motherName = Entry(textvariable=motherNameVar)
   e_motherName.place(x=200, y=270)
   e_fatherName = Entry(textvariable=fatherNameVar)
   e_fatherName.place(x=200, y=300)
   e_address = Entry(textvariable=addressVar)
   e_address.place(x=200, y=330)

   insertbtn = Button(window, text="Update Student Data", font=('italic', 10), bg="white", command=insert)
   insertbtn.place(x=200, y = 360)
   homebtn = Button(window, text="< Back", font=('italic', 10), bg="white", command=back)
   homebtn.place(x=20, y = 20)

   window.mainloop()
