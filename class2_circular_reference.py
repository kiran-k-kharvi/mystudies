# Python program to illustrate destructor

class A:
    def __init__(self, bb):
        self.b = bb
        


class B:
    def __init__(self, w, e, r):
        self.p = w
        self.q = e
        self.s = r
        self.a = A(self)

    def __del__(self):
        print("die")


b = B(2,3,4)
