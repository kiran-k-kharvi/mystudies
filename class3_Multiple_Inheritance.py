class A():
    father = ''
    
class B():
    mother = ''

class C(A,B):
    def details(self):
        print("father name is : ",self.father)
        print("mother name is : ",self.mother)

obj = C()

obj.father = "mike"
obj.mother = "melissa"
obj.details()
