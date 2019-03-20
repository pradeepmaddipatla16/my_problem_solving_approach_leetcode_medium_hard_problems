def function1(candies):
    req = len(candies)//2
    if len(set(candies)) == req:return len(set(candies))
    else:return len(list(set(candies))[:req])

print(function1([1,1,1,2,2,3,4,4]))