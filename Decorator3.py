def upperCase(fun):
    def wrapper():
        innerFun = fun()
        changedCase = innerFun.upper()
        return changedCase
    return wrapper


def split_str(fun2):
    def string_split():
        afterChange = fun2()
        return afterChange.split()
    return string_split


@split_str
@upperCase
def myFun():
    return 'testing this function'

print(myFun())

