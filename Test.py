from Shell import Shell_runner
import tkinter
from tkinter import messagebox
from tkinter import filedialog

class Application:
    def __init__(self):
        self.mainWindow=tkinter.Tk()


        # creating instance of the other class
        self.shell_runner = Shell_runner()


        self.mainWindow.geometry("800x500")
        self.mainWindow.title("Shell Script Runner")

        # Adding label for the button
        self.label = tkinter.Label(self.mainWindow, text="Select Shell Script", font=('Arial', 16))
        self.label.pack(pady=20)

        # check state
        self.checkSate = tkinter.IntVar()

        # button, passing shell_script function as a parameter
        # self.button = tkinter.Button(self.mainWindow, text='Upload Script', font=('Arial', 14),command=lambda : self.shell_runner.shell_script(self.checkSate.get()))
        self.button = tkinter.Button(self.mainWindow, text='Upload Script', font=('Arial', 14),command= lambda : self.run_command(self.checkSate.get()))
        self.button.pack(padx=50, pady=10)


        # Check box
        self.check = tkinter.Checkbutton(self.mainWindow, text='Yes, run the script', font=('Arial', 12), variable=self.checkSate)
        self.check.pack(padx=10, pady=10)

        # Opening the window
        self.mainWindow.mainloop()

    # run script

    def run_command(self,checker):
        if checker == 0:
            messagebox.showwarning(title="Warning", message='Please check the box to run shell scripts')

        elif checker == 1:
            print("Checking")

            # selecting file from local pc
            file_path = filedialog.askopenfile(title="Select a file", filetypes=[("Shell Scripts", "*.sh")])
            self.shell_runner.run_shell_script(file_path)

        else:
            return




if __name__ == '__main__':
    app = Application()