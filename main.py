from tkinter import *
import mysql.connector
from tkinter.scrolledtext import ScrolledText
from db.database import *
from tkcalendar import DateEntry
import datetime as dt
from time import *

fontVar = "Calibri"

class Defaults():
      def __init__(self, parent):
            self.root = parent

      def defaultScreen(self):
            # Default center screen config
            width = self.root.winfo_screenwidth()
            height = self.root.winfo_screenheight()
            x = int(width / 2 - 1024 / 2)
            y = int(height / 2 - 770 / 2)
            reso = "1024x720+"+ str(x) + "+" + str(y)

            # Default size config
            self.root.geometry(reso)
            self.root.title("Study Helper v1.0")
            self.root.configure(bg = "gray17")

            # To disable window resize
            self.root.resizable(width=False, height=False)

      def menuFrame(self):
            # ===== Menu Frame ===== #
            self.menuFrame = Frame(self.root)
            self.menuFrame.place(x=0, y=0, height = 720, width=50)
            self.menuFrame.configure(bg ="dark slate gray")

      def newTaskScreen(self):
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


class Transitions():
      def __init__(self, parent):
            self.root = parent

      def loginScreen(self):      
            self.root.destroy()
            screen = Screens()
            screen.loginPage()

      def registrationScreen(self):
            self.root.destroy()
            screen = Screens()
            screen.registrationPage()
            
      def homeScreen(self):
            self.root.destroy()
            screen = Screens()
            screen.homePage()

      def newTaskScreen(self):
            screen = Screens()
            screen.newTaskPage()

      def destroyNewTask(self):
            self.root.destroy()
      
      def subjectScreen(self):      
            self.root.destroy()
            screen = Screens()
            screen.subjectPage()


