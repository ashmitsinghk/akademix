import akademix, database, viewStudent
import tkinter as tk
from tkinter import *
from tkinter import ttk

cursorObject = database.cursorObject
dataBase = database.dataBase

def searchStudent():
    def viewStudentByID():
        admission_no = e_admission.get()
        root.destroy()
        viewStudent.viewStudent(admission_no)
    
    def home():
        root.destroy()
        akademix.homeScreen()

    def getResult():
        name = e_Name.get()
        cols = ("ADMISSION NO.", "STUDENT NAME", "CLASS")
        listBox = ttk.Treeview(root, columns=cols, show='headings')
        listBox.place(x=30, y=80)

      
        for col in cols:
            listBox.heading(col, text=col)    
            listBox.grid(row=1, column=0, columnspan=2)

        cursorObject.execute(f"SELECT STUDENT_ID, CONCAT(FIRST_NAME, ' ', LAST_NAME) AS STUDENT_NAME, CONCAT(CLASS, ' ', SECTION) AS CLASS FROM student WHERE CONCAT(FIRST_NAME, ' ', LAST_NAME) LIKE '%{name}%';")
        records = cursorObject.fetchall()
      
        for i, (STUDENT_ID, STUDENT_NAME, CLASS) in enumerate(records, start=1):
            listBox.insert("", "end", values=(STUDENT_ID, STUDENT_NAME, CLASS))
        listBox.place(x=35, y=80)
    
    root = tk.Tk()
    root.geometry("740x500")
    root.title("Search Student")

    name = Label(root, text = "Enter Student Name:", font = ('bold', 10))
    name.place(x=20, y=50)
    e_Name = Entry(width=72)
    e_Name.place(x=160, y=50)

    searchbtn = Button(root, text="Search", font=('italic', 9), command=getResult)
    searchbtn.place(x=600, y=45)
    
    admission = Label(root, text = "Enter Admission No.:", font = ('bold', 10))
    admission.place(x=20, y=350)
    e_admission = Entry(width=71)
    e_admission.place(x=167, y=350)

    viewbtn = Button(root, text="View Profile", font=('italic', 9), command=viewStudentByID)
    viewbtn.place(x=600, y=345)

    homebtn = Button(root, text="< Back", font=('italic', 10), bg="white", command=home)
    homebtn.place(x=20, y = 5)
    
    

    root.mainloop()

if __name__ == "__main__":
    searchStudent()

