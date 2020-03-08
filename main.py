from tkinter import *
import mysql.connector

# === MAIN SCREEN === #

class Screens:
   
      def __init__(self):
            # create a tkinter window
            self.root = Tk()

            # to scenter the screen
            width = self.root.winfo_screenwidth()
            height = self.root.winfo_screenheight()
            x = int(width / 2 - 1024 / 2)
            y = int(height / 2 - 750 / 2)
            reso = "1024x720+"+ str(x) + "+" + str(y)

            # size of window configuration
            self.root.geometry(reso)
            self.root.title("Study Helper v1.0")
            self.root.configure(bg = "gray17")

            # disable resize of the window
            self.root.resizable(width=False, height=False)

            # === Images Used === #
            self.logo = PhotoImage(file = "images\logo.png")

            # === Frames list === #
            # LogoFrame
            self.LogoFrame = Frame(self.root)
            self.LogoFrame.place(x=405, y=75)
            # OptionFrame
            self.OptionFrame = Frame(self.root)
            self.OptionFrame.place(x=370, y=340)
            self.OptionFrame.configure(bg ="gray17")

            # Showing Logo
            Label(self.LogoFrame, image=self.logo, bg = "gray17").pack()

            # Showing OptionFrame
            Label(self.OptionFrame,
                  text="Welcome to Study Helper",
                  bg = "gray17",
                  fg = "SlateGray2",
                  height = "3",
                  font = ("Courier 18")).pack()
            # Login Button
            Button(self.OptionFrame,
                  text="Login",
                  bg = "steel blue",
                  fg = "snow",
                  width = "12",
                  font = ("Courier 12"),
                  command = self.loginScreen).pack()
            Label(self.OptionFrame,
                  text = "",
                  bg = "gray17",
                  font = ("Courier 1")).pack()
            # Register Button
            Button(self.OptionFrame,
                  text="Register",
                  bg = "steel blue",
                  fg = "snow",
                  width = "12",
                  font = ("Courier 12"),
                  command = self.registrationScreen).pack()

            # loop to run the tkinter
            self.root.mainloop()
            
      def loginScreen(self):
            # destroy current window
            self.root.destroy()

            #open the new window
            log = LoginWindow()

      def registrationScreen(self):
            # destroy current window
            self.root.destroy()

            #open the new window
            reg = RegistrationWindow()


# === LOGIN SCREEN === #
class LoginWindow:

      def __init__(self):
            # create a tkinter window
            self.root = Tk()

            # to center the screen
            width = self.root.winfo_screenwidth()
            height = self.root.winfo_screenheight()
            x = int(width / 2 - 1024 / 2)
            y = int(height / 2 - 750 / 2)
            reso = "1024x720+"+ str(x) + "+" + str(y)

            # size of window configuration
            self.root.geometry(reso)
            self.root.title("Study Helper v1.0")
            self.root.configure(bg = "gray17")

            # disable resize of the window
            self.root.resizable(width=False, height=False)

            # === Images Used === #
            self.logo = PhotoImage(file = "images\logo.png")

            # === Frames list === #
            # LogoFrame
            self.LogoFrame = Frame(self.root)
            self.LogoFrame.place(x=405, y=75)
            # OptionFrame
            self.OptionFrame = Frame(self.root)
            self.OptionFrame.place(x=370, y=340)
            self.OptionFrame.configure(bg ="gray17")
            
            # Showing Logo
            Label(self.LogoFrame, image=self.logo, bg = "gray17").pack()

            # Showing OptionFrame
            Label(self.OptionFrame,
                  text="Welcome to Study Helper",
                  bg = "gray17",
                  fg = "SlateGray2",
                  height = "3",
                  font = ("Courier 18")).pack()
            Label(self.OptionFrame,
                  text="Username",
                  bg = "gray17",
                  fg = "Snow",
                  font = ("Courier 10")).pack()
            userEntry = Entry(self.OptionFrame,
                              bg = "snow")
            userEntry.pack()
            Label(self.OptionFrame,
                  text="Password",
                  bg = "gray17",
                  fg = "Snow",
                  font = ("Courier 10")).pack()
            passEntry = Entry(self.OptionFrame,
                              bg = "snow",
                              show = "*")
            passEntry.pack()
            Label(self.OptionFrame,
                  text = "",
                  bg = "gray17",
                  font = ("Courier 1")).pack()
            
            # LoginButton
            Button(self.OptionFrame,
                  text="Login",
                  bg = "steel blue",
                  fg = "snow",
                  width = "8",
                  font = ("Courier 10"),
                  command = self.homeScreen).pack()
            
            # To Registration Window 
            Label(self.OptionFrame,
                  text = "       Don't have an account yet?",
                  bg = "gray17",
                  fg = "white",
                  font = ("Courier 8")).pack(side=LEFT)

            Button(self.OptionFrame,
                  text="Click here",
                  bg = "gray17",
                  fg = "steel blue",
                  relief = "flat",
                  font = ("Courier 8"),
                  command = self.registrationScreen).pack(side=LEFT)

            # loop to run the tkinter
            self.root.mainloop()

      def registrationScreen(self):
            # destroy current window
            self.root.destroy()

            #open the new window
            reg = RegistrationWindow()

      def homeScreen(self):
            # destroy current window
            self.root.destroy()

            #open the new window
            home = HomeWindow()

