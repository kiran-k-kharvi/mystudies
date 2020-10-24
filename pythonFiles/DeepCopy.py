import copy

class A:
    def __init__(self,x,y,ob):
        self.a = x
        self.b = y
        self.m = ob
        
class B:
    def __init__(self,p,q):
        self.r = p
        self.s = q

objB = B(4,5)
objA = A(3,6,objB)

newObj = copy.deepcopy(objA)

print("Before newObj.a = ",newObj.a)
print("Before newObj.b = ",newObj.b)
print("Before newObj.m.r = ",newObj.m.r)
print("Before objA.a = ",objA.a)
print("Before objA.b = ",objA.b)
print("Before objA.m.r = ",objA.m.r)

objA.m.r = 565
objA.a = 78


print()
print("ObjA.a = 78 and  objA.m.r = 565 ")
print()





print("After newObj.a = ",newObj.a)
print("After newObj.b = ",newObj.b)
print("After newObj.m.r = ",newObj.m.r)
print("After objA.a = ",objA.a)
print("After objA.b = ",objA.b)
print("After objA.m.r = ",objA.m.r)

