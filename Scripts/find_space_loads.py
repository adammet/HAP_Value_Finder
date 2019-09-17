#Module Name: find_space_loads
#Module Purpose: To parse a CSV file from HAP for sensible cooling, latent cooling and heating values
#Author: Adam Metwally
#Date: 2019.09.13

import csv
import sys
file_path = "C:/Users/CAAM070972/Desktop/Python/Sample_PDF/Floor_6_REV03.csv" #file path of csv to parse
output_file_path = file_path.replace(".csv", ".txt")

def find_space_loads(file_path, output_file_path):
    searchable_1 = "Component" #The thing to search for when looking for space titles
    searchable_2 = ">> Total Zone Loads" #The thing to search for when looking for space loads
    txt_file = open(output_file_path, "w+")

    with open(file_path) as f: #open the CSV file
        reader = csv.reader(f) 
        sens_cooling_list = []
        lat_cooling_list = []
        heat_list = []
        txt_file.write("Your project's sensible cooling, latent cooling and heating loads are shown below. \n \n")
        for row in reader: #parse through all of the CSV rows
        
            if searchable_1 in row[0]: #Check if the next entry is a space title
                next_title = row[0] #get the next title
                next_title_formatted = next_title.split() #split the csv row to put into readable format
                first_index = 5 #get rid of beginning garbage, the number of words at the beginning will always be the same based on HAP output
                last_index = len(next_title_formatted) - 4 #get rid of end garbage, the number of words at the end will always be the same based on HAP output
           
                readable_title = " ".join(next_title_formatted[first_index:last_index]) #create a user friendly title using the join method without garbage

                txt_file.write("Space Name: " + readable_title + '\n') #print title
        
            if searchable_2 in row[0]: #Check if the next entry has the sensible/latent/heating loads
                next_numbers = row[0]
                next_numbers_formatted = next_numbers.split() #split the csv row
                sensible_cooling = next_numbers_formatted[5] #find specific load
                sens_cooling_list.append(sensible_cooling) #add to list for copyable format
                latent_cooling = next_numbers_formatted[6] #find specific load
                lat_cooling_list.append(latent_cooling) #add to list for copyable format
                sensible_heating = next_numbers_formatted[8] #find specific load
                heat_list.append(sensible_heating) #add to list for copyable format
                txt_file.write("Sensible Cooling = " + sensible_cooling + " BTU/hr, Latent Cooling = " + latent_cooling + " BTU/hr, Sensible Heating = " + sensible_heating + " BTU/hr" +'\n' '\n') #print the useful information

    
        #Print a more usable format for users
        txt_file.write("\n")

        txt_file.write("Copyable Sensible Cooling Loads in BTU/hr (in order shown above):" + '\n')
        for i in range(len(sens_cooling_list)):
            txt_file.write(sens_cooling_list[i] + "\n")
    
        txt_file.write("\n")

        txt_file.write("Copyable Latent Cooling Loads in BTU/hr (in order shown above):" + '\n')
        for i in range(len(lat_cooling_list)):
            txt_file.write(lat_cooling_list[i] + "\n")

        txt_file.write("\n")

        txt_file.write("Copyable Heating Loads in BTU/hr (in order shown above):" + '\n')
        for i in range(len(heat_list)):
            txt_file.write(heat_list[i] + "\n")



