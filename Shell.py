import os
import tkinter
import subprocess
from tkinter import filedialog

class Shell_runner:

    # passing the widget
    def __init__(self , output_text_widget):
        self.output_text_widget = output_text_widget

    def run_shell_script(self,file):
        print(file)

       # making bash file executable if not
        if not os.access(file,os.X_OK):
            subprocess.call(['chmod','+x',file])

        #running the script on the output_text_widget
        try:
            output= subprocess.run(['bash',file],check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE,text=True)
            # clearing output screen
            self.output_text_widget.delete(1.0, tkinter.END)
            self.output_text_widget.insert(tkinter.END,output.stdout)
            self.output_text_widget.insert(tkinter.END, output.stderr)

        except Exception as e:
            self.output_text_widget.delete(1.0, tkinter.END)
            self.output_text_widget.insert(tkinter.END, "Error: "+str(e))

