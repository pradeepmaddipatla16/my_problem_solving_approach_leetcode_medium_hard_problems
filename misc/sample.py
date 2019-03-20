
'''

print(len('abcdef'))
print(ord('F')*len('abcdef'))
print('5'*6)
n = input()
name = input()
print(int(n)*2)
print(name)


n1,name1 = input().split()
print(n1,name1)

n2 = int(input())
print(type(n2))



def function1():
    length = input()
    n = int(input())
    width,height = input().split()
    print(length,n,width,height)
    for i in range(n):
        if length in range(10001):
            if width in range(1, 10001) and height in range(1, 1000):
                if width < length or height < length:
                    print("UPLOAD ANOTHER")
                elif width==length and height == length:
                    print("ACCEPTED")
                else:
                    print("CROP IT")

function1()


def spiralmatrix2(A,m,n):
    t,b,l,r=[0,m-1,0,n-1]
    d = 0
    while t<=b and l<=r:
        if d == 0:
            for i in range(l,r+1):
                print(A[t][i])
            t+=1
        elif d == 1:
            for i in range(t,b+1):
                print(A[i][r])
            r-=1
        elif d == 2:
            for i in range(r,l-1,-1):
                print(A[b][i])
            b-=1
        elif d == 3:
            for i in range(b,t-1,-1):
                print(A[i][l])
            l+=1
        d = (d+1)%4




spiralmatrix2([[2,4,6,8],[5,9,12,16],[2,11,5,9],[3,2,1,8]],4,4)




def mininfinitedis(x,y):
    xlen,ylen=[0,0]
    for i in range(len(x)-1):
        xlen = xlen + abs(x[i]-x[i+1])
    for i in range(len(y)-1):
        ylen = ylen + abs(y[i]-y[i+1])
    print(max(xlen,ylen))


mininfinitedis([0,-1,1],[-1,1,4])


def addonetonumber(x):
    return (-(~x))

print(addonetonumber(2))


def increment(digits):
    for i in reversed(range(len(digits))):
        if digits[i] != 9:
           digits[i] += 1
           break
        else:
           digits[i] = 0
    else: # no break, all 9s
        digits.insert(0, 1)
    print(digits)

increment([1,9,9,9])

def maxsumsubarray(a):
    max_sum_so_far = 0
    max_sum_ending_here = 0
    for each in range(len(a)):
        max_sum_ending_here = max_sum_ending_here + a[each]
        if max_sum_ending_here < 0 :
            max_sum_ending_here = 0
        elif max_sum_so_far < max_sum_ending_here:
            max_sum_so_far = max_sum_ending_here

    return max_sum_so_far

print(maxsumsubarray([-2,-3,4,-1,-2,1,5,-3]))

def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

print(fib(3))



def func1(nums):
    a=0
    for i in nums:
        a=a^i
    return a

print(func1([1,1,2,2,3,4,4]))

'''

v = input("enter the name:")
p=input()
print(f"first name is : {v} ")
print("last name is : {0}".format(p))
print("can do this",'5')
print("cannot do this"+'5')