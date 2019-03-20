'''
relative order is changing:
def function1(nums):
    i=0
    j=len(nums)-1
    while(i<j):
        if nums[i]==0:
            nums[i],nums[j]=nums[j],nums[i]
            i+=1
            j-=1
        else:
            i+=1
    return nums

print(function1([0,1,0,3,12]))


def function1(nums):
    count = 0
    for each in nums:
        if each!=0:
            nums[count] = each
            count+=1
    #print(count)

    #while(count<len(nums)):
    #    nums[count] = 0
    #   count+=1

    for i in range(count,len(nums)):
        nums[i]=0
    return nums

print(function1([0,1,0,3,12]))

'''

