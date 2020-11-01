def binarysearch(arr,l,h,key):
    while l <= h:
        mid = (l+h)//2
        if arr[mid] == key:
            break
        elif arr[mid] > key:
            h = mid-1
        else:
            l = mid+1
    return mid  

arr = [45,54,65,67,23,32,17,3,9,78,86,55]
s = sorted(arr)
print(s)
l = 0
h = len(arr)-1 
key = 86
pos = binarysearch(s,l,h,key)
if pos > -1:
    print(f'found in {pos+1} position')
else:
    print('not found')


