import mysql.connector

class Validation:
    def __init__(self):
        self.mydb = mysql.connector.connect(host='localhost',
                                        user='root',
                                        passwd='1234',
                                        database='studyhelper')
        self.cursor = self.mydb.cursor()
    
    def validationUserRegistration(self, username):
        try:
            self.cursor.execute("SELECT * FROM STUDENTS WHERE Username = %s;", username)
            return (self.cursor.fetchone())
        except:
            return False




class UserDb:
    def __init__(self):
        self.mydb = mysql.connector.connect(host='localhost',
                                        user='root',
                                        passwd='1234',
                                        database='studyhelper')
        self.cursor = self.mydb.cursor()

    def userLogin(self, data):
        try:
            self.cursor.execute("SELECT * FROM students WHERE Username = %s AND Password = %s;", data)
            return (self.cursor.fetchone())
        except:
            return False

    def userRegistration(self, data, username):
        try:
            username = (username,)
            self.validation = Validation()
            reg = self.validation.validationUserRegistration(username)
            if reg:
                pass
            else:
                try:
                    self.cursor.execute("INSERT INTO STUDENTS(Username,Password) VALUES(%s, %s);", (data))
                    self.mydb.commit()
                except:
                    pass
            return reg
        except:
            return False
