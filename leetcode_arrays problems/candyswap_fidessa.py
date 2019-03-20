def function(a,b):
    sa = sum(a)
    sb = sum(b)
    print(sa,sb)
    setb = set(b)
    print(setb)
    for x in a:
        if (x+(sb-sa)//2) in setb:
            return [x,(x+(sb-sa)//2)]

print(function([1,1],[2,2]))