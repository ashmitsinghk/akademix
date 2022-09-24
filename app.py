import database, addStudent

cursorObject = database.cursorObject
dataBase = database.dataBase
# Main Menu
print("=======================================================")
print("SELECT YOUR OPERATION")
print("=======================================================")
print("1. Add New Student")
operation = input()

if operation == '1':
    addStudent()

# disconnecting from server
dataBase.close()
