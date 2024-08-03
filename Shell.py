import os
import tkinter
import subprocess
from tkinter import filedialog
from tkinter import messagebox

class Shell_runner:

    # passing the widget
    def __init__(self , output_text_widget):
        self.output_text_widget = output_text_widget

    def run_shell_script(self,file):
        print(file)

        # making bash file executable if not
        if not os.access(file,os.X_OK):
            subprocess.call(['chmod','+x',file])

        git_bash_path = r"C:\Program Files\Git\bin\bash.exe"


        #running the script on the output_text_widget
        try:
            output = subprocess.run([git_bash_path,file],check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,text=True)
            # clearing output screen
            self.output_text_widget.delete(1.0, tkinter.END)
            self.output_text_widget.insert(tkinter.END,output.stdout)
            self.output_text_widget.insert(tkinter.END, output.stderr)

        except Exception as e:
            self.output_text_widget.delete(1.0, tkinter.END)
            self.output_text_widget.insert(tkinter.END, "Error: "+str(e))

