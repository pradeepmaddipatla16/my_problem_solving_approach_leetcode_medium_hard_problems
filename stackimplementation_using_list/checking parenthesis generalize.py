from stackimplementation_using_list.array import Stack
s=Stack()
def matches(open,close):
    opens='([{'
    closes = ')]}'
    return opens.index(open) == closes.index(close)

def checkparenthesis(string):
    balanced = True
    for each in string:
        if each =='(' or each == '{' or each == '[':
            s.push(each)
        elif each == ')' or each =='}' or each == ']':
            if s.is_empty() or not matches(s.top(),each):
                balanced = False
            else:
                s.pop()
    if balanced and s.is_empty():
        return True
    else:
        return False

print(checkparenthesis('{{([][])}()}'))
print(checkparenthesis('[{()]'))