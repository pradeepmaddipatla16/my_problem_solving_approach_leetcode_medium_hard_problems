def function1(list1):
    buf_dict = {}
    for each in list1:
        if each in buf_dict:
            buf_dict[each]+=1
        else:
            buf_dict[each]=1
        print(each)
        if buf_dict[each]>=2:return True
    return False

print(function1([-1,-1,'sab','sab','drake','a','1','sab','dr','b','s','a',1]))
print(function1([-1,1,'a','sab','[]',567]))