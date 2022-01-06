str1 = "Hello world"
print(str1[2])
print(str1[2:7])
print(len(str1))
print(str1.lower())
print(str1.upper())
print(str1.replace("Hello", "hi"))
str2 = "@hello@"
print(str2.lstrip("@"))
print(str2.rstrip("@"))
print(str2.strip("@"))
x = 8
y = 9
print(x, y)
print(x, y, sep="&&")
print(x, end=" ")
print(y)
length = 10
breadth = 10
print("Area wth length {} and breadth {} is {}sq.units".format(length, breadth, length * breadth))