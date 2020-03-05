from tkinter import *
import mysql.connector


def main():
    global mydb
    mydb = mysql.connector.connect(host='localhost',
                                   user='root',
                                   passwd='1234',
                                   database='studyhelper')
    root = Tk()
    root.title('Study Helper 1.0')
    cursor = mydb.cursor()
    cursor.execute('INSERT INTO STUDENTS(Username,Password) VALUES(%s, %s);',
                    ('test1', 'passtest1'))
    mydb.commit()
    root.mainloop()


main()
