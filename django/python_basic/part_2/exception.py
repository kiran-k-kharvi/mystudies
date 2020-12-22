try:
    f = open('sample.txt','r')
    f.write("Test write to sample text!")
except IOError:
    print(" This is except block")
else:
    print("success")
finally:
    print("I Always work no matter what!!@@@@@")
