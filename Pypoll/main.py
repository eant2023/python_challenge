
# for this project I utilized the assistance of the following Youtube video to assist
# with my coding:https://www.youtube.com/watch?v=cdwlWjjwxlc&list=PLBNHcTwrlK2h-3_kPuZo597i3mMUOA0oe&index=2&t=8s


import os

import csv

#Paths to files to load and output

election_path = os.path.join("..", "resources", "election_data.csv")
election_path_out=("..","python_challege","Pypoll","analysis.txt")

#Initialize variables
all_candidates = []
total_vote = 0
vote_choice = {} 
win_cand = ["",0]
win_tot = 0
vote = 0

# Open csv files and dictionary
with open(election_path,"r") as csvfile:

     csvreader = csv.DictReader(csvfile)

# Vote counter     
     for row in csvreader:
          
          vote = vote + 1

#Gets candidates names
          cand_nm = row ["Candidate"]

                
          if cand_nm not in all_candidates:

               all_candidates.append(cand_nm)

               vote_choice[cand_nm] = 0

          else:
               vote_choice[cand_nm] = vote_choice[cand_nm] + 1
      
#Determine winner of election
if (vote > win_tot):
 win_cand [1] = vote_choice
 win_cand [0] = cand_nm
     
winner = sorted(vote_choice.items(),)
         
      
#Prints results and writes to text file
with open(analysis, "w") as txt_file:
    
    election_results = (
    f"\n\nElections= Results\n"
    f"--------------------------\n"
    f"Total Votes:      {vote}\n"
    f"---------------------------\n"
)
print(election_results)

print("Election Results")     
print("------------------------------")
print(f"Total Votes: {vote}")
print("------------------------------")

print(f"Winner" + str(winner[1]))   