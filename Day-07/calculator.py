class calculator:
    def __init__(self):
        print("Instance of class is created")

    def addition(self, num1, num2):
        return num1 + num2

    def subtraction(self, num1, num2):
        return num1 - num2

    def multiplication(self, num1, num2):
        return num1 * num2

    def __del__(self):
        print("Class is closed")


obj = calculator()
add = obj.addition(10, 20)
print("Addition:", add)
sub = obj.subtraction(10, 20)
print("subtraction:", sub)
mul = obj.multiplication(10, 20)
print("Multiplication:", mul)