class Screens():
      def __init__(self):
            pass

      # =========================================== VALIDATION =========================================== # 
      # =========================================== VALIDATION =========================================== # 
      # =========================================== VALIDATION =========================================== #       

      # Global Variables
      def getDateToday(self):
            self.x = dt.datetime.now()
            self.mixed = (self.x.strftime("%A") + ", " + self.x.strftime("%B") + " " + self.x.strftime("%d"))
            self.date = StringVar()
            self.date.set(self.mixed)

      # Validation for Registration
      def userRegistration(self):
            self.db = UserDb()
            self.transition = Transitions(self.root)
            data = (self.regUserEntry.get(), self.regPassEntry.get())
            if self.regUserEntry.get() == "":
                  self.regAlert.set("Enter Username First")

            elif self.regPassEntry.get() == "":
                  self.regAlert.set("Enter Password First")
                  
            elif self.regPass2Entry.get() == "":
                  self.regAlert.set("Enter Password First")

            elif len(self.regUserEntry.get()) < 6:
                  self.regAlert.set("Invalid Username. Minimum of 6 characters")

            elif len(self.regPassEntry.get()) < 8:
                  self.regAlert.set("Invalid Password. Minimum of 8 characters")      

            elif self.regUserEntry.get().isalnum():     
                  if(self.regPassEntry.get() == self.regPass2Entry.get()):  
                        test = self.db.userRegistration(data, self.regUserEntry.get())
                        if not test:
                              self.colorAlert.set('green')
                              self.transition.loginScreen()
                        else:
                              self.regAlert.set("Username already exist")
                  else:
                        self.regAlert.set("Password do not match!")
            else:
                  self.regAlert.set("Invalid username. Use alphanumeric only.")
                        
      # Validation for Login
      def userLogin(self):
            self.transition = Transitions(self.root)
            self.db = UserDb()
            data = (self.logUserEntry.get(), self.logPassEntry.get())

            if self.logUserEntry.get() == "":
                  self.logAlert.set("Enter Username First")
                  
            elif self.logPassEntry.get() == "":
                  self.logAlert.set("Enter Password First")
                  
            else:
                  test = self.db.userLogin(data)
                  if test:
                        self.logAlert.set("Login Successfully")
                        self.colorAlert.set('green')
                        self.transition.homeScreen()
                  else:
                        self.logAlert.set("Wrong username/password")

      # Validation for New Task
      def newTask(self):
            self.transition = Transitions(self.root)
            self.db = UserDb()
            Type = self.typeVar.get()
            Title = self.Title.get()
            DueDate = self.DueDate.get()
            Details = self.Details.get('1.0', END)

            data = (Type, Title, DueDate, Details,
            )

            if self.DueDate.get() == "":
                  self.regAlert.set("Please fill up the blanks")

            elif self.Title.get() == "":
                  self.regAlert.set("Please fill up the blanks")
                  
            elif self.Details.get('1.0', END) == "":
                  self.regAlert.set("Please fill up the blanks")
            else:
                  self.db.newTask(data)
                  self.transition.destroyNewTask()

      # =========================================== FRAMES =========================================== # 
      # =========================================== FRAMES =========================================== # 
      # =========================================== FRAMES =========================================== # 

      # It calls all the images that can be used
      def imageUsed(self):
            self.logo = PhotoImage(file = "images\logo.png")
            self.pup = PhotoImage(file = "images\PUPLogo.png")
            self.menuLogo = PhotoImage(file = "images\menulogo.png")
            self.menuDashBoard = PhotoImage(file = "images\menudashboard.png")
            self.menuTask = PhotoImage(file = "images\menutask.png")
            self.menuSubject = PhotoImage(file = "images\menusubject.png")
            self.menuProgress = PhotoImage(file = "images\menuprogress.png")

      
      # Default startlogo frame It is the default logo frame for Start Page, Login Page, and Registration Page
      def startPageLogoFrame(self):
            self.LogoFrame = Frame(self.root)
            self.LogoFrame.place(x=385, y=75)      

      # Default startmiddle frame. It is the default middle frame for the Start Page, Login Page, and Registration Page
      def startPageOptionFrame(self):
            self.OptionFrame = Frame(self.root)
            self.OptionFrame.place(x=385, y=340)
            self.OptionFrame.configure(bg ="gray17")
      
      # Default Frame for Homepage
      def homePageFrame(self):
            # Line Frame1
            self.lineFrame = Frame(self.root)
            self.lineFrame.place(x=408, y=0, height = 720, width=2)
            self.lineFrame.configure(bg = "gray20")

            # Line Frame2
            self.lineFrame2 = Frame(self.root)
            self.lineFrame2.place(x=766, y=0, height = 720, width=2)
            self.lineFrame2.configure(bg = "gray20")

            # Header Frame 
            self.headerFrame = Frame(self.root)
            self.headerFrame.place(x=0, y=0, width=1024 ,height = 120)
            self.headerFrame.configure(bg = "gray20")

            # Top left Frame
            self.topLeftFrame = Frame(self.root)
            self.topLeftFrame.place(x=100, y=0, width=408 ,height = 120)
            self.topLeftFrame.configure(bg = "gray20")

            # Top middle Frame
            self.topMiddleFrame = Frame(self.root)
            self.topMiddleFrame.place(x=410, y=0, width=408 ,height = 120)
            self.topMiddleFrame.configure(bg = "gray20")

            # Top right Frame
            self.topRightFrame = Frame(self.root)
            self.topRightFrame.place(x=770, y=0, width=408 ,height = 120)
            self.topRightFrame.configure(bg = "gray20")

            # Menu Frame
            self.menuFrame = Frame(self.root)
            self.menuFrame.place(x=0, y=0, height = 720, width=100)
            self.menuFrame.configure(bg ="dark slate gray")

            # Content Left Frame
            self.contentLeftFrame = Frame(self.root)
            self.contentLeftFrame.place(x=100, y=120)
            self.contentLeftFrame.configure(bg ="gray17")

            # Content Middle Frame
            self.contentMiddleFrame = Frame(self.root)
            self.contentMiddleFrame.place(x=410, y=120)
            self.contentMiddleFrame.configure(bg ="gray17")

            # Content Right Frame
            self.contentRightFrame = Frame(self.root)
            self.contentRightFrame.place(x=770, y=120)
            self.contentRightFrame.configure(bg ="gray17")

      # Default Frame for NewTaskPage
      def newTaskFrame(self):
            # Header Frame
            self.headerFrame = Frame(self.root)
            self.headerFrame.place(x=0, y=0, width=600, height=75)
            self.headerFrame.configure(bg ="dark slate gray")
            Label(self.headerFrame, text = "New Task", bg = "dark slate gray", fg = "white", font = (fontVar,"18", "bold")).place(x=20, y=15)
            Year = Label(self.headerFrame, text = "2020", bg = "dark slate gray", fg = "white", font = (fontVar,"12")).place(x=20, y=45)

            # Middle Frame
            self.middleFrame = Frame(self.root)
            self.middleFrame.place(x=0, y=76, width = 600, height = 425)
            self.middleFrame.configure(bg = "gray20")            

      # =========================================== PAGES =========================================== # 
      # =========================================== PAGES =========================================== # 
      # =========================================== PAGES =========================================== # 

      # Start page or default screen page
      def startPage(self):
            self.root = Tk()
            self.default = Defaults(self.root)
            self.transition = Transitions(self.root)
            self.default.defaultScreen()
            self.startPageLogoFrame()
            self.startPageOptionFrame()
            self.imageUsed()
            
            # Logo Display of startPage
            Label(self.LogoFrame, image=self.logo, bg = "gray17").pack()

            # Welcome Label
            Label(self.OptionFrame, text="Welcome to Study Helper", bg = "gray17", fg = "SlateGray2", height = "3", font = (fontVar, "18")).pack()

            # Login Button
            Button(self.OptionFrame, text="Login", bg = "steel blue", fg = "snow", width = "12", font = (fontVar, "12"), command = self.transition.loginScreen).pack()

            # Spacer
            Label(self.OptionFrame, text = "", bg = "gray17", font = (fontVar, "1")).pack()

            # Register Button
            Button(self.OptionFrame, text="Register", bg = "steel blue", fg = "snow", width = "12", font = (fontVar, "12"), command = self.transition.registrationScreen).pack()

            # Loop to start
            self.root.mainloop()
            
      # Login page
      def loginPage(self):
            self.root = Tk()
            self.default = Defaults(self.root)
            self.transition = Transitions(self.root)
            self.default.defaultScreen()
            self.startPageLogoFrame()
            self.startPageOptionFrame()
            self.imageUsed()
            
            self.logAlert = StringVar()
            self.colorAlert = StringVar()
            self.colorAlert.set('red')
            self.logSuccess = StringVar()

            # Showing Logo
            Label(self.LogoFrame, image=self.logo, bg = "gray17").pack()

            # Welcome Label
            Label(self.OptionFrame, text="Welcome to Study Helper", bg = "gray17", fg = "SlateGray2", height = "2", font = (fontVar,"18")).pack()

            # Account Login Label
            Label(self.OptionFrame, text="Account Login", bg = "gray17", fg = "steel blue", font = (fontVar,"15")).pack()

            # Username Label and Entry
            Label(self.OptionFrame, text="Username", bg = "gray17", fg = "Snow", font = (fontVar,"10")).pack()
            self.logUserEntry = Entry(self.OptionFrame, bg = "snow")
            self.logUserEntry.pack()

            # Password Label and Entry
            Label(self.OptionFrame, text="Password", bg = "gray17", fg = "Snow", font = (fontVar,"10")).pack()
            self.logPassEntry = Entry(self.OptionFrame, bg = "snow", show = "*")
            self.logPassEntry.pack()
            Label(self.OptionFrame, text = "", bg = "gray17", font = (fontVar,"1")).pack()
            
            # Login Button
            Button(self.OptionFrame, command = self.userLogin, text="Login", bg = "steel blue", fg = "snow", width = "8", font = (fontVar,"10")).pack()
            
            # Message Alert
            #Label(self.OptionFrame, textvariable=self.loginSuccess, bg = "gray17", font =(fontVar, "8")).pack()
            Label(self.OptionFrame, textvariable=self.logAlert, bg = "gray17", fg = self.colorAlert.get(), font = (fontVar, "8")).pack()  

            # To Registration Window 
            Label(self.OptionFrame, "", bg = "gray17", width = 4).pack(side=LEFT)
            Label(self.OptionFrame, text = "Don't have an account yet?", bg = "gray17", fg = "white", font = (fontVar,"8")).pack(side=LEFT)
            Button(self.OptionFrame, text="Click here", bg = "gray17", fg = "steel blue", relief = "flat", font = (fontVar,"8"), command = self.transition.registrationScreen).pack(side=LEFT)

      # Registration Page
      def registrationPage(self):
            self.root = Tk()
            self.default = Defaults(self.root)
            self.transition = Transitions(self.root)
            self.default.defaultScreen()
            self.startPageLogoFrame()
            self.startPageOptionFrame()
            self.imageUsed()
            self.regAlert = StringVar()
            self.colorAlert = StringVar()
            self.colorAlert.set('red')

            
            # Showing Logo
            Logo = Label(self.LogoFrame, image=self.logo, bg = "gray17")
            Logo.image = self.logo
            Logo.pack()
      

            # Welcome Label
            Label(self.OptionFrame, text="Welcome to Study Helper", bg = "gray17", fg = "SlateGray2", height = "2", font = (fontVar,"18")).pack()

            # Account Registration Label
            Label(self.OptionFrame, text="Account Registration", bg = "gray17", fg = "steel blue", font = (fontVar,"15")).pack()

            # Username Label and Entry
            Label(self.OptionFrame, text="Username", bg = "gray17", fg = "Snow", font = (fontVar,"10")).pack()
            self.regUserEntry = Entry(self.OptionFrame, bg = "snow")
            self.regUserEntry.pack()

            # Password Label and Entry
            Label(self.OptionFrame, text="Password", bg = "gray17", fg = "Snow", font = (fontVar,"10")).pack()
            self.regPassEntry = Entry(self.OptionFrame, bg = "snow", show = "*")
            self.regPassEntry.pack()

            # Password 2 Label and Entry
            Label(self.OptionFrame, text="Re-type password", bg = "gray17", fg = "Snow", font = (fontVar,"10")).pack()
            self.regPass2Entry = Entry(self.OptionFrame, bg = "snow", show = "*")
            self.regPass2Entry.pack()
            Label(self.OptionFrame, text = "", bg = "gray17", font = (fontVar,"1")).pack()
            
            # Registration Button
            Button(self.OptionFrame, command = self.userRegistration, text="Register", bg = "steel blue", fg = "snow", width = "8", font = (fontVar,"10")).pack()

            # Message Alert
            #Label(self.OptionFrame, textvariable=self.regSuccess, bg = "gray17", font = (fontVar, "8")).pack()
            self.alert = Label(self.OptionFrame, textvariable=self.regAlert, bg = "gray17", fg = self.colorAlert.get(), font = (fontVar, "8")).pack()

            # To Login Window 
            Label(self.OptionFrame, "", bg = "gray17", width = 4).pack(side=LEFT)
            Label(self.OptionFrame, text = "Already have an account?", bg = "gray17", fg = "white", font = (fontVar,"8")).pack(side=LEFT)
            Button(self.OptionFrame, text="Click here", bg = "gray17", fg = "steel blue", relief = "flat", font = (fontVar,"8"), command = self.transition.loginScreen).pack(side=LEFT)

      # Home Page
      def homePage(self):
            self.root = Tk()
            self.default = Defaults(self.root)
            self.transition = Transitions(self.root)
            self.default.defaultScreen()
            self.homePageFrame()
            self.imageUsed()
            self.getDateToday()
            

            # Content of top left frame
            Today = Label(self.topLeftFrame, text = "Today", bg = "gray20", fg = "white", font = (fontVar, "18", "bold")).place(x = 20, y = 30)
            DayToday = Label(self.topLeftFrame, textvariable = self.date, bg = "gray20", fg = "white", font = (fontVar,"12")).place(x = 21, y = 60)

            # Content of top middle frame
            Tasks = Label(self.topMiddleFrame, text = "Tasks", bg = "gray20", fg = "white", font = (fontVar,"18", "bold")).place(x = 20, y = 30)
            NewTask = Button(self.topMiddleFrame, command = self.transition.newTaskScreen, text = "New Task +", bg = "steel blue", fg = "white", font = (fontVar,"12", "bold"), relief = "raised").place(x = 20, y = 65, height = 25)

            # Content of top right frame
            Tasks = Label(self.topRightFrame, text = "Exams", bg = "gray20", fg = "white", font = (fontVar,"18", "bold")).place(x = 20, y = 30)

            # Logo of menu frame
            Logo = Label(self.menuFrame, image = self.menuLogo, bg = "dark slate gray")
            Logo.image = self.menuLogo
            Logo.place(x=0, y=20, width = 100)

            # Content of menu frame
            menuDashBoard = Button(self.menuFrame, image = self.menuDashBoard, bg = "dark slate gray", relief = "flat", activebackground="dark slate gray")
            menuDashBoard.image = self.menuDashBoard
            menuDashBoard.place(x=29, y=140, width=40, height=40)
            
            menuTask = Button(self.menuFrame, image = self.menuTask, bg = "dark slate gray", relief = "flat", activebackground="dark slate gray")
            menuTask.image = self.menuTask
            menuTask.place(x=29, y=200, width=40, height=40)

            menuSubject = Button(self.menuFrame, command = self.transition.subjectScreen, image = self.menuSubject, bg = "dark slate gray", relief = "flat", activebackground="dark slate gray")
            menuSubject.image = self.menuSubject
            menuSubject.place(x=29, y=260, width=40, height=40)

            menuProgress = Button(self.menuFrame, image = self.menuProgress, bg = "dark slate gray", relief = "flat", activebackground="dark slate gray")
            menuProgress.image = self.menuProgress
            menuProgress.place(x=29, y=320, width=40, height=40)
 
      # New Task Page
      def newTaskPage(self):
            self.root = Tk()
            self.default = Defaults(self.root)
            self.default.newTaskScreen()            
            self.transition = Transitions(self.root)
            self.imageUsed()
            self.newTaskFrame()

            # Content of Middle Frame
            self.subjVar = StringVar(self.root)
            self.typeVar = StringVar(self.root)

            # Subject OptionMenu (Dropdown)
            Label(self.middleFrame, text = "Subject", bg = "gray20", fg = "white", font = (fontVar,"10")).place(x=20, y=20)
            self.Subject = OptionMenu(self.middleFrame, self.subjVar, "Subject1", "Subject2", "Subject3")
            self.Subject["highlightthickness"]=0
            self.Subject.place(x=25, y=45)
            
            # Due Date
            Label(self.middleFrame, text = "Due Date", bg = "gray20", fg = "white", font = (fontVar,"10")).place(x=20, y=80)
            self.DueDate = DateEntry(self.middleFrame, date_pattern = "y-mm-dd", foreground = "white", background = "steel blue")
            self.DueDate.place(x=25, y=105, height = 25)

            # Type OptionMenu (Dropdown)
            Label(self.middleFrame, text = "Type", bg = "gray20", fg = "white", font = (fontVar,"10")).place(x=340, y=80)
            self.Type = OptionMenu(self.middleFrame, self.typeVar, "Assignment", "Exam", "Quiz")
            self.Type["highlightthickness"]=0
            self.Type.place(x=345, y=105)

            # Title (Entry)
            Label(self.middleFrame, text = "Title", bg = "gray20", fg = "white", font = (fontVar,"10")).place(x=20, y=140)
            self.Title = Entry(self.middleFrame)
            self.Title.place(x=25, y=165, width = 415, height = 28)
            
            # Details (Entry)
            Label(self.middleFrame, text = "Detail", bg = "gray20", fg = "white", font = (fontVar,"10")).place(x=20, y=200)
            self.Details = ScrolledText(self.middleFrame, font = (fontVar, "9"))
            self.Details.place(x=25, y=225, height = 140, width = 550)

            # Cancel and Save (Button)
            Button(self.middleFrame, command = self.transition.destroyNewTask, text = "Cancel", bg = "gray80", fg = "gray10", font =(fontVar,"11")).place(x=25, y=379)
            Button(self.middleFrame, command = self.newTask, text = "Save", width = 5, bg = "steel blue", fg = "white", font =(fontVar,"11")).place(x=525, y=379)

      # Create New Subject
      def subjectPage(self):
            self.root = Tk()
            self.default = Defaults(self.root)
            self.default.defaultScreen()
            self.transition = Transitions(self.root)
            self.homePageFrame()
            self.imageUsed()
      


app = Screens()
app.startPage()




