##PyBank
#This script analyzes profits/losses per month 
#Input = CSV file with column 0 as month and column 1 as profits/losses
#Output = total months, average change in profits/losses per month, greatest increase/decrease 
#Output to txt file and terminal

#TO DO: create nice README - https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet 

#References
#Ramos, L.P. (2020). "How to Iterate Through a Dictionary in Python". realpython.com
#Geeksforgeeks. (2017). "Reading and Writing to text files in Python". geeksforgeeks.org
#Geeksforgeeks. (2019). "Python return statement". geeksforgeeks.org

import os
import csv

budget_data = os.path.join('Resources', 'budget_data.csv')

#stores header and data from CSV files as lists; determines total entries in file and total profits/loss
#input = file path
#output = total months, total profits/losses, list of months and list of profits/losses
def processCSVdata(file_path):
    with open(file_path, 'r') as csvfile:
        months = []
        profitsLosses = []
        netTotal = 0
        csvreader =csv.reader(csvfile, delimiter=',')
        header = next(csvreader)
        for row in csvreader:
            months.append(row[0])
            profitsLosses.append(int(row[1]))
            netTotal += int(row[1])
        totalMonths = len(months)
    return totalMonths, netTotal, months, profitsLosses


#calculates change in profits/losses per month 
#input = list of months, list of profits/losses
#output = new list of changes between months
#cannot calculate change for the month at index [0]
def calculateChanges(months, profitsLosses):
    changesPerMonth = []
    for value in profitsLosses[1:]:
        valueBefore = profitsLosses[(profitsLosses.index(value)-1)]
        change = value - valueBefore
        changesPerMonth.append(change)
    return changesPerMonth

#determines average 
#input = list of numerical values
#output = average (float) rounded to 2 decimal points
def average(listNums):
    total = 0
    for num in listNums:
        total += num
    average = round(total/len(listNums), 2)
    return average
    
#write string to a txt file
#input = string 
#output = txt file named results in folder 'Analysis
def writeTxt(analysis):
    outputPath = os.path.join('Analysis', 'results.txt')
    with open(outputPath, 'w') as txtfile:
        txtfile.writelines(analysis)

totalMonths, netTotal, months, profitsLosses = processCSVdata(budget_data)
changesPerMonth = calculateChanges(totalMonths, profitsLosses)
changeAverage = average(changesPerMonth)


#determines max/min changes in profits/losses; finds associated month from CSV file
maxIncrease = max(changesPerMonth)
monthmaxIncrease = months[changesPerMonth.index(maxIncrease)+1]
maxDecrease = min(changesPerMonth)
monthmaxDecrease = months[changesPerMonth.index(maxDecrease)+1]

#creates a properly formatted string of entire analysis
analysisWriteUp = (f'Financial Analysis \n---------------------------- \nTotal Months: ' 
f'{totalMonths} \nTotal: ${netTotal} \nAverage Change: ${changeAverage}'
f'\nGreatest Increase in Profits: {monthmaxIncrease} (${maxIncrease})' 
f'\nGreatest Decrease in Profits: {monthmaxDecrease} (${maxDecrease})')

print(analysisWriteUp)
writeTxt(analysisWriteUp)
