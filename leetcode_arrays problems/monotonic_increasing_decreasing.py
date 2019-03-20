def function1(a):
    increasing=decreasing=True
    for i in range(len(a)-1):
        if a[i]>a[i+1]:
            increasing = False
        if a[i]<a[i+1]:
            decreasing = False
    return increasing or decreasing

print(function1([1,2,2,3]))