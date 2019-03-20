def twosum(array,target):
    buf_dict = {}
    for i in range(len(array)):
        complement = target-array[i]
        if complement in buf_dict:
            return (buf_dict[complement],i)
        else:
            buf_dict[array[i]]=i

print(twosum([2,7,11,15],18))
