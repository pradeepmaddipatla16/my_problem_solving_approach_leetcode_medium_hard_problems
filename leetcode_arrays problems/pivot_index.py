def function1(array):
    total = sum(array)
    left_sum=0
    for index,value in enumerate(array):
        if left_sum == total-value-left_sum:return index
        left_sum+=value
    return -1

print(function1([1,7,3,6,5,6]))