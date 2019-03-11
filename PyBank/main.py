#PyBank
import csv
import os

#Directory 
budget_data = os.path.join('..','Resources','budget_data.csv')

#Initial variables
Monthes = []
Balance = []
ListAveChanges = []

#Read file
with open(budget_data, mode='r') as csvfile:
    #Only get the info from each column instead of the special characters
    file_data = csv.reader(csvfile, delimiter=',')
    next(file_data,None)

    #Reading the file
    for row in file_data:
        #Add all the monthes to a list
        Monthes.append(row[0])
        TotalNumMonthes = len(Monthes)

        #Add all the money to a list
        Balance.append(int(row[1]))
        TotalBalance = sum(Balance)

        #Get a list of average changes
        ListAveChanges = [Balance[n+1] - Balance[n] for n in range(len(Balance) -1)]

#print(Balance)
#print(Monthes)
#print(TotalNumMonthes)
#print(TotalBalance)

AveChange = round(sum(ListAveChanges)/ len(ListAveChanges),2)

#print(ListAveChanges)
#print(AveChange)

#Find the position of the Max/Min values in the list
#Get the Max and Min of the list of each month balances
MaxProfit = max(ListAveChanges)
MinProfit = min(ListAveChanges)

Maxposition = ListAveChanges.index(MaxProfit)
Minposition = ListAveChanges.index(MinProfit)

#print(Maxposition)
#print(Minposition)
# Monthes list has one more index since Ave Changes list is missing the first month
Maxmonth = Monthes[Maxposition + 1]
Minmonth = Monthes[Minposition + 1]

#print(Maxmonth)
#print(Minmonth)

#Final Results
print("Financial Analysis")
print("-----------------------------")
print("Average Change: $ " + str(AveChange) )
print("Greatest Increase in Profits: " + Maxmonth + " ($" + str(MaxProfit) + ")")
print("Greatest Decrease in Profits: " + Minmonth + " ($" + str(MinProfit) + ")")