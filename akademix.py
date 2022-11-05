import scanner, addStudent, selectGrade
import tkinter as tk
from tkinter import *

def homeScreen():
    def newStudent():
        root.destroy()
        addStudent.addStudent()

    def markAttendance():
        root.destroy()
        scanner.open_scanner()

    def viewByClass(): 
        root.destroy()
        selectGrade.selectGrade()
    
    root = tk.Tk()
    root.geometry("400x250")
    root.title("Akademix Records")

    addbtn = Button(root, text="Add New Student", font=('italic', 10), bg="white", command=newStudent)
    addbtn.place(x=130, y = 50)
    attendancebtn = Button(root, text="Mark Attendance", font=('italic', 10), bg="white", command=markAttendance)
    attendancebtn.place(x=130, y = 125)
    gradebtn = Button(root, text="View Students by Class", font=('italic', 10), bg="white", command=viewByClass)
    gradebtn.place(x=130, y = 200)

    root.mainloop()

if __name__ == "__main__":
    homeScreen()
