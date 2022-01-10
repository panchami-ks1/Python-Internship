""" range() function"""

# for i in range(1, 20, 2):
#     print(i, end=' ')
# else:
#     print("\n Finished..")
# for i in range(10, 50):
#     if i % 3 == 0 and i % 5 == 0:
#         print(i)

# """ Q1:Given year is leap year or not?"""
# year = int(input("Enter year:"))
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print(" Leap year")
#         else:
#             print("Not a leap year")
#     else:
#         print("Leap Year")
# else:
#     print("Not a leap year")

""" Q2:To find sum of two integers,if sum is between 15 and 20 return 20"""
num1 = int(input("Enter number1:\n"))
num2 = int(input("Enter number2:"))
sum = num1 + num2
if (15 <= sum < 20):
    print("sum is:",20)
else:
    print("Sum is:", sum)
#
# """ Q3:Find area of circle"""
# radius = int(input("Enter radius:"))
# area = 3.14 * radius ** 2
# print("Area of circle is:", area)
