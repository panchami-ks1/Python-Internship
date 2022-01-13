class A:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def add(self):
        return self.x+self.y

# obj1=A(10,20)
# sum=obj1.add()
# print(sum)

class B(A):
    def __init__(self,x,y,z):
        #A.__init__(self,x,y)
        super().__init__(x,y)
        # self.z=z
        # self.x = x
        # self.y = y
    def own(self):
        print("B's function")

obj2=B(10,20,30)
print(obj2.add())
obj2.own()


