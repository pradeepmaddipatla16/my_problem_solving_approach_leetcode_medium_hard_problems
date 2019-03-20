def function1(string,d):
    left_first = string[0:d]
    left_second = string[d:len(string)]
    right_first = string[len(string)-d:]
    right_second = string[0:len(string)-d]
    left_rotation = left_second+left_first
    right_rotation = right_first+right_second
    print(left_rotation,right_rotation)

function1("pradeep",2)
function1([1,2,3,4,5,6],2)