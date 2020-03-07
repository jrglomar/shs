from tkinter import *
from screens.login import *
from screens.registration import *
import mysql.connector

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


if __name__ == "__main__":
    x = Screens()

    



