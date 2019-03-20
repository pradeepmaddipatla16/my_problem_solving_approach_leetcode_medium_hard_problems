def reshape(matrix,r,c):
    if len(matrix)==0 or r*c != len(matrix)*len(matrix[0]): return matrix
    rows=0
    cols=0
    res=[[0 for x in range(c)]for y in range(r)]
    for i in range(0,len(matrix)):
        for j in range(0,len(matrix[0])):
            res[rows][cols] = matrix[i][j]
            cols=cols+1
            if cols==c:
                rows=rows+1
                cols=0
    return res

matrix=[[1,2],[3,4]]
print(reshape(matrix,1,4))