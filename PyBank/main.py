##PyBank
# This script analyzes profits/losses per month 
# Input = CSV file with column 0 as month and column 1 as profits/losses
# Output = total months, average change in profits/losses per month, greatest increase/decrease in terminal and txt file

#References
#Ramos, L.P. (2020). "How to Iterate Through a Dictionary in Python". realpython.com

import os
import csv

budget_data = os.path.join('Resources', 'budget_data.csv')

#stores header as list and data from CSV file as dict; determines total entries in file
with open(budget_data, 'r') as csvfile:
    budgetDict = {}
    totalMonths = 0
    csvreader =csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    for row in csvreader:
        budgetDict[row[0]] = int(row[1])
        totalMonths += 1



