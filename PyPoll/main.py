#Load dependencies
import pandas as pd

#set input file
task2_input_file = "Resources/election_data.csv"

#create data frame
polling_df = pd.read_csv(task2_input_file)
polling_df.head()

#check to see if there are any missing rows
polling_df.count()

#check to see if anyone voted twice
polling_df["Voter ID"].value_counts()

#calculate total number of votes
total_votes = polling_df["Voter ID"].count()
total_votes

#Number of votes each candidate got
polling_df["Candidate"].value_counts()

#Number of candidates
num_of_candidates = len(polling_df["Candidate"].unique())
num_of_candidates

#Create dataframe of tallied votes
polls_summary = pd.DataFrame(polling_df["Candidate"].value_counts())

#Rename columns
polls_summary = polling_votes.rename(columns ={'Voter ID': 'Number of Votes'})