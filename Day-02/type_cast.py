"""
The process of converting the value of one data type (integer, string, float, etc.) to another data type is called type conversion.
Python has two types of type conversion.
1:Implicit Type Conversion: Python automatically converts one data type to another data type
2:Explicit Type Conversion:UUsers convert the data type of an object to required data type.
"""
num1 = 123
num2 = 12.3
print(type(num1))
print(type(num2))
sum = num1 + num2  # Implicit Conversion
print(type(sum))
list = [1, 2, 3]
tuple = tuple(list)  # Explicit Conversion
print(tuple)
num3 = '123'
num4 = int(num3)
print(type(num3))
print(type(num4))


