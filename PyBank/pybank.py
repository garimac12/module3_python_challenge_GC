#!/usr/bin/env python
# coding: utf-8

# In[70]:


# Dependencies
import os
import csv
import statistics

# file to upload and output

file_to_load = os.path.join(".", "Resources", "budget_data.csv")

file_to_output = os.path.join(".", "budget_analysis.txt")

# Initialization

total_months = 0 
total_value = 0
current_change_list = []

month_of_changes =[]

greatest = [" ", 0]
least = [" ", 0]

# read the csv and convert into a list 

with open (file_to_load, "r") as financial_analysis:
    csv_reader = csv.reader(financial_analysis, delimiter = ",")
    
    #print (csv_reader)
    
    # Reader the header row
    csv_header = next(csv_reader)
    
    #print(f"Header: {csv_header}")
    
    # Move to next row and store the current row in a variable
    first_row = next(csv_reader)
    previous_change = int(first_row[1])
    total_value = total_value + int(first_row[1])
    total_months = total_months + 1
    
    for row in csv_reader:
        
        # Total number of months in the dataset
        total_months = total_months + 1
        
        # net total amount of "profit/losses"
        total_value = int(row[1]) + total_value
        
        # average change over the entire period
        current_change = int(row[1]) - previous_change
        previous_change = int(row[1])
        current_change_list.append(current_change)
                
        #greatest increase in profits
        if current_change > greatest[1] and current_change > 0:
            greatest[1] = current_change
            greatest[0] = row[0]
 
          
        
        #greatest decrease in profits
        if current_change < least[1] and current_change < 0 :
            least[1] = current_change
            least[0] = row[0]
 
        
        
        #print (row)
        
        
#print(current_change_list)
    
           
     
output = (
    f" Financial Analysis\n "
    f"---------------------------------\n"
    f" Total Months = {total_months} \n"
    f" Total:  ${total_value} \n"
    f" Average Change:  $ {statistics.mean(current_change_list):.2f} \n"
    f" Greatest Increase in Profits:  {greatest[0]} (${greatest[1]}) \n"
    f" Greatest Decrease in Profits:  {least[0]} (${least[1]}) \n"
    )

print(output)  

with open (file_to_output, "w") as txt_file:
    txt_file.write(output)
    
    
    


# In[ ]:





# In[ ]:




