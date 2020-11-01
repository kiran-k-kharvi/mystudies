def linear(arr,key):
    for x in arr:
        if x == key:
            return -1
    print("if ele not found this will execute")
arr = [3,4,22,36,78,84,31,26,56,44,17,45]
key = 44

found = linear(arr,key)
if found == -1 :
    print("ele found")
else:
    print("not found")
