s = 'django'

print(s[0])
print(s[-1])
print(s[0:4])
print(s[1:4])
print(s[4:])
print(s[::-1])
# *********************************************

l = [3,7,[1,4,'hello']]
l[2][2]='goodbye'
print(l)

# **************************************

d1 = {'s1' : 'hello'}
d2 = {'k1' : {'k2':'i am'}}
d3 = {'k2' : [{'nested':['this is deep',['kiran']]}]}

print(d1['s1'])
print(d2['k1']['k2'])
print(d3['k2'][0]['nested'][1][0])

#***************************************

mylist= [1,1,1,1,2,2,2,2,3,3,3,3]
print(list(set(mylist)))
#****************************

age = 4
dogName = 'sam'
print('my dogs name is {} and he is {} years old'.format(dogName,age))

