import math
def arrayrotations(array,k):
    n=len(array)
    d=-1
    for i in range(0,math.gcd(n,k)):
        j=i
        temp=array[i]
        while(1):
            d=(j+k)%n
            if d==i:
                break
            array[j]=array[d]
            j=d

        array[j]=temp
    return array

print(arrayrotations([1,2,3,4,5,6,7,8,9],3))


