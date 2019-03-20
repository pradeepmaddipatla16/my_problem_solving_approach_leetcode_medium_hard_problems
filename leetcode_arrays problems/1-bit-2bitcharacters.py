def function1(bits):
    if not bits:return False
    n = len(bits)
    index = 0
    while index < n:
        if index == n-1:return True
        if bits[index]==1:index+=2
        elif bits[index]==0:index+=1
    return False

print(function1([0,0]))