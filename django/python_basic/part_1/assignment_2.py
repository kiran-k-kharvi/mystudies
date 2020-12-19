def array_check(arr):
    count = 0
    for x in arr:
        if(x==1):
            if (arr[count+1] ==2 and arr[count+2] ==3):
                print("series found in index {} to index {}".format(count,count+2))
                return
            else:
                count += 1
                continue
        else:
            count += 1


array_check([1,2,1,3,4,1,2,3])
array_check([2,3,1,2,3])
array_check([9,3,4,5,1,2,3,4,5,6])

#***********************************************************


def end_other(a,b):
    #return a.endswith(b) or b.endswith(a)
    if(len(a)>len(b)):
        if(a[-(len(b)):].lower() == b.lower()): # Do not repeat yourself ".lower()"
            return True
        else:
            return False
    else:
        q=b[-(len(a)):]
        if(q.lower() == a.lower()):
            return True
        else:
            return False



b = "ram"
a= "jdfdlfram"
print(end_other(a,b))

#*******************************************************

def no_teen_sum(a,b,c):

    print(fix_teen(a)+fix_teen(b)+fix_teen(c))


def fix_teen(x):
    if( x == 15 or x == 16 or 13 > x or x > 19):
        return x
    else:
        return 0

no_teen_sum(4,15,16)

#*************************************************************

def test(a):
    if a in [ 2,3,4,5,6]:
        return 1
    return 0
print(test(4))