class A():
    firstLevel = ''

class B(A):
    secondLevel = ''

class C(B):
    thirdLevel = ''
    def details(self):
        print("This is first Level", self.firstLevel)
        print("This is second Level", self.secondLevel)
        print("This is third Level", self.thirdLevel)

obj = C()

obj.firstLevel = "1st"
obj.secondLevel = "2nd"
obj.thirdLevel = "3rd"

obj.details()