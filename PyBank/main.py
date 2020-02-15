#Import dependacies
import pandas as pd
import numpy as np

#Set input file
task1_input_file = "Resources/budget_data.csv"

#read in file
budget_df = pd.read_csv(task1_input_file)

#Check data types
budget_df.dtypes
budget_df.count()

#get the months out of the dates
budget_df["Month"] = budget_df["Date"].str[:3]
#budget_df.head(10)

#get the year out of the dates
budget_df["Year"] = budget_df["Date"].str[-4:]
#budget_df.head(10)

#Total number of months
months = budget_df["Month"]


#Total Profits
tot_profit_loss = budget_df["Profit/Losses"].sum()
#tot_profit_loss

#Calculate Percent change 
budget_df["Change"] = round(budget_df["Profit/Losses"].diff(),2)
#budget_df.head(10)

#Obtain average, min and max Percent Changes
avg_change = round(budget_df["Change"].mean(),2)
#avg_change

max_change = budget_df["Change"].max()
#max_change

min_change = budget_df["Change"].min()
#min_change

#row with max and min change
max_chnge_row = budget_df.loc[budget_df["Change"] == max_change]
min_chnge_row = budget_df.loc[budget_df["Change"] == min_change]

#print summary
print(f"Financial Analysis")
print("--------------------------")
print(f"Total Months: {len(months)}")
print(f"Total: ${format(tot_profit_loss, ',.2f')}")
print(f"Average Change: ${format(avg_change, ',.2f')}")
print(f"Greatest Increase in Profits: {max_chnge_row.iloc[0,0]} (${format(max_change, ',.2f')})")
print(f"Greatest Decrease in Profits: {min_chnge_row.iloc[0,0]} (${format(min_change, ',.2f')})")

#Create output file
task1_output_file= open(r"Output/Task1 Summary.txt", "w")

#store output summary in list
output_text = [f"Financial Analysis \n", f"-------------------------- \n", f"Total Months: {len(months)} \n", f"Total: ${format(tot_profit_loss, ',.2f')} \n",
f"Average Change: ${format(avg_change, ',.2f')} \n", f"Greatest Increase in Profits: {max_chnge_row.iloc[0,0]} (${format(max_change, ',.2f')}) \n",
f"Greatest Decrease in Profits: {min_chnge_row.iloc[0,0]} (${format(min_change, ',.2f')}) \n" ]

#output summary into text file
task1_output_file.writelines(output_text)
