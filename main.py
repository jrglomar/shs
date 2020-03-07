from tkinter import *
from screens.login import *
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
        
        Button(self.root, image = self.logo, command = self.loginScreen).pack()
    
        self.root.mainloop()
        
    def loginScreen(self):
        # destroy current window
        self.root.destroy()

        #open the new window
        log = LoginWindow()


if __name__ == "__main__":
    x = Screens()

    



