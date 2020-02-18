#Import dependacies
import os
import csv
import statistics as stat

#Set input file
input_file_path  = os.path.join( 'Resources', 'election_data.csv')

#create variables
voters = []
candidates_all = []

with open(input_file_path, newline='') as input_file:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(input_file, delimiter=',')

    csv_header = next(csvreader)

    for row in csvreader:
        voters.append(row[0])
        candidates_all.append(row[2])

    candidates = list(set(candidates_all))

    total_votes = len(voters)

    cand_summary = {}

    for cand in candidates:
        cand_summary.update({cand: [0]})
        counter = 0

        input_file.seek(0)
        next(csvreader)
        for row in csvreader:
            if row[2] == cand:
                counter = counter + 1
        votes_info = []
        percentage_votes = round(counter/total_votes,10)
        votes_info.append(counter)
        votes_info.append(percentage_votes)
        cand_summary[cand] = votes_info
            
winning_per = 0

for i in cand_summary:
    if cand_summary[i][1] > winning_per:
        winning_per = cand_summary[i][1]
        winner = i

print(f"Election Results")
print(f"------------------------------")
print(f"Total Votes: {format(total_votes, ',.0f')}")
print(f"------------------------------")
for i in cand_summary:
    print(f"{i}: {format(cand_summary[i][1]*100,',.3f')}% ({format(cand_summary[i][0],',.0f')})")
print(f"------------------------------")
print(f"Winner: {winner}")

#Create output file
output_file= open(r"Output/PyPoll_Summary.txt", "w")

#store output summary in list
output_text = [f"Election Results \n", f"------------------------------ \n", f"Total Votes: {format(total_votes, ',.0f')} \n",
f"------------------------------ \n"]
for i in cand_summary:
    output_text.append(f"{i}: {format(cand_summary[i][1]*100,',.3f')}% ({format(cand_summary[i][0],',.0f')}) \n")
output_text.extend([f"------------------------------ \n", f"Winner: {winner} \n", f"------------------------------ \n"])

#output summary into text file
output_file.writelines(output_text)

