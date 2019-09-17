#Module Name: get_file_path
#Module Purpose: To open a simple dialog box to prompt users for a file path and to return that file path
#Author: Adam Metwally
#Date: 2019.09.13

from tkinter import Tk 
from tkinter.filedialog import askopenfilename

def get_file_name():
    Tk().withdraw() #Prevents tkinter from opening GUI
    filename = askopenfilename() #Prompts user to select a file and gets the filename
    return filename



