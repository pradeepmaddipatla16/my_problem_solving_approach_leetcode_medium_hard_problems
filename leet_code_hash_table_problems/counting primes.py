def function1(n):
    counter=0
    primes_list = [True]*(n+1)
    #print(primes_list,len(primes_list))
    primes_list[0],primes_list[1]=False,False
    for i in range(2,n+1):
        if primes_list[i]:
            for j in range(2,n):
                if (i*j)<=n:
                    primes_list[i*j]=False
    for i in range(n+1):
        if primes_list[i]==True:
            counter+=1
    return counter







print(function1(100))