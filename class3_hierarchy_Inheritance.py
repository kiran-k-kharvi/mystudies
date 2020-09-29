class A():
    Base = 'hi'

class B(A):
    child1 = ''
    def details(self):
        print("Base is : ",self.Base)
        print("Child is : ",self.child1)

class C(A):
    child2 = ''
    def details(self):
        print("Base is : ",self.Base)
        print("Child is : ",self.child2)


obj1 = B()
obj2 = C()

obj1.Base = "Base class"
obj1.child1 = "Child class 1"

obj2.child2 = "Child class 2"


obj1.details()
obj2.details()
