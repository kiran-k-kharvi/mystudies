def rev(arr):
    x =0
    y=len(arr)-1
    mid = (x+len(arr)//2)

    while(y >= mid):
        arr[x],arr[y] = arr[y],arr[x]
        x += 1
        y -= 1
    
    print(arr)


arr= ['s','d','f','h']
rev(arr)