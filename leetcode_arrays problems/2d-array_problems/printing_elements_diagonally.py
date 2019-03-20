def function1(twodarray):
    m=len(twodarray)
    n=len(twodarray[0])
    for k in range(0,m):
        i=k
        j=0
        while(i>=0):
            print(twodarray[i][j])
            i-=1
            j+=1
    for k in range(1,n):
        i=m-1
        j=k
        while(j<=n-1):
            print(twodarray[i][j])
            i-=1
            j+=1

function1([['a','b','c','d','e'],
           ['f','g','h','i','j'],
           ['k','l','m','n','o'],
           ['p','q','r','s','t']])