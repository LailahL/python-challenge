
import os
import csv

print("'''")
print("Election Results")
print("-----------------------------")

ballot=[]
county=[]
candidate1=[]
candidate2=[]
candidate3=[]
vote1=0
vote2=[]
vote3=[]


table=('ballot','county', 'candidate')

csvpath=os.path.join('.','Resources','election_data.csv')
with open(csvpath) as elect_file:
    ereader=csv.reader(elect_file,delimiter=",")
    eheader=next(ereader)
    for row in ereader:
        ballot.append(row[0])
        bcount=len(ballot)
    print("Total Votes : " + str(bcount))
    print("-----------------------------")


with open(csvpath) as elect_file:
    ereader=csv.reader(elect_file,delimiter=",")
    eheader=next(ereader)
    for i, row in enumerate(ereader):
       if i==2 and row[2]!="":
           candidate1.append(row[2])
           vote1=int(vote1)+1
           i=i+1
        if i+1 and row[2]==candidate1:
 
    print(str(vote1))
           

        
   


        