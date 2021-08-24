import csv
import os
from collections import defaultdict
#Set path for file
csvpath =os.path.join("..","Resources","budget_data.csv")
#open file
columns = defaultdict(list) # each value in each column is appended to a list
with open(csvpath,newline='') as budget:
# open('budget_data.csv',newline='') as budget:
# open('test_data.csv',newline='') as budget:
    reader=csv.DictReader(budget)
    #next(budget)
    for row in reader: # read a row as {column1: value1, column2: value2,...}
        for (k,v) in row.items(): # go over each column name and value 
            columns[k].append(v)
    month=columns['Date']
    amount=columns['Profit/Losses']
    max_profit=0.0
    max_loss=0.0
    ctotal=0.0                #change total per month
    gtotal=int(amount[0])     #total profit/loss 
    ptotal=amount[0]
    average=0.0
    ctr=1
    mylist=[]                  #profit/loss changes list
    max_idx=0
    min_idx=0
    pmlist=0

            
    for i in range(1,len(amount)):
        amount[i]=float(amount[i])
        #pdate[i]=str(pdate[i])
        ctotal=float(amount[i])-float(amount[i-1])
        #ctotal is the change profit/loss total amount
        mylist.append(ctotal)
        gtotal += amount[i]
        ctr +=1 
    
    #get month of max and min PL
    for c, d in enumerate(mylist):
       #print(d)
       #print(min(mylist))
       if d==min(mylist):
          min_idx = c+1
          #print(min_idx)
    
    
       if d==max(mylist):
          max_idx=c+1
         # print(max_idx)
        
    tot_diff=sum(mylist)
    #print(tot_diff)
    average = round(tot_diff/i,2)
    max_profit=max(mylist)
    min_profit=min(mylist)
    print("Financial Analysis")
    print("___________________ ")
    print(" ")
    print(f"Total Months : {ctr} ")
    print(f"Total Profit/Loss : {gtotal}")
    print(f"Average Profit/Loss : {average}")
    #print(month[max_idx])
    #print(month[min_idx])
    #print(f"Greatest Increase in Profit : {max_profit}")
    print("Greatest Increase in Profit  :  "  + str(month[max_idx]) + "  ($"  + str(max_profit)+")")
    print("Greatest Decrease in Profit :  " + month[min_idx] + "  ($"  + str(min_profit)+")")

   # print("check profit/loss Jan amount   " + str(ptotal))

# Specify the file to write to
output_path = os.path.join("..", "Resources", "analysis_paybank.txt")

with open(output_path,'w', newline='') as file:

    # Initialize csv.writer
    csvwriter = csv.writer(file)
    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["----------------------------"])
    csvwriter.writerow(" ")
    csvwriter.writerow(["Total Months : "+str(ctr)])
    csvwriter.writerow(["Total Profit/Loss : "+str({gtotal})])
    csvwriter.writerow(["Average Profit/Loss : " +str({average})])
    csvwriter.writerow(["Greatest Increase in Profit  :  "  + str(month[max_idx]) + "  ($"  + str(max_profit)+")"])
    csvwriter.writerow(["Greatest Decrease in Profit :  " + str(month[min_idx]) + "  ($"  + str(min_profit)+")"])
