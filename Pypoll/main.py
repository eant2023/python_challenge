
import os

import csv

election_path = os.path.join("..", "resources", "election_data.csv")

#Initialize variables
county = []
candidate = []
total_vote = 0  
count = ()


with open(election_path,"r") as csvfile:

     csvreader = csv.reader(csvfile, delimiter=",")

     header = next(csvreader, None)


     for row in csvreader:
          
          vote = row[0]
          
          total_vote += 1

print("Election Results")
print("------------------------------")
print(f"Total Votes: {total_vote}")
print("------------------------------")

