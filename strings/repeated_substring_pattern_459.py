def function1(string):
    multiplier = len(string)
    for i in range(len(string)):
        if string[:i]*multiplier == string:return True
        else:multiplier=len(string)//(i+1)
    return False

print(function1("abcabcabcabc"))
