#Import denpendacies
import pandas as pd
import numpy as np

#Set input file
task1_file = "Resources/budget_data.csv"

#read in file
budget_df = pd.read_csv(task1_file)
budget_df.head(10)

#Check data types
budget_df.dtypes
budget_df.count()

#get the months out of the dates
budget_df["Month"] = budget_df["Date"].str[:3]
budget_df.head(10)

#get the year out of the dates
budget_df["Year"] = budget_df["Date"].str[-4:]
budget_df.head(10)

#Total number of months
months = budget_df["Month"]
len(months)

#Total Profits
tot_profit_loss = budget_df["Profit/Losses"].sum()
tot_profit_loss

#Calculate Percent change 
budget_df["Percent Change"] = round(budget_df["Profit/Losses"].pct_change(),2)
budget_df

#Obtain min and max Percent Changes
max_change = budget_df["Percent Change"].max()
max_change

min_change = budget_df["Change"].min()
min_change

