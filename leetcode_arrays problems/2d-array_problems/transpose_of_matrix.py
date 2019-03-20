def function1(matrix):
    row,column = len(matrix),len(matrix[0])
    ans = [[None]*row for _ in range(column)]
    for i,row in enumerate(matrix):
        for j,value in enumerate(matrix[i]):
            ans[j][i]=value
    return ans

def function2(matrix):
    return zip(*matrix)


#print(function1([[1,2],[3,4],[5,6]]))
print(function2([[1,2],[3,4],[5,6]]))