def func1(nums):
    s = sorted(nums)
    if len(s) == 0 or len(s) ==1: return False
    for i in range(0,len(s)):
        if s[i]==s[i+1]:
            return True
    return False


print(func1([2,4,18,22,22]))