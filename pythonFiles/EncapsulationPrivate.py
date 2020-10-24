class A:
    def __init__(self,var1,var2):
        self.__op1 = var1
        self.op2 = var2
        
        

class B(A):
    def __init__(self,x,y):


        A.__init__(self,x,y)

obj = B(5,9)

print(obj.op2)
print(obj._A__op1) # private variable can be accessed from child class using mangling
print(obj.op1) # private variable cannot be accessed from child class
