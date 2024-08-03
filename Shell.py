
import tkinter
from tkinter import messagebox

class Shell_runner:

    def shell_script(self,checker):
        if checker == 0:
            messagebox.showwarning(title="Warning", message='Please check the box to run shell scripts')
        elif checker == 1:
            print('Here is your script')
        else:
            return
