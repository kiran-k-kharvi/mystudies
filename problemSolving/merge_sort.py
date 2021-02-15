def merge_sort_conqure(arr2, l,r,mid):
    l_sort = arr2[l:mid+1]
    r_sort = arr2[mid+1:r+1]
    i=0
    j=0
    arrSortIndex = l
    n1 = len(l_sort)-1
    n2 = len(r_sort)-1

    while i<= n1 and j<= n2:
        if  l_sort[i] > r_sort[j]:
            arr2[arrSortIndex] = r_sort[j]
            j += 1
            arrSortIndex += 1
        else:
            arr2[arrSortIndex] = l_sort[i]
            i += 1
            arrSortIndex += 1


    while(i<=n1):
        arr2[arrSortIndex] = l_sort[i]
        i += 1
        arrSortIndex += 1
    
    while(j<=n2):
        arr2[arrSortIndex] = r_sort[j]
        j += 1
        arrSortIndex += 1




def merge_sort_divide(arr,l,r):
    if l>=r:
        return
    else:
        mid = (l+r)//2
        merge_sort_divide(arr,l,mid)
        merge_sort_divide(arr,mid+1,r)
        merge_sort_conqure(arr, l,r,mid)
        


arr = [ 4,5,2,1,7,56,3,5678,45]

merge_sort_divide(arr,0,len(arr)-1)
print(arr)