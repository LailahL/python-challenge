import os
import csv

print("''' text")
print("Financial Analysis")
print("---------------------------")
months = []
profits_losses=[]
begval=[]
endval=[]
pchange=[]

table=('months', 'profits_losses','pchange')

csvpath=os.path.join('.','Resources', 'budget_data.csv')
with open (csvpath) as budget_file:
    budreader=csv.reader(budget_file,delimiter=",")
    
    cheader=next(budreader)
    
    for row in budreader:
        months.append(row[0])
        mcount=len(months)   
    print("Total Months: " + str(mcount))


with open (csvpath) as budget_file:
    budreader=csv.reader(budget_file,delimiter=",")
    
     
    for row in budreader:
        profits_losses.append(row[1])
        pnlsum=sum(int(row[1]) for row in budreader)
    print("Total: " + str(pnlsum))
  
with open (csvpath) as budget_file:
    budreader=csv.reader(budget_file,delimiter=",")
    cheader=next(budreader)
     
    for row in budreader:
        begval.append(row[1])

    pchange=next(row[1])-begval
    
   
    
        
        

        








