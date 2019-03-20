def func1(array):
    arraysum=0
    currentsum=0
    n=len(array)
    for i in range(len(array)):
        arraysum = arraysum+array[i]
        currentsum = currentsum+(i*array[i])
    max = currentsum
    for j in range(1,len(array)):
        currentsum = currentsum+arraysum-(n)*array[n-j]
        if currentsum>max:
            max=currentsum
    return max

print(func1([8,3,1,2]))

