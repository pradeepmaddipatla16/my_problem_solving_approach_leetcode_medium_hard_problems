def function1(a,b):
    buf_dict = {}
    output = []
    for each in a.split():
        if each in buf_dict:
            buf_dict[each]+=1
        else:
            buf_dict[each]=1
    for each in b.split():
        if each in buf_dict:
            buf_dict[each]+=1
        else:
            buf_dict[each]=1
    print(buf_dict.items())
    for each in buf_dict:
        if buf_dict[each]==1:output.append(each)
    return output

print(function1('this is an apple sweet','this is an apple banana'))