# === REGISTRATION SCREEN === #
class RegistrationWindow:

      def __init__(self):
            # create a tkinter window
            self.root = Tk()

            # to center the screen
            width = self.root.winfo_screenwidth()
            height = self.root.winfo_screenheight()
            x = int(width / 2 - 1024 / 2)
            y = int(height / 2 - 750 / 2)
            reso = "1024x720+"+ str(x) + "+" + str(y)

            # size of window configuration
            self.root.geometry(reso)
            self.root.title("Study Helper v1.0")
            self.root.configure(bg = "gray17")

            # disable resize of the window
            self.root.resizable(width=False, height=False)

            # === Images Used === #
            self.logo = PhotoImage(file = "images\logo.png")

            # === Frames list === #
            # LogoFrame
            self.LogoFrame = Frame(self.root)
            self.LogoFrame.place(x=405, y=75)
            # OptionFrame
            self.OptionFrame = Frame(self.root)
            self.OptionFrame.place(x=370, y=340)
            self.OptionFrame.configure(bg ="gray17")
            
            # Showing Logo
            Label(self.LogoFrame, image=self.logo, bg = "gray17").pack()

            # Showing OptionFrame
            Label(self.OptionFrame,
                  text="Welcome to Study Helper",
                  bg = "gray17",
                  fg = "SlateGray2",
                  height = "3",
                  font = ("Courier 18")).pack()
            Label(self.OptionFrame,
                  text="Username",
                  bg = "gray17",
                  fg = "Snow",
                  font = ("Courier 10")).pack()
            userEntry = Entry(self.OptionFrame,
                              bg = "snow")
            userEntry.pack()
            Label(self.OptionFrame,
                  text="Password",
                  bg = "gray17",
                  fg = "Snow",
                  font = ("Courier 10")).pack()
            passEntry = Entry(self.OptionFrame,
                              bg = "snow",
                              show = "*")
            passEntry.pack()
            Label(self.OptionFrame,
                  text="Re-type password",
                  bg = "gray17",
                  fg = "Snow",
                  font = ("Courier 10")).pack()
            pass2Entry = Entry(self.OptionFrame,
                              bg = "snow",
                              show = "*")
            pass2Entry.pack()
            Label(self.OptionFrame,
                  text = "",
                  bg = "gray17",
                  font = ("Courier 1")).pack()
            
            # Registration Button
            Button(self.OptionFrame,
                  text="Register",
                  bg = "steel blue",
                  fg = "snow",
                  width = "8",
                  font = ("Courier 10"),
                  command = self.loginScreen).pack()

            # To Login Window 
            Label(self.OptionFrame,
                  text = "       Already have an account?",
                  bg = "gray17",
                  fg = "white",
                  font = ("Courier 8")).pack(side=LEFT)

            Button(self.OptionFrame,
                  text="Click here",
                  bg = "gray17",
                  fg = "steel blue",
                  relief = "flat",
                  font = ("Courier 8"),
                  command = self.loginScreen).pack(side=LEFT)

            # loop to run the tkinter
            self.root.mainloop()

      def loginScreen(self):
            # destroy current window
            self.root.destroy()

            #open the new window
            log = LoginWindow()
            log.loginScreen

