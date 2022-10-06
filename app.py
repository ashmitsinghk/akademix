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
    addStudent()
elif operation == '2':
    scanner()

# disconnecting from server
dataBase.close()
