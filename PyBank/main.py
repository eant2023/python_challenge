
import os
import csv

csvpath = os.path.join("..","pybank","resources","budget_data.csv")

# Open and Read csv
with open(csvpath) as csv_file:

    csvreader = csv.reader(csv_file, delimiter=",")

    csvheader = next(csvreader)

    print("Financial Analysis")
    print("---------------------------------------")


    month =0

    month =(len(list(csvreader)))  

    month=[0]




    

                           
                           
                          


