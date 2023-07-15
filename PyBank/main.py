# Import Dependencies
import os
import csv

print("Financial Analysis")
print("----------------------------")

# Read the csv file and does analysis
csvpath = os.path.join("Resources", "budget_data.csv")

with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",") 
    csv_header = next(csvreader)
    month = 0
    total = 0
    profitLoss = 0
    change = 0
    change1 = 0
    greatestInc = 0
    greatestDec = 0
    for row in csvreader:
        month = month + 1
        total = total + int(row[1])
        change = int(row[1]) - profitLoss
        if change != int(row[1]):
            change1 = change1 + change
            if change > greatestInc:
                greatestInc = change
                incMonth = row[0]
            if change < greatestDec:
                greatestDec = change
                decMonth = row[0]
        profitLoss = int(row[1])
    avgChange = '{0:.2f}'.format(change1/(month-1))
    print("Total Months: " + str(month))
    print("Total: $" + str(total))
    print("Average Change: $" + str(avgChange))
    print("Greatest Increase in Profits: " + incMonth + " ($" + str(greatestInc) + ")")
    print("Greatest Decrease in Profits: " + decMonth + " ($" + str(greatestDec) + ")")

output_path = os.path.join("analysis", "PyBank.txt")

# Write results to text file
with open(output_path,"w") as txtfile:
    txtfile.writelines("Financial Analysis \n")
    txtfile.writelines("---------------------------- \n")
    txtfile.writelines(f"Total Months: {month} \n")
    txtfile.writelines(f"Total: ${total} \n")
    txtfile.writelines(f"Average Change: ${avgChange} \n")
    txtfile.writelines(f"Greatest Increase in Profits: {incMonth} (${greatestInc}) \n")
    txtfile.writelines(f"Greatest Decrease in Profits: {decMonth} (${greatestDec}) \n")