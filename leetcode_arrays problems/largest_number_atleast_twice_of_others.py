def function1(array):

    big = max(array)
    if all(big>= 2*number for number in array if number!=big):
        return array.index(big)
    else:return -1


print(function1([1,2,3,4]))