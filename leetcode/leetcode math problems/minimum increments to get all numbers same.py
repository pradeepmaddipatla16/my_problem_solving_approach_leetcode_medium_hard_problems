def function1(array):
    min_element = min(array)
    return sum([x-min_element for x in array])

print(function1([1,1,3]))