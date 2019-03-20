def function1(grid):
    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]==1:
                perimeter+=count(grid,i,j)
    return perimeter

def count(grid,i,j):
    counter=0
    if i-1< 0 or grid[i-1][j] == 0:counter+=1
    if j+1>= len(grid[0]) or grid[i][j+1] == 0:counter+=1
    if i+1 >= len(grid) or grid[i+1][j] == 0:counter+=1
    if j-1 <0 or grid[i][j-1] == 0:counter+=1
    return counter

print(function1([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))