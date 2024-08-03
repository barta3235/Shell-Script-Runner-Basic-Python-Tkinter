from Shell import Shell_runner
import tkinter


class Application:
    def __init__(self):
        self.mainWindow=tkinter.Tk()


        # creating instance of the pther class
        self.shell_runner = Shell_runner()


        self.mainWindow.geometry("800x500")
        self.mainWindow.title("Shell Script Runner")

        # Adding label for the button
        self.label = tkinter.Label(self.mainWindow, text="Select Shell Script", font=('Arial', 16))
        self.label.pack(pady=20)

        # check state
        self.checkSate = tkinter.IntVar()

        # button, passing shell_script function as a parameter
        self.button = tkinter.Button(self.mainWindow, text='Upload Script', font=('Arial', 14),command=lambda : self.shell_runner.shell_script(self.checkSate.get()))
        self.button.pack(padx=50, pady=10)


        # Check box
        self.check = tkinter.Checkbutton(self.mainWindow, text='Yes, run the script', font=('Arial', 12), variable=self.checkSate)
        self.check.pack(padx=10, pady=10)

        # Opening the window
        self.mainWindow.mainloop()


if __name__ == '__main__':
    app = Application()