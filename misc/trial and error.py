
'''
l=0
for i in range(10,l-1,-1):
    print(i,end=' ')

twod = [[0 for x in range(4)] for y in range(4)]
print(twod)

x=[1,2,3,4]
for i in range(len(x)-1):
    print(x[i])

for i in reversed(range(3)):
    print(i,end=',')

a=[-2,-3,4,-1,-2,1,5,-3]

for each in a:
    print(each)

matrix=[[1,2,3,4],
        [5,1,2,3],
        [9,5,6,2]]

def toplietz(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if row>0 and col>0 and matrix[row][col] != matrix[row-1][col-1]: return False
    else: return True



print(toplietz(matrix))

'''


tup = ((0,2.3345),265)
print(tup[0][1])

i = tuple([(0,2.5656),345])
print(i[0][1])