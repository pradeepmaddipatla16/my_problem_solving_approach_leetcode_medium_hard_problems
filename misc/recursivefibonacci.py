import time
starttime=time.time()
def recfib(n):
    memo={}
    if n in memo:return memo[n]
    if n<2:
        f=n
    else:
        f = recfib(n-1)+recfib(n-2)
    memo[n]=f
    return f


print(recfib(30))

print(time.time()-starttime)
