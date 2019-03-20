
def function1(points,k):
    points.sort(key=lambda p:p[0]**2+p[1]**2)
    return points[:k]

'''
def function2(points):
    points.sort(key=lambda p:sum(p))
    return points

print(function2([[1,8],[3,4],[5,6]]))

'''

print(function1([[1,3],[-2,2]],1))