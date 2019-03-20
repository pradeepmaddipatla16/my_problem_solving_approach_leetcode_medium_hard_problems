def function1(nums1,nums2):
    buf_dict = {}
    stack = []
    output = []
    for each in nums2:
        while stack and stack[-1] < each:
            buf_dict[stack.pop()]=each
        stack.append(each)

    for each in nums1:
        if each in buf_dict:
            output.append(buf_dict[each])
        else:output.append(-1)

    return output,stack

print(function1([1,3,5,2,4],[6,5,4,3,2,1,7]))