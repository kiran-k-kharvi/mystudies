# def myfun(num):
#     def myfun2(num):
#         return num+1
#     return myfun2(num) + 1

# print(myfun(5))

# ***************************************************
# def plus_one(number):
#     return number + 1

# def function_call(function):
#     number_to_add = 5
#     return function(number_to_add)

# print(function_call(plus_one))

# ***********************************************

def myfun(num):
    def myfun2(num):
        return num + 1
    
    return myfun2
new = myfun(5)
print(new(4)) #myfun2 cant access directly

# ***********************************************

# def myfun(num):
#     def myfun2(num):
#         return num+1
#     return myfun2(num) + 1

# print(myfun(5))
# print(myfun2(9)) #myfun2 cant access directly