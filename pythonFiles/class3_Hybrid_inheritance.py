class A():
    Base = ''

class B(A):
    firstChild = ''

class C(A):
    secondChild = ''

class D(B,C):
    hybridChild = ''
    def details(self):
        print("Base class ", self.Base)
        print("Child class 1 ", self.firstChild)
        print("Child class 2 ", self.secondChild)
        print("Hybrid class ", self.hybridChild)

obj = D()

obj.Base = 'Base class'
obj.firstChild = 'Child 1'
obj.secondChild = 'Child 2'
obj.hybridChild = 'Hybrid Child'

obj.details()
