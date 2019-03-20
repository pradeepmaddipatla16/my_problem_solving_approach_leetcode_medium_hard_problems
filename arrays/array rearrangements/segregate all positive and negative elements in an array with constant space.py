def function1(numbers):
    nl = [x for x in numbers if x>0]+[x for x in numbers if x <0]
    print(nl)

function1([1,-1,3,2,-7,-5,11,6])