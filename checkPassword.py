import database
import tkinter as tk
from tkinter import *

def checkPassword():
    def submit():
        if passEntry.get() == database.dataBase._password:
            
        else:
            errorLabel = Label(root, text="Incorrect Password, Please try again.")
            errorLabel.place(x=20,y=100)
    root = tk.Tk()
    root.geometry("200x200")
    root.title("Enter MySQL Password")

    passLabel = Label(root, text="Enter your MySQL Password:")
    passLabel.place(x=20, y=20)

    passEntry = Entry(root)
    passEntry.place(x=20, y=50)

    submitbtn = Button(root, text="Submit", font=('italic', 10), command=submit)


    

    root.mainloop()

checkPassword()