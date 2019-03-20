def function1(nums,target):
    buf_dict={}
    for index,value in enumerate(nums):
        if (target-value) in buf_dict.keys():return (buf_dict[(target-value)],index)
        else:buf_dict[value]= index


print(function1([2,7,11,15],26))