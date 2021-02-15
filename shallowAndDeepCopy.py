import copy
x = [1,2,3,4]

print(id(x))
y = copy.deepcopy(x)
print(id(y))

print(id(x[0]))
print(id(y[0]))

x.append([67])
print(x)
print(y)

print(id(x[0]))
print(id(y[0]))
for x in range(1,10,2):
    print(x)



old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.copy(old_list)

old_list[1][1] = 'AA'

print("Old list:", old_list)
print("New list:", new_list)