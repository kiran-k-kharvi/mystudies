class A:
    def __init__(self,name,id):
        self.Aname = name
        self.id = id

class B(A):
    def __init__(self,name,id,age):
        self.Bname = name
        self.age = age
        A.__init__(self,name,id) # this is required else class a is not initialised

obj = B("kiran",344,23)
print(obj.Aname,obj.id,obj.age,sep=' ')