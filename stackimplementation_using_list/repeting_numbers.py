def func1(nums):
    buf_dict={}
    list1=[]
    for each in nums:
        if each in buf_dict:
            buf_dict[each]=buf_dict[each]+1
        else:
            buf_dict[each]=1

    for each in buf_dict:
        if buf_dict[each]>=2:
            list1.append(each)
    return list1

print(func1([4,2,4,5,2,3,1]))
