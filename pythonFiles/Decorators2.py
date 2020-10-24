# def upperCase(fun):
#     def wrapper():
#         changedCase = fun.upper()
#         return changedCase
#     return wrapper


# print(upperCase('test')())  # or yes = upperCase('test')   
#                             #print(yes())



def upperCase(fun):
    def wrapper():
        innerFun = fun()
        changedCase = innerFun.upper()
        return changedCase
    return wrapper

@upperCase
def myFun():
    return 'testing this function'

print(myFun())