
import os
import csv

#Initialize variables
months = set()
total_prolos = 0    
start_rev = 0
all_rev =[]
diff_rev = []
rev_total = 0
month_change =[]


#Provide the path to CSV file

csv_path = os.path.join("..","resources","budget_data.csv")

# Open and Read csv
with open(csv_path, 'r') as csvfile:

    # Create a CSV reader object

    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header row 
    header = next(csvreader, None)

    ## Loop through each row in the CSV file
    for row in csvreader:

        # Extract the date from the row
        date = row[0]
        months.add(date)
        total_months = len(months)
        
        
        # Calulate sum of prof/loss
        prolos = int(row[1]) 
        total_prolos = total_prolos + prolos

        #Calculate avg change of pro/loss
        if start_rev != 0:
            diff_rev = prolos - start_rev
            all_rev.append(diff_rev)
            month_change.append(row[0])
            
        start_rev = prolos
    
    avg_change = sum(all_rev) / len(all_rev) if len(all_rev) > 0 else 0


increase_m = max(all_rev)
month_max = all_rev[all_rev.index(increase_m)]

decrease_m = min(all_rev) 
month_min = all_rev[all_rev.index(decrease_m)]



        

   

# Print the results
print("Financial Analysis")
print("---------------------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_prolos}")
print(f"Average Change: ${round(avg_change,2)}")
print(f"Greatest Increase in Profit: (${increase_m})")
print(f"Greatest Decrease in Profits: (${decrease_m})")


#output

output = (

    f"/nFinancial Analysis/"
    f"------------------------/"
    f"Total Months: {total_month}/"
    f"Average Change: ${round(avg_change,2)}/"
    f"Greatest Increase in Profits: {increase_m}/"
    f"Greatest Decrease in Profits: {decrease_m}/n")
 
output 

with open(csv_path,"w") as txt_file







    




    

                           
                           
                          


