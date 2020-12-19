class test:
    def __init__(self,a):
        print("obj created")
        self.a = a+2
    def hi(self):
        print("hi man")

class t2(test):
    def __init__(self,a):
        test.__init__(self,a)
        print("child created")
        self.c = a
        
    

x =t2(77)
print(x.a)
