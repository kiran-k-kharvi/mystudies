
class A:
    def __init__(self,a):
        self.b = a
    def __del__(self):
        print("obj destroyed")


obj = A(4)
print(obj.b)

