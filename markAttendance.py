import database
from datetime import date, datetime

cursorObject = database.cursorObject
dataBase = database.dataBase

def markAttendance(studentID):
    cursorObject.execute("SELECT COUNT(*) FROM ATTENDANCE WHERE STUDENT_ID = " + studentID + " AND DATE = CURRENT_DATE();")
    flag = cursorObject.fetchone()[0]
    print(flag)
    if flag == 0:
        sql = "INSERT INTO ATTENDANCE(STUDENT_ID, DATE, TIME)\
            VALUES(%s, %s, %s);"
        val = (studentID, str(date.today()) , datetime.now().strftime("%H:%M:%S"))
        cursorObject.execute(sql, val)
        sql2 = f"UPDATE STUDENT SET ATTENDANCE = ATTENDANCE + 1 WHERE STUDENT_ID = {studentID};"
        cursorObject.execute(sql2)
        dataBase.commit()
    else:
        print("Attendance already marked for today.")
