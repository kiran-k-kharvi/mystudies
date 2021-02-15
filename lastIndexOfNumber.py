def lastIndex(a,key,l):
    l -= 1
    if l<0:
        return -1
    if a[l] == key:
        return l
    
    samllArr = lastIndex(a,key,l)
    return samllArr

a = [2,3,4,5,7,2,3,2,4,5,6,2,55,45454,4645,45,454,45,54,7667688,1]

print(lastIndex(a,45,len(a)))
