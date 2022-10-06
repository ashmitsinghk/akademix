import database, addStudent, scanner

cursorObject = database.cursorObject
dataBase = database.dataBase
# Main Menu
print("=======================================================")
print("SELECT YOUR OPERATION")
print("=======================================================")
print("1. Add New Student")
print("2. Mark Attendance")
operation = input()

if operation == '1':
    addStudent.addStudent()
elif operation == '2':
    scanner.open_scanner()

# disconnecting from server
dataBase.close()
