import pandas as pd
#print(pd.__version__)
mydataset={'cars':['Tesla','Audi','Jagur'],
           'Ranking':[1,2,3]}
# Converting to dataframe
dataf=pd.DataFrame(mydataset)

fruits=['Apple','orange','banana']
myvar=pd.Series(fruits,index=['A','B','C'])

#  Locate data

#print(dataf.loc[0])
#print(dataf.loc[1:2])
print(dataf.loc[:1])

#  Loading CSV data
# pdf=pd.read_csv('cars.csv')
# pd.options.display.max_rows=100
# data=pdf.to_string()
# print(data)
# print(pdf.loc[:80])

#  Converting JSON file to dataframe
pdf=pd.read_json('EmployeeData.json')
