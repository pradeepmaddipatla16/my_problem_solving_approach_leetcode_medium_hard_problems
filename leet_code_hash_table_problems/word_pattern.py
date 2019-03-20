def function1(pattern,string):
    str = string.split()
    if ([pattern.find(char) for char in pattern] == [str.index(word) for word in str ]):return True
    else:return False

print(function1('abba','dog cat cat fish'))