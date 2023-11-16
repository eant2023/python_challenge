
import os

import csv

election_path = os.path.join("..", "resources", "election_data.csv")

#Initialize variables
all_candidates = []
total_vote = 0
vote_choice = {} 
win_cand = ["",0]
win_tot = 0
vote = 0


with open(election_path,"r") as csvfile:

     csvreader = csv.DictReader(csvfile)

     
     for row in csvreader:
          
          vote = vote + 1
          
          cand_nm = row ["Candidate"]

                
          if cand_nm not in all_candidates:

               all_candidates.append(cand_nm)

               vote_choice[cand_nm] = 0

          else:
               vote_choice[cand_nm] = vote_choice[cand_nm] + 1
      

if (vote > win_tot):
 win_cand [1] = vote_choice
 win_cand [0] = cand_nm
     
winner = sorted(vote_choice.items(),)
         
      

print("Election Results")     
print("------------------------------")
print(f"Total Votes: {vote}")
print("------------------------------")
print(f"{vote_choice}")
print(f"Winner" + str(winner[1]))   


