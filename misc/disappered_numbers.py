array1 = [4,3,2,7,8,2,3,1]
new=[]
def disappearednums(array1):
    for each in array1:
        val = abs(each)-1
        if array1[val]>0:
            array1[val] = - array1[val]
    for i in range(len(array1)):
        if array1[i]>0:
            new.append(i+1)
    return new

print(disappearednums(array1))