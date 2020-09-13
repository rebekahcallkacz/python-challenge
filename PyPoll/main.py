#PyPoll
#This script analyzes voting records to determine a list of candidates and which of these candidates won.
#This script reads a CSV file with voter id at column[0] and candidate at column[2]

#References
#The Python Tutorial. Python 3.6.12 Documentation. "Data Structures: Dictionaries". docs.python.org
#Geeksforgeeks. (2020). "Python | Get key with maximum value in Dictionary". geeksforgeeks.org
#https://www.geeksforgeeks.org/python-get-key-with-maximum-value-in-dictionary/

#Part 1: read in CSV file

#Part 2: store/capture data - while iterating through CSV rows
    #total # votes cast (keep list of voter ids to remove dupes)
    #dict with keys as candidates and values as running totals of votes
        #generate empty dict 
        #check if candidate is in dict as a key
        #if no, add candidate as key with value of a list containing 0
        #if yes, add 1 to candidate value
        #return total votes and dict which contains candidates and their total votes

#Part 3: analyze data
    # % votes won by each candidate (append this to each candidate's list in the dict)
    # winner based on popular vote (max value in dict?)