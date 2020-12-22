def test1(fun):
    print("this is test 1 function")
    def child_func():
        fun()
        print('This is child func')
    
    return child_func

@test1
def test2():
    print('this is test 2 function')

# test2 = test1(test2)
# test2()
 
test2()
