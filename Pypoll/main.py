import csv
import os


#Set path for file
csvpath =os.path.join("Resources","election_data.csv")

#csvpath =os.path.join("..","Resources","election_data.csv")
#open file
with open(csvpath,newline='') as election:
    reader=csv.reader(election)
    next(election)
    names=[item[2] for item in reader] 
    candidate_list=[]
    tally_list=[]
    pct_list=[]
   # result_list=[]
    ctr=0
    pct=0

    #print(names)
    ## create unique candidate list and get the total count of the csv file
    for candidate in names:
        if  candidate not in candidate_list:
            candidate_list.append(candidate)
        ctr +=1 #count all the rows in the input file
    

   # print(f'Total votes is : {ctr}')

    ##compare names and count the rows for each candidate(one row = one vote)
    for c,d in enumerate(candidate_list):
        #ctr=0
        c=0
        for b in names:
            if b==d:
                c +=1
        tally_list.append(c)
    
    ## computation for percentage 
    for vote in tally_list:
        Pct =((vote)/(ctr)) * 100
        Pct = round(Pct,2)
        pct_list.append(Pct)

for e,f in enumerate(tally_list):
    if f==max(tally_list):
        maxidx=e
    

## using zip
#anadata = zip(candidatelist,pct_list,tally_list)
#tanadata=tuple(anadata)


print("Election Results")
print("----------------------------")
print(f'Total votes is : {ctr}')
print("----------------------------")
for i in range(len(candidate_list)):
    print(f"{candidate_list[i]}:  {pct_list[i]}%  ({tally_list[i]})")
 
print("----------------------------")
print('Winner is :',candidate_list[maxidx])
print("----------------------------")

#print(result_list)
# print(f'Total votes is {ctr})')

#
#  Specify the file to write to
output_path = os.path.join("Analysis", "analysis_pypoll.txt")

with open(output_path,'w', newline='') as file:

    # Initialize csv.writer
    csvwriter = csv.writer(file, delimiter=",")
    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(["----------------------------"])
    csvwriter.writerow(" ")
    csvwriter.writerow(["Total votes : "+str(ctr)])
    csvwriter.writerow(["----------------------------"])
    for i in range(len(candidate_list)):
        csvwriter.writerow([candidate_list[i] + ": " + str(pct_list[i]) + "% (" +  str(tally_list[i]) + ")"])
    csvwriter.writerow(["----------------------------"])
    csvwriter.writerow(["Winner: "+ candidate_list[maxidx]])
    csvwriter.writerow(["----------------------------"])