class HomeWindow:
      def __init__(self):
            self.root = Tk()

            # to center the screen
            width = self.root.winfo_screenwidth()
            height = self.root.winfo_screenheight()
            x = int(width / 2 - 1024 / 2)
            y = int(height / 2 - 750 / 2)
            reso = "1024x720+"+ str(x) + "+" + str(y)

            # size of window configuration
            self.root.geometry(reso)
            self.root.title("Study Helper v1.0")
            self.root.configure(bg = "gray17")

            # disable resize of the window
            self.root.resizable(width=False, height=False)  

            # Line Frame
            self.lineFrame = Frame(self.root)
            self.lineFrame.place(x=358, y=0, height = 720, width=2)
            self.lineFrame.configure(bg = "gray20")

            # Line Frame2
            self.lineFrame2 = Frame(self.root)
            self.lineFrame2.place(x=716, y=0, height = 720, width=2)
            self.lineFrame2.configure(bg = "gray20")

            # Header Frame 
            self.headerFrame = Frame(self.root)
            self.headerFrame.place(x=0, y=0, width=1024 ,height = 120)
            self.headerFrame.configure(bg = "gray20")

            # Top left Frame
            self.topLeftFrame = Frame(self.root)
            self.topLeftFrame.place(x=50, y=0, width=358 ,height = 120)
            self.topLeftFrame.configure(bg = "gray20")

            # Top middle Frame
            self.topMiddleFrame = Frame(self.root)
            self.topMiddleFrame.place(x=360, y=0, width=358 ,height = 120)
            self.topMiddleFrame.configure(bg = "gray20")

            # Top right Frame
            self.topRightFrame = Frame(self.root)
            self.topRightFrame.place(x=720, y=0, width=358 ,height = 120)
            self.topRightFrame.configure(bg = "gray20")

            # Menu Frame
            self.menuFrame = Frame(self.root)
            self.menuFrame.place(x=0, y=0, height = 720, width=50)
            self.menuFrame.configure(bg ="dark slate gray")

            # Content Left Frame
            self.contentLeftFrame = Frame(self.root)
            self.contentLeftFrame.place(x=50, y=120)
            self.contentLeftFrame.configure(bg ="gray17")

            # Content Middle Frame
            self.contentMiddleFrame = Frame(self.root)
            self.contentMiddleFrame.place(x=50, y=120)
            self.contentMiddleFrame.configure(bg ="gray17")

            # Content Right Frame
            self.contentRightFrame = Frame(self.root)
            self.contentRightFrame.place(x=50, y=120)
            self.contentRightFrame.configure(bg ="gray17")

            # Content of top left frame
            Today = Label(self.topLeftFrame, text = "Today", bg = "gray20", fg = "white", font = ("Courier 18 bold")).place(x = 20, y = 30)
            DateToday = Label(self.topLeftFrame, text = "Day, Month 0", bg = "gray20", fg = "white", font = ("Courier 14")).place(x = 20, y = 60)

            # Content of top middle frame
            Tasks = Label(self.topMiddleFrame, text = "Tasks", bg = "gray20", fg = "white", font = ("Courier 18 bold")).place(x = 20, y = 30)
            NewTask = Button(self.topMiddleFrame, command = self.newTaskScreen, text = "New Task +", bg = "steel blue", fg = "white", font = ("Courier 12 bold"), relief = "raised").place(x = 20, y = 65)

            # Content of top right frame
            Tasks = Label(self.topRightFrame, text = "Exams", bg = "gray20", fg = "white", font = ("Courier 18 bold")).place(x = 20, y = 30)

      def newTaskScreen(self):
            newTask = NewTaskWindow()


class NewTaskWindow:
      def __init__(self):
            self.root = Tk()

            # to center the screen
            width = self.root.winfo_screenwidth()
            height = self.root.winfo_screenheight()
            x = int(width / 2 - 600 / 2)
            y = int(height / 2 - 430 / 2)
            reso = "600x500+"+ str(x) + "+" + str(y)

            # size of window configuration
            self.root.geometry(reso)
            self.root.title("Create New Task")
            self.root.configure(bg = "gray20")

            # disable resize of the window
            self.root.resizable(width=False, height=False) 

            # Header Frame
            self.headerFrame = Frame(self.root)
            self.headerFrame.place(x=0, y=0, width=600, height=75)
            self.headerFrame.configure(bg ="dark slate gray")
            Label(self.headerFrame, text = "New Task", bg = "dark slate gray", fg = "white", font = ("Courier 18 bold")).place(x=20, y=15)
            Year = Label(self.headerFrame, text = "2020", bg = "dark slate gray", fg = "white", font = ("Courier 12")).place(x=20, y=45)

            # Middle Frame
            self.middleFrame = Frame(self.root)
            self.middleFrame.place(x=0, y=76, width = 600, height = 425)
            self.middleFrame.configure(bg = "gray20")
            
            # Content of Middle Frame
            subjVar = StringVar(self.root)
            subjVar.set("Subject 0")
            typeVar = StringVar(self.root)
            typeVar.set("Task Type")

            Label(self.middleFrame, text = "Subject", bg = "gray20", fg = "white", font = ("Courier 10")).place(x=20, y=20)
            Subject = OptionMenu(self.middleFrame, subjVar, "Subject1", "Subject2", "Subject3")
            Subject["highlightthickness"]=0
            Subject.place(x=25, y=45)
            

            Label(self.middleFrame, text = "Due Date", bg = "gray20", fg = "white", font = ("Courier 10")).place(x=20, y=80)
            DueDate = Entry(self.middleFrame).place(x=25, y=105, height = 30)

            Label(self.middleFrame, text = "Type", bg = "gray20", fg = "white", font = ("Courier 10")).place(x=340, y=80)
            Type = OptionMenu(self.middleFrame, typeVar,  "Assignment", "Exam", "Quiz")
            Type["highlightthickness"]=0
            Type.place(x=345, y=105)

            Label(self.middleFrame, text = "Title", bg = "gray20", fg = "white", font = ("Courier 10")).place(x=20, y=140)
            Title = Entry(self.middleFrame).place(x=25, y=165, width = 300, height = 30)
            
            Label(self.middleFrame, text = "Detail", bg = "gray20", fg = "white", font = ("Courier 10")).place(x=20, y=200)
            Details = Entry(self.middleFrame)
            Details.place(x=25, y=225, height = 150, width = 550)

            Button(self.middleFrame, text = "Cancel", bg = "gray80", fg = "gray10", font =("Courier 10")).place(x=25, y=385)
            Button(self.middleFrame, text = "Save", bg = "steel blue", fg = "white", font =("Courier 10")).place(x=532, y=385)




if __name__ == "__main__":
    x = Screens()

    



