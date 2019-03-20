def function1(matrix):
    minimum = matrix[0][0]
    maximum = matrix[0][len(matrix[0])-1]
    for i,row in enumerate(matrix):
        for j,value in enumerate(matrix[i]):
            minimum = min(minimum,value)
            maximum = max(maximum,value)
    return abs(minimum-maximum)

print(function1([[1,2,3],[4,5],[1,2,3]]))