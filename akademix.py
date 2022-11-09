import scanner, addStudent, selectGrade, searchStudent
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
    
    def studentProfile(): 
        root.destroy()
        searchStudent.searchStudent()
    
    
    root = tk.Tk()
    root.geometry("500x400")
    root.title("Akademix Records")

    title = Label(root, text="Akademix Records", font=('Bold', 30))
    title.place(x=75, y=50)

    addbtn = Button(root, text="Add New Student", font=('italic', 10), bg="white", command=newStudent, width=25, height=5)
    addbtn.place(x=35, y = 150)
    attendancebtn = Button(root, text="Mark Attendance", font=('italic', 10), bg="white", command=markAttendance, width=25, height=5)
    attendancebtn.place(x=255, y = 150)
    gradebtn = Button(root, text="View Students by Class", font=('italic', 10), bg="white", command=viewByClass, width=25, height=5)
    gradebtn.place(x=35, y = 250)
    searchbtn = Button(root, text="Search and View Student Profile", font=('italic', 10), bg="white", command=studentProfile, width=25, height=5)
    searchbtn.place(x=255, y = 250)

    root.mainloop()

if __name__ == "__main__":
    homeScreen()
