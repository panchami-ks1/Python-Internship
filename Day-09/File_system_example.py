#  File System
#  Write to a file
import os

if not os.path.exists("myfiles/test.txt"):
    fp = open('myfiles/test.txt', 'w')
    if (fp):
        print('file created in w mode')
        str_data = "First Line\n"
        fp.write(str_data)  # Existing content overwrite
    else:
        print('Unable to create file')

else:
    fp = open('myfiles/test.txt', 'a')
    str_data = 'second line\n'
    fp.write(str_data)

# To write a list of data
fp = open('myfiles/test.txt', 'a')
list_data = ['text\n', 'text1\n', 'text2\n']
fp.writelines(list_data)

# Read a file
fpr = open("myfiles/test.txt", 'r')
x = fpr.read(20)
print(x)
print(fpr.read())

# Reset fpr
fpr.seek(0)

# Read line
while True:
    line = fpr.readline()
    if not line:
        break
    print(line.strip())  # Unwanted space remove

#   Read multiple lines
x = fpr.readlines()
for line in x:
    print(line)

fpr.close()
# file permissions
os.mkdir('newfolder', 0o444)
fp = open('newfolder/test.txt', 'w')
fp.write('newline')
