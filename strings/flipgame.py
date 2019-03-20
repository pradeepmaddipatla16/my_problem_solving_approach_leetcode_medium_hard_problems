def function1(s):
    return ["{0}--{1}".format(s[:i],s[i+2:]) for i in range(len(s)) if s[i:i+2]=="++"]

print(function1("++++"))