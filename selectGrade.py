import database
import tkinter as tk
from tkinter import *
import tkinter.messagebox as MessageBox


cursorObject = database.cursorObject
dataBase = database.dataBase

window = tk.Tk()
window.geometry("600x300")
window.title("View by class")
master = Tk()
variable = StringVar(master)
label1 = Label(master, text = "Username").place(x = 30,y = 50) 
variable = set("Select your Class") # default value
w = OptionMenu(master, variable, "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12")
w.pack()

mainloop()
# grade = str(input("Enter grade: "))
# section = str(input("Enter section: "))
    
# cursorObject.execute(f"SELECT * FROM STUDENT WHERE CLASS = '" + grade + "' AND SECTION = '" + section + "';")

# def selectGrade():
#     i = 0
#     for student in cursorObject:
#         for j in range(len(student)):
#             entry = Label(window, width=10, text=student[j], borderwidth=2, relief='ridge')
#             entry.grid(row = i, column = j)
#             entry.insert(END, student[j])
#         i += 1
window.mainloop()

