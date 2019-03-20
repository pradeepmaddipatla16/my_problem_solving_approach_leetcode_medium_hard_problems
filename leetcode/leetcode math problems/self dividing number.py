def function1(left,right):
    output=[]
    for i in range(left,right+1):
        if str(0) in str(i):continue
        if all([i%int(digit)==0 for digit in str(i)]):output.append(i)
    return output

print(function1(1,22))

