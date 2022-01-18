import csv
import os
import time
from datetime import  datetime

# CSV operations
csvData=[
    ['Name','Age'],
['peter','22'],
['Ann','20']]

with open('data.csv','w',newline='') as csvFile:
    writer=csv.writer(csvFile)
    writer.writerows(csvData)
with open('data.csv','r',newline="") as csvFile:
    reader=csv.reader(csvFile)
    for row in reader:
        print(row)
# OS commands
os.getcwd()  # current working directory
os.chdir()  # change Directory
os.listdir()#  List directory
os.rename('old_name','new_name')
os.remove('Filename')
os.rmdir('folder_name')#remove directory
os.path.exists()
os.path.join('path')
os.chmod('path','permission')
os.mkdir()
os.mkdirs()

#datetime,timestamp
x=datetime.now()
print(x)
print(x.strftime('%Y'))
timestamp=int(time.time())
print(timestamp)
date=datetime.fromtimestamp(timestamp)
print(date.strftime('%B'))
time_stamp=datetime.timestamp(x)
print(time_stamp)




