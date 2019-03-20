def func1(string):
    buff_dict={}
    list=[]
    for each in string:
        if each in buff_dict:
            buff_dict[each]+=1
        else:buff_dict[each]=1
    for key,value in buff_dict.items():
        list.append(key)
        list.append(str(value))
    compressor = ''.join(list)
    if len(compressor)>=len(string):return string
    else:return compressor

print(func1('aabcccccaaa'))


