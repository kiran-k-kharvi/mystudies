def bub(a):
    for x in range(len(a)):
        for y in range(len(a)-x-1):
            if a[y]> a[y+1]:
                a[y],a[y+1]=a[y+1],a[y]
        print(a)

l = [2,4,32222,2,1,4,6,5,5,43,7,54,332,56,4323,667]
bub(l)

