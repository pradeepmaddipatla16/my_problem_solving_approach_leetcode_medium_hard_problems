def arrayreverse(array,start,end):
    while(start<end):
        temp = array[start]
        array[start] = array[end]
        array[end] = temp
        start+=1
        end-=1
    return array

def func1(array,d):
    n=len(array)
    arrayreverse(array,n-d,n-1)
    arrayreverse(array,0,n-(d+1))
    arrayreverse(array,0,n-1)
    return array

print(func1([1,2,3,4,5,6,7,8,9,10],3))