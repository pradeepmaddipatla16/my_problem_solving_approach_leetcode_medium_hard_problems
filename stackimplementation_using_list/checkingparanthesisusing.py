from stackimplementation_using_list.array import Stack as s
S = s()
def parenthesischecker(string):
    balanced = True
    for each in list(string):
        if each == '(':
            S.push(each)
        else:
            if S.is_empty():
                balanced = False
            else:
                S.pop()
    if balanced and S.is_empty():
        return True
    else:
        return False

print(parenthesischecker('((()))'))
print(parenthesischecker('((())'))
