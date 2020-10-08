class stat:
    commonVar = 0
    def __init__(self,var1,var2):
        self.__x = var1
        self.y = var2
        stat.commonVar += 1
    def naiKavya(self):
        print(self.__x,self.y)
        
    

obj1 = stat(2,4)
obj2 = stat(44,67)

print(obj2.naiKavya())
print()
print("after 2 object creation obj2.commonVar",obj2.commonVar)
obj3 = stat(8,4)
obj4 = stat(8,5)

print("after 4 object creation.  obj4.commonVar =",obj4.commonVar)

print()
print()

print("after 4 object creation. obj2.commonVar =",obj2.commonVar)
