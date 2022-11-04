import database, scanner

cursorObject = database.cursorObject
dataBase = database.dataBase
# Main Menu
print("=======================================================")
print("SELECT YOUR OPERATION")
print("=======================================================")
print("1. Add New Student")
print("2. Mark Attendance")
print("3. View students by class")
operation = input()

if operation == '1':
    import addStudent
elif operation == '2':
    scanner.open_scanner()
elif operation == '3':
    import selectGrade

# disconnecting from server
dataBase.close()