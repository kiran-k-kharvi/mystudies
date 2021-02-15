def insertionSort(a):
    for i in range(1,len(a)):
        j = i-1
        current = a[i]

        while(j>=0 and a[j]>current):
            a[j+1]= a[j]
            j -= 1

        a[j+1] = current
    print(a)

l = [4,3,2,1,6,3,4,2,1,3,67,555,654,3,24,7,8,0]
insertionSort(l)