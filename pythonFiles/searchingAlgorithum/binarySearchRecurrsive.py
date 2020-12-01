def binary(arr,l,h,key):
    if l>h:
        return -1
    mid = (l+h)//2
    if arr[mid] == key:
        return mid
    elif key > arr[mid]:
        l = mid+1
        return binary(arr,l,h,key)
    elif key < arr[mid]:
        h = mid-1
        return binary(arr,l,h,key)


arr = [2,4,6,7,8,45,21,12,34,556,43]
s = sorted(arr)
h = len(s)-1
l = 0
key = 556
ans = binary(s,l,h,key)
if ans > -1:
    print(f'found in {ans+1} position')
else:
    print('not found')