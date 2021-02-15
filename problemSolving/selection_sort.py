def selction_sort(a):

    for x in range(len(a)-1):
        minPos  = x

        for y in range(x,len(a)):
            if a[y] < a[minPos]:
                minPos = y
        
        a[x],a[minPos] = a[minPos],a[x]
        print(a)

l = [2,4,3,2,1,4,6,5,5,43,7,54,332,56,4323,667]
selction_sort(l)