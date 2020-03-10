from tkinter import *
import mysql.connector
from tkinter.scrolledtext import ScrolledText
from db.database import *

fontVar = "Calibri"
colorAlert = "red"

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


class Screens():
      def __init__(self):
            pass
            
      # Validation for Registration
      def userRegistration(self):
            self.db = UserDb()
            data = (self.regUserEntry.get(), self.regPassEntry.get())

            if self.regUserEntry.get() == "":
                  self.regAlert.set("Enter Username First")

            elif self.regPassEntry.get() == "":
                  self.regAlert.set("Enter Password First")
                  
            elif self.regPass2Entry.get() == "":
                  self.regAlert.set("Enter Password First")
                  
            else:
                  if(self.regPassEntry.get() == self.regPass2Entry.get()):  
                        test = self.db.userRegistration(data, self.regUserEntry.get())
                        if not test:
                              self.regAlert.set("Registration Successfully")
                              colorAlert = "green"
                              self.root.update()
                        else:
                              self.regAlert.set("Username already exist")
                              
                  else:
                        self.regAlert.set("Password do not match!")
                        
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

      # It calls all the images that can be used
      def imageUsed(self):
            self.logo = PhotoImage(file = "images\logo.png")
            self.pup = PhotoImage(file = "images\PUPLogo.png")

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
            self.alert = Label(self.OptionFrame, textvariable=self.regAlert, bg = "gray17", fg = colorAlert, font = (fontVar, "8")).pack()

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

            # Content of top left frame
            Today = Label(self.topLeftFrame, text = "Today", bg = "gray20", fg = "white", font = (fontVar, "18", "bold")).place(x = 20, y = 30)
            DateToday = Label(self.topLeftFrame, text = "Day, Month 0", bg = "gray20", fg = "white", font = (fontVar,"14")).place(x = 20, y = 60)

            # Content of top middle frame
            Tasks = Label(self.topMiddleFrame, text = "Tasks", bg = "gray20", fg = "white", font = (fontVar,"18", "bold")).place(x = 20, y = 30)
            NewTask = Button(self.topMiddleFrame, command = self.transition.newTaskScreen, text = "New Task +", bg = "steel blue", fg = "white", font = (fontVar,"12", "bold"), relief = "raised").place(x = 20, y = 65)

            # Content of top right frame
            Tasks = Label(self.topRightFrame, text = "Exams", bg = "gray20", fg = "white", font = (fontVar,"18", "bold")).place(x = 20, y = 30)

      # New Task Page
      def newTaskPage(self):
            self.root = Tk()
            self.default = Defaults(self.root)
            self.default.newTaskScreen()            
            self.transition = Transitions(self.root)
            self.imageUsed()
            self.newTaskFrame()

            # Content of Middle Frame
            subjVar = StringVar(self.root)
            subjVar.set("Subject 0")
            typeVar = StringVar(self.root)
            typeVar.set("Task Type")

            # Subject OptionMenu (Dropdown)
            Label(self.middleFrame, text = "Subject", bg = "gray20", fg = "white", font = (fontVar,"10")).place(x=20, y=20)
            Subject = OptionMenu(self.middleFrame, subjVar, "Subject1", "Subject2", "Subject3")
            Subject["highlightthickness"]=0
            Subject.place(x=25, y=45)
            
            # Due Date
            Label(self.middleFrame, text = "Due Date", bg = "gray20", fg = "white", font = (fontVar,"10")).place(x=20, y=80)
            DueDate = Entry(self.middleFrame).place(x=25, y=105, height = 25)

            # Type OptionMenu (Dropdown)
            Label(self.middleFrame, text = "Type", bg = "gray20", fg = "white", font = (fontVar,"10")).place(x=340, y=80)
            Type = OptionMenu(self.middleFrame, typeVar,  "Assignment", "Exam", "Quiz")
            Type["highlightthickness"]=0
            Type.place(x=345, y=105)

            # Title (Entry)
            Label(self.middleFrame, text = "Title", bg = "gray20", fg = "white", font = (fontVar,"10")).place(x=20, y=140)
            Title = Entry(self.middleFrame).place(x=25, y=165, width = 415, height = 28)
            
            # Details (Entry)
            Label(self.middleFrame, text = "Detail", bg = "gray20", fg = "white", font = (fontVar,"10")).place(x=20, y=200)
            Details = ScrolledText(self.middleFrame, font = (fontVar, "9"))
            Details.place(x=25, y=225, height = 140, width = 550)

            # Cancel and Save (Button)
            Button(self.middleFrame, command = self.transition.destroyNewTask, text = "Cancel", bg = "gray80", fg = "gray10", font =(fontVar,"11")).place(x=25, y=379)
            Button(self.middleFrame, command = self.transition.destroyNewTask, text = "Save", width = 5, bg = "steel blue", fg = "white", font =(fontVar,"11")).place(x=525, y=379)

app = Screens()
app.startPage()




