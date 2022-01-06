"""
 in Python programming, data types are actually classes and variables are instance (object) of these classes.
 Following are the standard or built-in data type of Python:
 1:Numeric-int,float,complex
 2:Sequence types-String,List,Tuple
 3:Boolean-true,false
 4:Set
 5.Dictionary
type() function is used to determine the type of data type

"""
print("Hello python")
name = "panju"
number = 123
my_list = ['pan', 'name', 1, 2]
my_tuple = (1, 2, 'panju', 'achu')
set1 = set([1, 'apple', 2, 'orange', 3, 'kiwi'])
Dict1 = {1: 'apple', 2: 'orange', 3: 'plum', 'category': 'fruits'}
print("My name is", name)
print("Roll no:", number)
print("name is:" + name)
print(my_list)
print(type(my_tuple))
print(my_tuple)
print(set1)
print(Dict1)
