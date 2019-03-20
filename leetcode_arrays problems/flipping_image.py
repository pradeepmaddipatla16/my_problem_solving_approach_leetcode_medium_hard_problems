def function1(A):
    for row in A:
        for i in range((len(row)+1)//2):
            row[i],row[~i]= row[~i]^1,row[i]^1
    return A
print(function1([[1,1,0],[1,0,1],[0,0,0]]))