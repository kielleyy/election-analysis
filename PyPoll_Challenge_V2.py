# What this file will tabulate and output
# 1. Total number of votes cast
# 2. List of candidates who received votes
# 3. Number of votes per candidate
# 4. Percentage of overall votes per candidate
# 5. Winner of the election based on popular vote
# 6. List of counties that cast votes
# 7. Votes per county
# 8. Percentage of total votes per county
# 9. Identifying county with highest turnout
# 10. Results printed to election_analysis.txt
# 11. Results printed to command line

#add dependencies
import os
import csv

#Assign a variable for the file and find path
file_to_load=os.path.join("Resources","election_results.csv")

#Assign a variable and path for file to write to
file_to_save=os.path.join("analysis","election_analysis.txt")

#create total votes variable and set to zero
total_votes=0
#create candidate_options variable
candidate_options=[]
#create candidate votes dictionary
candidate_votes={}

# 1: Create a county list and county votes dictionary.
county_options = []
county_votes={}

#create winning_candidate, winning counts and % tracker
winning_candidate=""
winning_count=0
winning_percentage=0

# 2: Track the largest county and county voter turnout.
winning_county=""
winning_county_count=0
winning_county_percentage=0


#Open and read election results file
with open(file_to_load) as raw_election_data:

    #Perform Analysis
    #read the file object with the reader function
    file_reader=csv.reader(raw_election_data)

    #read the HEADER rows
    headers=next(file_reader)
    
    #for each row in the csv file
    for row in file_reader:
        #increment total votes var by 1
        total_votes += 1
        #get the candidate name from each row
        candidate_name = row[2]
        #item 3
        #get the county name from each row
        county_name = row[1]

        #append candidate names to the candidate options list if not already present
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            #start tracking that candidates votes
            candidate_votes[candidate_name]=0
        #add a vote to that candidates count
        candidate_votes[candidate_name]+=1

        #sections 4 and 5
        #append county names to the county options list if not already present
        if county_name not in county_options:
            county_options.append(county_name)
            #start tracking that county's votes
            county_votes[county_name]=0
        #add a vote to that county's count
        county_votes[county_name]+=1



#Open and write results to text file
with open(file_to_save,"w") as txt_file:
    #print the final vote count
    election_results=(
        f"Election Results\n"
        f"----------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"----------------\n\n"
        f"County Results:\n")
    print(election_results, end="")
    txt_file.write(election_results)


    #calculate percentage of votes
    #for loop to cycle through each county name with turnout
    for county_name in county_votes:
        #establish vote count per county
        turnout=county_votes[county_name]
        #percentage of county votes in relation to overall count
        turnout_percentage=float(turnout)/float(total_votes)*100
        #print county name and their percentage of votes
        county_results=(
            f"{county_name}: {turnout_percentage:.1f}%, ({turnout:,})\n")
        print(county_results,end="")
        txt_file.write(county_results)

        # Section 7 of challenge
        # determine county with largest turnout
        if (turnout>winning_county_count) and (turnout_percentage>winning_county_percentage):
            winning_county_count = turnout
            winning_county=county_name
            winning_county_percentage=turnout_percentage
    
    #print the winning county summary
    winning_county_summary = (
        f"------------------\n\n"
        f"County with Largest Turnout: {winning_county}\n"
        f"Winning Turnout Count: {winning_county_count:,}\n"
        f"Percentage of Overall Turnout: {winning_county_percentage:.1f}%\n")
    print(winning_county_summary, end="")
    txt_file.write(winning_county_summary)

    #print a header for the next section
    candidate_results_header=(
        f"-----------------\n\n"
        f"Candidate Results:\n")
    print(candidate_results_header,end="")
    txt_file.write(candidate_results_header)

    #for loop to cycle through each candidate name with candidate votes list
    for candidate_name in candidate_votes:
        #establish vote count per candidate
        votes=candidate_votes[candidate_name]
        #calculate percentage of candidate votes in relation to all votes
        vote_percentage=float(votes)/float(total_votes)*100
        #print candidate name and their percentage of votes
        candidate_results=(
            f"{candidate_name}: {vote_percentage:.1f}%, ({votes:,})\n")
        print(candidate_results, end="")
        txt_file.write(candidate_results)
            
            #determine winning vote count and winning candidate
            #set conditions of counter resetting to new candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

    #winning candidate summary
    winning_candidate_summary=(
        f"---------------------\n\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Percentage: {winning_percentage:.1f}%\n"
        f"Winning Vote Count: {winning_count:,}\n")
    print(winning_candidate_summary, end="")
    txt_file.write(winning_candidate_summary)
