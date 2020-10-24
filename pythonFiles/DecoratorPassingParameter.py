def OutterFun(fun):
    def innerFun(args1,args2):
        print(f'arguments are {args1} and {args2}')
        fun(args1,args2)
    return innerFun

@OutterFun
def myFun(a1,b1):
    print("this is inside my function")

myFun(89,54)
