import mysql.connector as mysql
mydb=mysql.connect(
    host='localhost',
    user='root',
    password='',
    database='test'
)
mycursor=mydb.cursor()
# Create Database
mycursor.execute('CREATE TABLE users(User_id int PRIMARY KEY AUTO_INCREMENT,Name varchar(40), Phone varchar(20),Date_of_Birth date)')
# 1.Insert data to table
sql=""" insert into users(Name,Phone,Date_of_Birth) values('Ann','88 99 77 12','1990-01-20'),('Ben','55 66 77321','1992-02-22')"""
mycursor.execute(sql)
mydb.commit()

# 2.Insert data to table
sql="insert into users(Name,Phone,Date_of_Birth) values(%s,%s,%s)"
values=('Oscar','+47945990','2020-03-20')
mycursor.execute(sql,values)
mydb.commit()
#3:Insert data to table
sql="""INSERT INTO users(Name,Phone,Date_of_Birth) values(%s,%s,%s)"""
values=[('Clara','+47939777','2021-03-02'),('Ishika','+919567432','2020-03-28'),('Riaan','+919087654','2019-02.28')]
mycursor.executemany(sql,values)
mydb.commit()

# id=mycursor.lastrowid
# print(id)
#Fetching data from table
mycursor.execute('select *from users')
result=mycursor.fetchall()
for row in result:
    print(row)

record=mycursor.fetchone()
print(record)

mycursor.execute('select *from users where User_id=1')
record=mycursor.fetchone()
for row in record:
    print(row)


#  Reading column names from result
field_names=[x[0] for x in mycursor.description]
print(field_names)
print(mycursor.description)
