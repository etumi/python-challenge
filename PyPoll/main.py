#Load dependencies
import pandas as pd

#set input file
task2_input_file = "Resources/election_data.csv"

#create data frame
polling_df = pd.read_csv(task2_input_file)

#calculate total number of votes
total_votes = polling_df["Voter ID"].count()

#list of candidates
candidates = polling_df["Candidate"].unique().tolist()

#Number of votes each candidate got
polling_df["Candidate"].value_counts()

#Number of candidates
num_of_candidates = len(candidates)

#Create dataframe of tallied votes
polls_summary = pd.DataFrame(polling_df["Candidate"].value_counts())

#Rename columns
polls_summary2 = polls_summary.rename(columns ={'Candidate': 'Number of Votes'})

#Add percentage of votes
polls_summary2["Percentage of Votes(%)"] = polls_summary2["Number of Votes"]/total_votes*100

#Obtain max votes
max_votes = polls_summary2["Number of Votes"].max()

#Get the index of the winner
winner = polls_summary2.index[polls_summary2['Number of Votes'] == max_votes].tolist()

#Print final results
print(f"Election Results")
print(f"------------------------------")
print(f"Total Votes: {format(total_votes, ',.0f')}")
print(f"------------------------------")
for i in polls_summary2.index:
    print(f"{i}: {format(polls_summary2.loc[i,'Percentage of Votes(%)'],',.3f')}% ({format(polls_summary2.loc[i,'Number of Votes'],',.0f')})")
print(f"------------------------------")
for i in winner:
    print(f"Winner: {i}")
print(f"------------------------------")

#Create output file
task2_output_file= open(r"Output/Task2 Summary.txt", "w")

#store output summary in list
output_text = [f"Election Results \n", f"------------------------------ \n", f"Total Votes: {format(total_votes, ',.0f')} \n",
f"------------------------------ \n"]
for i in polls_summary2.index:
    output_text.append(f"{i}: {format(polls_summary2.loc[i,'Percentage of Votes(%)'],',.3f')}% ({format(polls_summary2.loc[i,'Number of Votes'],',.0f')}) \n")
output_text.append(f"------------------------------ \n")
for i in winner:
    output_text.append(f"Winner: {i} \n")
output_text.append(f"------------------------------ \n")

#output summary into text file
task2_output_file.writelines(output_text)