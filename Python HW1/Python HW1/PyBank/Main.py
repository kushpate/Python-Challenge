+import os
import csv

#file path
os.chdir(os.path.dirname(__file__))
csvpath = os.path.join('budget_data.csv')

#Read csv
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #Variables after the first line is read
    #Skip header
    next(csvreader)

    months = []
    profit = []

    for  row in csvreader:
        months.append(row[0]) 
        profit.append(row[1])
    #Numbers of months
    num_months = len(months)

    #Convert strings to ints and sum profit
    int_profit = map(int,profit)
    total_profit = sum(int_profit)

    #Find average changes in profit/loss over entire period
    revenue_change = []

    for profit_month in range(1, len(profit)):
        revenue_change.append((int(profit[profit_month]) - int(profit[profit_month-1])))

        revenue_average = sum(revenue_change) / len(revenue_change)
    #print(revenue_average)

    #Greatest increase in profits
    greatest_increase = max(revenue_change)
    greatest_decrease = min(revenue_change)

    #Print results
    print(f"Financial Analysis:")
    print("-------------------------------------------------------")
    print(f"Total Months: {num_months}")
    print(f"Total: ${total_profit} USD")
    print(f"Average Revenue Change: ${revenue_average} USD")
    print("Greatest Increase in Profits: " + str(months[revenue_change.index(max(revenue_change))+1]) + " " + "$" + str(greatest_increase))
    print("Greatest Increase in Profits: " + str(months[revenue_change.index(min(revenue_change))+1]) + " " + "$" + str(greatest_decrease))

    #Write file
    filewriter = open("write_data.txt", "w")

    filewriter.write(f"Financial Analysis\n")
    filewriter.write(f"------------------------------------------\n")
    filewriter.write(f"Total months: {num_months}\n")
    filewriter.write(f"Total: ${total_profit}\n")
    filewriter.write("Greatest Increase in Profits: " + str(months[revenue_change.index(max(revenue_change))+1]) + " " + "$" + str(greatest_increase) + "\n")
    filewriter.write("Greatest Decrease in Profits: " + str(months[revenue_change.index(min(revenue_change))+1]) + " " + "$" + str(greatest_decrease) + "\n")

    #filewriter.close()