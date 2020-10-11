# What we need to find
# 1. Total number of votes cast
# 2. List of candidates who received votes
# 3. Number of votes per candidate
# 4. Percentage of overall votes per candidate
# 5. Winner of the election based on popular vote

import os
import csv
#Assign a variable for the file and find path
file_to_load=os.path.join("Resources","election_results.csv")

#Assing a variable and path for file to write to
file_to_save=os.path.join("analysis","election_analysis.txt")

#Open and write counties to the file
with open(file_to_save,"w") as txt_file:
    txt_file.write("Counties in the Election\n---------------------\n")
    txt_file.write("Arapahoe\nDenver\nJefferson")

#Open and read election results file
with open(file_to_load) as raw_election_data:

    #Perform Analysis
    #read the file object with the reader function
    file_reader=csv.reader(raw_election_data)

    #print the HEADER rows
    headers=next(file_reader)
    print(headers)
#    for row in file_reader:
 #       print(row[0])

