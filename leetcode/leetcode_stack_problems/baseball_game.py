def function1(ops):
    stack = []
    for each in ops:
        if each == '+':
            stack.append(stack[-1]+stack[-2])
        elif each == 'D':
            stack.append(2*stack[-1])
        elif each == 'C':
            stack.pop()
        else:stack.append(int(each))
    return sum(stack)

print(function1(['5','2','C','D','+']))
print(function1(['5','-2','4','C','D','9','+','+']))