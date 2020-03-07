from tkinter import *
import mysql.connector

def delete(): 
    cursor = mydb.cursor()
    cursor.execute('delete from STUDENTS where Username = "raven";')
    mydb.commit()

def update():
    cursor = mydb.cursor()
    cursor.execute('update STUDENTS set Password = "1234" where Username = "test1";')
    mydb.commit()

def main():
    global mydb
    mydb = mysql.connector.connect(host='localhost',
                                   user='root',
                                   passwd='1234',
                                   database='studyhelper')
    root = Tk()
    root.title('Study Helper 1.0')

    username = 'raven'
    password = '1234'
    cursor = mydb.cursor()
    cursor.execute('INSERT INTO STUDENTS(Username,Password) VALUES(%s, %s);',
                    (username, password))
    mydb.commit()
    update()
    delete()
    root.mainloop()



main()


