"""
Python uses the usual flow control statements.The most well-known statement type is the if statement.
There can be zero or more elif parts, and the else part is optional.
The keyword ‘elif’ is short for ‘else if’, and is useful to avoid excessive indentation.
An if … elif … elif … sequence is a substitute for the switch or case statements found in other languages."""

age = int(input("Enter age:"))
if age < 18:
    print("Not adult")
elif 18 <= age <= 60:
    print("Adult Person")
else:
    print("Senior citizen")
