
import tkinter
from tkinter import messagebox
import subprocess
from tkinter import filedialog

class Shell_runner:

    def shell_script(self,checker):
        if checker == 0:
            messagebox.showwarning(title="Warning", message='Please check the box to run shell scripts')
        elif checker == 1:
            print("Checking")
            file_path = filedialog.askopenfile(title="Select a file",filetypes=[("Shell Scripts", "*.sh")])




        else:
            return
