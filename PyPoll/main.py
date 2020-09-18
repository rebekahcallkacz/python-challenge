#PyPoll
#This script analyzes voting records to determine a list of candidates and which of these candidates won.
#This script reads a CSV file with voter id at column[0] and candidate at column[2]

#References
#The Python Tutorial. Python 3.6.12 Documentation. "Data Structures: Dictionaries". docs.python.org
#Geeksforgeeks. (2020). "Python | Get key with maximum value in Dictionary". geeksforgeeks.org
#https://www.geeksforgeeks.org/python-get-key-with-maximum-value-in-dictionary/
#https://www.geeksforgeeks.org/python-get-key-from-value-in-dictionary/
#https://realpython.com/python-formatted-output/ 

import os
import csv

electionData = os.path.join('Resources', 'election_data.csv')
    
#stores header and data from CSV files ; determines total entries in file and total votes per candidate
#input = file path
#output = total number votes, dict with candidates as key and total votes per candidate as values
def processCSVdata(file_path):
    with open(file_path, 'r') as csvfile:
        totalVotes = 0
        candidatesVotes = {}
        csvreader = csv.reader(csvfile, delimiter=',')
        header = next(csvreader)
        for row in csvreader:
            totalVotes += 1
            if row[2] not in candidatesVotes:
                candidatesVotes[row[2]] = [0]
            candidatesVotes[row[2]][0] += 1
    return totalVotes, candidatesVotes

#calculates percentage votes won by each candidate
#input = totalVotes = int, candidatesVotes = dict, key = candidate name, value = total number votes (type is list)
#output = adds percentage votes won to the end of the list associated with the candidate
def calculatePercentWon(totalVotes, candidatesVotes):
    for key in candidatesVotes.keys():
        percentWon = candidatesVotes[key][0]/totalVotes*100
        candidatesVotes[key].append(percentWon)
    return candidatesVotes

#determines candidate with the most votes (compares total votes of each candidate)
#input = dict with key of candidate and values of list with total votes and percentage of votes
#output = winner of popular vote (string)
def determineWinner(candidatesVotes):
    listVotes = []
    for key in candidatesVotes:
        listVotes.append(candidatesVotes[key][0])
    highestVotes = max(listVotes)
    for key, value in candidatesVotes.items():
        if value[0] == highestVotes:
            return key

#formats data as a string
#input = dict (key=candidate names , values = [totalvotes, percentofvotes(float)]), candwinner, totalVotes
#output = string with results
def createReportString(dataDict, total, winner):
    voteReport = ""
    for key, value in dataDict.items():
        voteReport += f"{key}: {value[1]:.3f}% ({value[0]})\n"
    analysisWriteUp = (f'Election Results \n---------------------------- \nTotal Votes: ' 
    f'{total} \n----------------------------\n{voteReport}'
    f'---------------------------- \nWinner: {winner}\n----------------------------')
    return analysisWriteUp

#write entire analysis to a txt file
#input = string 
#output = txt file named results
def writeTxt(analysis):
    outputPath = os.path.join('Analysis', 'results.txt')
    with open(outputPath, 'w') as txtfile:
        txtfile.writelines(analysis)

totalVotes, candidatesVotes = processCSVdata(electionData)
candidatesVotes = calculatePercentWon(totalVotes, candidatesVotes)
candWinner = determineWinner(candidatesVotes)
reportString = createReportString(candidatesVotes, totalVotes, candWinner)

print(reportString)
writeTxt(reportString)
