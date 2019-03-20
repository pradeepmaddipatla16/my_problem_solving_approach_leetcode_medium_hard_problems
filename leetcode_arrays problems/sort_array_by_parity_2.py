def function1(a):
    j=1
    for i in range(0,len(a),2):
        if a[i]%2:
            while a[j]%2==1:
                j+=1
            a[i],a[j]=a[j],a[i]
    return a

print(function1([4,2,5,7]))