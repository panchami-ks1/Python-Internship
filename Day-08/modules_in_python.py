# Inbuilt modules
import datetime
import numpy

print(datetime.datetime.now())  # Current date and time

x = numpy.array([10, 20, 30])  # creates array from list


# Custom modules
""" Any file created inside a python project is a module
import filename"""

#Import from a folder
""" from folder_name import filename as f
import folder_name.filename as f"""

# Modules with alias names
import function as f

f.welcome()

# import individual items from module
from function import x
from function import welcome

print(x)
welcome()

# Import all items from module
from function import *
print(x)

# Import class from a module
from  class_task import students as s
obj=s()
s.login('1001','steve')


