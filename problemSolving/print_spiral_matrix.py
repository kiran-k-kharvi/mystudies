matrix = []
myEntry = []
m = int(input("enter no of rows for matrix"))
n = int(input("enter no of column for matrix"))

for x in range(m):
    for y in range(n):
        myEntry.append(input(f" Enter element for matrix[{x}],[{y}]"))
    matrix.append(myEntry)
    myEntry = []

print(matrix)



top = 0
bottom = m-1
left = 0
right = n-1

dir = 0

while not(top>bottom and left>right):
    if dir == 0:
        for x in range(left,right+1):
            print(matrix[top][x])
        dir = 1
        top +=1

    if dir == 1:
        for y in range(top,bottom+1):
            print(matrix[y][right])
        dir = 2
        right -= 1

    if dir == 2:
        for z in range(right,left-1,-1):
            print(matrix[bottom][z])
        dir = 3
        bottom -=1
        

    if dir == 3:
        for a in range(bottom,top-1,-1):
            print(matrix[a][left])
        dir = 0
        left += 1
    