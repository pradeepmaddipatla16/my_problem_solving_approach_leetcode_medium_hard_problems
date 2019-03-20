#import itertools
def function1(A,B):
    if len(A)!=len(B):return False
    if A==B:
        seen = set()
        for each in A:
            if each in seen:return True
            seen.add(each)
        return False
    else:
        pairs = []
        for a,b in zip(A,B):
            if a!=b:
                pairs.append((a,b))
            if len(pairs)>=3:return False
        return len(pairs)==2 and pairs[0]==pairs[1][::-1]


print(function1('aaaaaaaaaabc','aaaaaaaaaacb'))