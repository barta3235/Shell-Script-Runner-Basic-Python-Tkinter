import os
import tkinter
import subprocess
from tkinter import filedialog
from tkinter import messagebox

class Shell_runner:

    # passing the widget
    def __init__(self, output_text_widget):

        # for output_text
        # self.output_text_widget = output_text_widget

        pass

    def run_shell_script(self,file):
        print(file)

        # making bash file executable if not
        if not os.access(file,os.X_OK):
            subprocess.call(['chmod','+x',file])

        git_bash_path = r"C:\Program Files\Git\bin\bash.exe"
        terminal_command=f'start "" "{git_bash_path}" -c "{file}; exec bash"'

        #running the script on the output_text_widget
        try:
            # output = subprocess.run([git_bash_path,file],check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,text=True)
            # self.output_text_widget.delete(1.0, tkinter.END)
            # self.output_text_widget.insert(tkinter.END,output.stdout)
            # self.output_text_widget.insert(tkinter.END, output.stderr)

            subprocess.Popen(terminal_command, shell=True)

        except Exception as e:
            # self.output_text_widget.delete(1.0, tkinter.END)
            # self.output_text_widget.insert(tkinter.END, "Error: "+str(e))

            messagebox.showerror("Error: "+str(e))

