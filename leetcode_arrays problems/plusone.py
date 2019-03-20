def function1(digits):
    string=''
    for each in digits:
        string+=str(each)
    return list(str(int(string)+1))

print(function1([1,2,3]))