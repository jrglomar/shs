from tkinter import *

class App():
    def __init__(self):
        self.startPage()
    
    def defaultScreen(self):
        width = self.root.winfo_screenwidth()
        height = self.root.winfo_screenheight()
        x = int(width / 2 - 1024 / 2)
        y = int(height / 2 - 770 / 2)
        reso = "1024x720+"+ str(x) + "+" + str(y)

        # size of window configuration
        self.root.geometry(reso)
        self.root.title("Study Helper v1.0")
        self.root.configure(bg = "gray17")

        # disable resize of the window
        self.root.resizable(width=False, height=False)
        
    def startPage(self):
        self.root = Tk()
        self.defaultScreen()
        Button(self.root, text = "Login Page", command = self.loginPage).pack()
        self.root.mainloop()

    def loginPage(self):
        self.root = Tk()
        self.defaultScreen()
        Button(self.root, text = "Start Page", command = self.startPage).pack()
        self.root.mainloop()

system = App()

