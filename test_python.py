import numpy as np
import pandas as pd
import csv
print ("Hi this file is to test python,Pandas")
dates=pd.date_range('20190101',periods=6)
print(dates)
print("Second try for data frames")
df=pd.DataFrame(dates,columns=['datecolums'])
print df
data=np.array([['','col1','col2'],
               ['row1',1,2],
               ['row2',3,4]])
print(data)
#print("this is to show that comment function is working properly or not")
print(pd.DataFrame(data=data[1:,1:],index=data[1:,0],columns=data[0,1:]))
print("---********---Script End/Starting new one ---********---")

print("reading csv file ..")
filename='/Users/pradeepsekar/Desktop/work/test_examples/test_example1.csv'
with open (filename) as csvfile:
    readCSV=csv.reader(csvfile,delimiter=',')
    for row in readCSV:
        print(row)

print("inserting")
toAdd=["String","String","String","String"]
with open(filename,"r") as insertfile:
    reader=list(csv.reader(insertfile))
    print(reader.insert(2,toAdd))
