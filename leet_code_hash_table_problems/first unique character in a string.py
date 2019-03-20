def function1(string):
    print(set(string))
    l = [string.index(i) for i in set(string) if string.count(i) == 1]
    print(l)
    if len(l)>0:
        return min(l)
    else:
        return -1

print(function1('ppppoppk'))

