def func1(string):
    bool = [False]*128
    for each in string:
        if bool[ord(each)]: return False
        else:
            bool[ord(each)]=True
    return True

print(func1('pradeep'))

