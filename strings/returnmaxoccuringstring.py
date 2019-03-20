def function1(string):
    counter = [0]*128
    max = -1
    c=''
    for each in string:
        counter[ord(each)]+=1
    for each in string:
        if max < counter[ord(each)]:
            max = counter[ord(each)]
            c=each
    return c

print(function1('tesimonial'))