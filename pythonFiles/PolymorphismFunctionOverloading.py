# class arithmatic:
#     def add(self,x,y):
#         print(x + y)
#     def add(self,x,y,z):
#         print(x + y + z)

# obj = arithmatic()

# obj.add(4,5)
# obj.add(4,5,8) # Python does not support method over loading with multiple func having same name

class India:
    def capital(self):
        print("Delhi")
    def commonLan(self):
        print("Hindi")


class USA:
    def capital(self):
        print("Los Angelous")
    def commonLan(self):
        print("English")

obj_ind = India()
obj_usa = USA()

for x in (obj_ind,obj_usa):
    x.capital()
    x.commonLan()