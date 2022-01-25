import sqlite3

#  Create Database
conn = sqlite3.connect('company.db')

if not conn:
    print('Db not created')
cursor = conn.cursor()
#  Create table
sql = """ CREATE TABLE IF NOT EXISTS USERS(Id INTEGER PRIMARY KEY AUTOINCREMENT,NAME VARCHAR(20))"""
cursor.execute(sql)
conn.commit()

#  Insert into table
sql1 = """ INSERT INTO users(name) values ('Ishi'),('Ishika'),('Maalu'),('Kajol')"""
cursor.execute(sql1)
conn.commit()

#  Select data
cursor.execute('select *from users')
result = cursor.fetchall()
for row in result:
    print(row)

# Update,Delete & Like queries

cursor.execute("UPDATE users set NAME='Diya' where id=1")

cursor.execute('DELETE from users where Name="Kajol"')

cursor.execute('SELECT * FROM users where NAME LIKE "I%"')
conn.commit()
