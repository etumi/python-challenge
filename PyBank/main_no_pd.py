#Import dependacies
import os
import csv
import statistics as stat

#Set input file
input_file_path  = os.path.join( 'Resources', 'budget_data.csv')
#task1_input_file = "Resources/budget_data.csv"


with open(input_file_path, newline='') as input_file:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(input_file, delimiter=',')

    csv_header = next(csvreader)

    #get the months
    months = []
    tot_profit_loss = 0
    profit_loss = []
    profit_loss_change = []
    date = []


    # Read each row of data after the header. create: list of only profit loss, months and calculate total profit/loss
    for row in csvreader:
        months.append(row[0][:3])
        tot_profit_loss = tot_profit_loss + float(row[1])
        profit_loss.append(float(row[1]))
        date.append(row[0])
    
    tot_num_months = len(months)

    #calculate change for each profit/loss
    for i in range(len(profit_loss)-1):
        change = profit_loss[i+1] - profit_loss[i]
        profit_loss_change.append(change)

#Obtain average, min and max Changes
avg_change = stat.mean(profit_loss_change)

max_change = max(profit_loss_change)

min_change = min(profit_loss_change)

#get the index of max and min in date list
max_change_index = profit_loss_change.index(max_change) + 1

min_change_index = profit_loss_change.index(min_change) + 1

#print summary
print(f"Financial Analysis")
print("--------------------------")
print(f"Total Months: {tot_num_months}")
print(f"Total: ${format(tot_profit_loss, ',.2f')}")
print(f"Average Change: ${format(avg_change, ',.2f')}")
print(f"Greatest Increase in Profits: {date[max_change_index]} (${format(max_change, ',.2f')})")
print(f"Greatest Decrease in Profits: {date[min_change_index]} (${format(min_change, ',.2f')})")

#Create output file
output_file= open(r"Output/PyBank_Summary.txt", "w")

#store output summary in list
output_text = [f"Financial Analysis \n", f"-------------------------- \n", f"Total Months: {len(months)} \n", f"Total: ${format(tot_profit_loss, ',.2f')} \n",
f"Average Change: ${format(avg_change, ',.2f')} \n", f"Greatest Increase in Profits: {date[max_change_index]} (${format(max_change, ',.2f')}) \n",
f"Greatest Decrease in Profits: {date[min_change_index]} (${format(min_change, ',.2f')}) \n" ]

#output summary into text file
output_file.writelines(output_text)        
        

        

