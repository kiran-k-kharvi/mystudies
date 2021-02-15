def partision(arr,l,r):
    pivot = arr[r]
    i = l-1
    j=0
    for j in range(l,r):
        if arr[j]< pivot:
            i += 1
            arr[i], arr[j]= arr[j],arr[i]
    arr[i+1],arr[r]=arr[r],arr[i+1] 
    return i + 1



def quick_sort(arr,l,r):
    if l>=r:
        return
    pi = partision(arr,l,r)
    quick_sort(arr,l,pi-1)
    quick_sort(arr,pi+1,r)


arr = [4,2,1,4,5565,45,23,98,78]
quick_sort(arr,0,len(arr)-1)
print(arr)