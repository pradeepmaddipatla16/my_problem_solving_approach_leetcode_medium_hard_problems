def func1(nums):
    nums1 = [str(x) for x in nums]
    number = str(int("".join(nums1)) + 1)
    return [int(each) for each in number]


print(func1([1,2,3]))