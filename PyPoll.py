# What we need to find
# 1. Total number of votes cast
# 2. List of candidates who received votes
# 3. Number of votes per candidate
# 4. Percentage of overall votes per candidate
# 5. Winner of the election based on popular vote

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
#create winning_candidate, winning counts and % tracker
winning_candidate=""
winning_count=0
winning_percentage=0


#Open and read election results file
with open(file_to_load) as raw_election_data:

    #Perform Analysis
    #read the file object with the reader function
    file_reader=csv.reader(raw_election_data)

    #read the HEADER rows
    headers=next(file_reader)
    
    #print each row
    for row in file_reader:
        #increment total votes var by 1
        total_votes += 1
        #print the candidate name from each row
        candidate_name = row[2]
        
        #append candidate names to the candidate options list if not already present
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            #start tracking that candidates votes
            candidate_votes[candidate_name]=0
        #add a vote to that candidates count
        candidate_votes[candidate_name]+=1

#Open and write results to text file
with open(file_to_save,"w") as txt_file:
    #print the final vote count
    election_results=(
        f"Election Results\n"
        f"----------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"----------------\n")
    print(election_results, end="")
    txt_file.write(election_results)


    #calculate percentage of votes
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
        f"---------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Percentage: {winning_percentage:.1f}%\n"
        f"Winning Vote Count: {winning_count:,}\n")
    print(winning_candidate_summary, end="")
    txt_file.write(winning_candidate_summary)
