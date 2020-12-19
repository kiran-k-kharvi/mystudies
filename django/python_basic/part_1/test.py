x =[1,2,3,4,5,6,7,8]

def ev(num):
    return num%2 == 0
evens = filter(lambda num: num%2==0,x)
print(list(evens))


s = [2,3,4,5,6,7]
t = [22,33,44,55,66,77]
test = map(lambda x,y: (x,y),s,t)
print(list(test))

d = 'dlksokjo'
print(d[0::2])

print(d[-3:])