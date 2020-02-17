#Import dependacies
import os
import csv
import statistics as stat

#Set input file
input_file_path  = os.path.join( 'Resources', 'election_data.csv')

#create variables
votes = []
candidates_all = []

with open(input_file_path, newline='') as input_file:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(input_file, delimiter=',')

    csv_header = next(csvreader)
    print(csv_header)

    for row in csvreader:
        #print(row)
        votes.append(row[0])
        candidates_all.append(row[2])

    candidates = list(set(candidates_all))

    cand_summary = {}

    for cand in candidates:
        cand_summary.update({cand: 0})
        print(cand_summary)
        counter = 0
        print(counter)
        print(cand)
        print(csvreader)

        input_file.seek(0)
        next(csvreader)
        for row in csvreader:
            #print(row[0])
            if row[2] == cand:
                #print(row[2])
                counter = counter + 1
        print(counter)
        cand_summary[cand] = counter
                    #Khan_count =  Khan_count + 1
                #elif row[2] == 'Correy':
                    #   Correy_count = Correy_count + 1
                #elif row[2] == "O'Tooley":
                    #   Tooley_count = Tooley_count + 1
                #elif row[2] == "O'Tooley":
            

total_votes = len(votes)
candidates = list(set(candidates_all))

#print(candidates)
#print(total_votes)
#print(cand_summary)

