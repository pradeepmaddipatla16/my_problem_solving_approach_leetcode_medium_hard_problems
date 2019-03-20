def func1(nums):
    n=len(nums)
    for i in range(n):
        index = nums[i]%n
        nums[index] = nums[index]+n
    for i in range(n):
        if nums[i]/n > 1:
            print(i,end=" ")

func1([1,2,3,1,3,6,6])