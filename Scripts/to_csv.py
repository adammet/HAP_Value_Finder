#Module Name: to_csv
#Module Purpose: To convert a file in PDF format into a more parseable CSV fomrat using Python
#Author: Adam Metwally
#Date: 2019.09.12

#Import nessecary libraries
import camelot
from tkinter import messagebox
from PyPDF2 import PdfFileReader

#Function
def to_csv(pdf_path, output_path):
    pdf_path = pdf_path
    output_path = output_path

    try:
        tables = camelot.read_pdf(pdf_path, pages='1-2') #Get the tables
        tables.export(output_path, f='csv',compress = True )

    except AttributeError:
        messagebox.showerror("Operation cancelled!", "In order to continue, please re-run the program and select a PDF file.")

pdf_path = "C:/Users/CAAM070972/Desktop/Python/Test_File/Floor_6_REV03.pdf"
output_path = pdf_path.replace(".pdf",".csv")
to_csv(pdf_path,output_path)
 
