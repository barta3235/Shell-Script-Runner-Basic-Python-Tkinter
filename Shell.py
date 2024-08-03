
import tkinter
import subprocess
from tkinter import filedialog

class Shell_runner:

    # passing the widget
    def __init__(self , output_text_widget):
        self.output_text_widget = output_text_widget

    def run_shell_script(self,file):
        print(file)

