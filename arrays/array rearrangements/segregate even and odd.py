def function1(number):
    l1=[x for x in number if x%2==0]+[x for x in number if x%2!=0]
    print(l1)

function1([1,9,5,3,2,6,7,11])