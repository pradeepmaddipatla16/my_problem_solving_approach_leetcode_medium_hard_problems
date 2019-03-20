def function1(array):
    sum=0
    array = sorted(array)
    for i in array[::2]:
        sum+=i
    return sum

print(function1([1,4,3,2]))