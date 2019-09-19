#Module Name: to_csv
#Module Purpose: To convert a file in PDF format into a more parseable CSV fomrat using Python
#Author: Adam Metwally
#Date: 2019.09.12

#Import nessecary libraries
import tabula, pandas, numpy, distro
from tkinter import messagebox


#Function
def to_csv(pdf_path, output_path):
    pdf_path = pdf_path
    output_path = output_path
    try:
        tabula.convert_into(pdf_path,pages='all', guess=False,output_format="CSV",output_path=output_path) #Try to convert the file
    except AttributeError:
        messagebox.showerror("Operation cancelled!", "In order to continue, please re-run the program and select a PDF file.")


 
