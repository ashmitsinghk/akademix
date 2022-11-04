import database
import tkinter as tk
from tkinter import *
from tkinter import ttk
import tkinter.messagebox as MessageBox


cursorObject = database.cursorObject
dataBase = database.dataBase

window = tk.Tk()
window.geometry("600x300")
window.title("View by class")

dropdown_section = StringVar(window)
dropdown_section.set("SELECT") 

def getStudents():
   grade = dropdown_grade.get()
   section = dropdown_section.get()
   window.destroy()

   root = tk.Tk()
   root.title("Student Records")
   label = tk.Label(root, text="Student Records", font=("Arial",30)).grid(row=0, columnspan=3)
   
   cols = ("STUDENT_ID", "FIRST_NAME", "LAST_NAME", "DOB")
   listBox = ttk.Treeview(root, columns=cols, show='headings')
   
   for col in cols:
      listBox.heading(col, text=col)    
      listBox.grid(row=1, column=0, columnspan=2)
   closeButton = tk.Button(root, text="Close", width=15, command=exit).grid(row=4, column=1)

   cursorObject.execute(f"SELECT STUDENT_ID, FIRST_NAME, LAST_NAME, DOB FROM student WHERE CLASS='{grade}' AND SECTION='{section}';")
   records = cursorObject.fetchall()
   print(records)
   
   for i, (STUDENT_ID, FIRST_NAME, LAST_NAME, DOB) in enumerate(records, start=1):
      listBox.insert("", "end", values=(STUDENT_ID, FIRST_NAME, LAST_NAME, DOB))
      dataBase.close()
   


def callback(*args):
   print("dropdown_grade changed!")
   if int(dropdown_grade.get())<=10:
      e_section = OptionMenu(window, dropdown_section, "A", "B")

   else:
      e_section = OptionMenu(window, dropdown_section, "Arts", "Commerce", "Science")
   e_section.pack()
   e_section.place(x=200, y=120)

dropdown_grade = StringVar(window)
dropdown_grade.trace("w", callback)
dropdown_grade.set("Select your Class") # default value

e_grade = OptionMenu(window, dropdown_grade, "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12")
e_grade.pack()
e_grade.place(x=200, y=90)

insertbtn = Button(window, text="Show Students", font=('italic', 10), bg="white", command=getStudents)
insertbtn.place(x=200, y = 150)

mainloop()
window.mainloop()

