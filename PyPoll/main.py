#PyPoll
#This script analyzes voting records to determine a list of candidates and which of these candidates won.
#This script reads a CSV file with voter id at column[0] and candidate at column[2]

#References
#The Python Tutorial. Python 3.6.12 Documentation. "Data Structures: Dictionaries". docs.python.org
#Geeksforgeeks. (2020). "Python | Get key with maximum value in Dictionary". geeksforgeeks.org
#https://www.geeksforgeeks.org/python-get-key-with-maximum-value-in-dictionary/

import os
import csv

electionData = os.path.join('Resources', 'election_data.csv')

#Code Questions: 
#should I check for dupes in the voter IDs? 
#what's going on with the rounding? 
       
#stores header and data from CSV files ; determines total entries in file and total votes per candidate
#input = file path
#output = total number votes, dict with candidates as key and total votes per candidate as values
def processCSVdata(file_path):
    with open(file_path, 'r') as csvfile:
        voterIDs = []
        totalVotes = 0
        candidatesVotes = {}
        csvreader =csv.reader(csvfile, delimiter=',')
        header = next(csvreader)
        for row in csvreader:
            totalVotes += 1
            if row[2] not in candidatesVotes:
                candidatesVotes[row[2]] = [0]
            candidatesVotes[row[2]][0] += 1
    return totalVotes, candidatesVotes

totalVotes, candidatesVotes = processCSVdata(electionData)

#calculates percentage votes won by each candidate
#input = totalVotes = int, candidatesVotes = dict, key = candidate name, value = total number votes (type is list)
#output = adds percentage votes won to the end of the list associated with the candidate
def calculatePercentWon(totalVotes, candidatesVotes):
    for key in candidatesVotes.keys():
        percentWon = candidatesVotes[key][0]/totalVotes*100
        candidatesVotes[key].append(percentWon)
    return candidatesVotes

candidatesVotes = calculatePercentWon(totalVotes, candidatesVotes)

print(candidatesVotes)
#Part 3: analyze data
    # % votes won by each candidate (append this to each candidate's list in the dict)
    # winner based on popular vote (max value in dict at specific index of list? see above for potential ways to do this)

#Part 4: data output
    #compile fancy string with all info
    #print fancy string and write to a txt file