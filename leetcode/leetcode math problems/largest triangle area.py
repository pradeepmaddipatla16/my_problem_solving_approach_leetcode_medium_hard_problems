from itertools import combinations
def function1(points):
    def area(p,q,r):
        return .5* abs(p[0]*q[1]+q[0]*r[1]+r[0]*p[1]-p[1]*q[0]-q[1]*r[0]-r[1]*p[0])

    return max(area(* triangle) for triangle in combinations(points,3))

print(function1([[0,0],[0,1],[1,0],[0,2],[2,0]]))