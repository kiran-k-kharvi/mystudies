class office:
    def __init__(self,name):
        self.Name = name
    def isEmployee(self):
        return False
    def getName(self):
        return self.Name

class emp(office):
    def isEmployee(self):
        return True

objEmp = emp("kiran")
print(objEmp.Name,objEmp.isEmployee(),sep=' ** ')

obj2 = office("virat")
print(obj2.Name,obj2.isEmployee(),sep=' ** ')
