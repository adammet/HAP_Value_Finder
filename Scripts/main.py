#Module Name: main 
#Module Purpose: To prompt the user for a HAP Output PDF file, 
# and to find within that file all of the sensible cooling, latent cooling and heating loads for every space.
# then to export that data into a concise output to be copyable to an Excel spreadsheet.
#Author: Adam Metwally
#Date: 2019.09.13

#Import helper functions
from to_csv import to_csv
from get_file_path import get_file_name
from find_space_loads import find_space_loads

pdf_path = get_file_name() #Recieve the file path from the user of the PDF to parse through
csv_path = pdf_path.replace(".pdf",".csv")  #Create a file path for a CSV file
txt_path = pdf_path.replace(".pdf", ".txt") #Create a file path for a TXT file

to_csv(pdf_path,csv_path) #Convert the PDF into a CSV since it is more parseable
find_space_loads(csv_path,txt_path) #Create the txt file for users
