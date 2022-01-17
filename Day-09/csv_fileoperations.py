"""How to create and write a CSV file in core python"""
fp=open('myfiles/data.csv','w')
mydata='''Name,Email,Phone
Arjun,a@gmail.com,777777
Ishi,I@gmail.com,666666
Pan,P@gmail.com,555555'''
fp.write(mydata)

with open('myfiles/data.csv','r') as fpr:
    data=fpr.readlines()
    for line in data:
        # print(line.strip())
        print(line.split(','))
