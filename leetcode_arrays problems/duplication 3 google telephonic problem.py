def function1(array,k):
    buf_dict = {}
    for index,key in enumerate(array):
        if key in buf_dict and index-buf_dict[key]<=k:
            return True
        buf_dict[key]=index
    return False

print(function1([1,0,1,1],1))