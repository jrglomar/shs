class Default:
      def __init__(self):
            # create a tkinter window
            self.root = Tk()

            # to scenter the screen
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
