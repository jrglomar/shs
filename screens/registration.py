from tkinter import *


class RegistrationWindow:

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
        
        # LoginButton
        Button(self.OptionFrame,
               text="Register",
               bg = "steel blue",
               fg = "snow",
               width = "8",
               font = ("Courier 10")).pack()


        # loop to run the tkinter
        self.root.mainloop()
        
if __name__ == "__main__":
    x = RegistrationWindow()
