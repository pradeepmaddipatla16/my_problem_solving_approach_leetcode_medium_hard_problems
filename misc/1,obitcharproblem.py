bits=[1,1,0]
#print(bits[-2])


def fun1(bits):
    if len(bits)==1 and bits[0]==0:return True
    elif bits[-2]==1:return False
    else:return True
print(fun1(bits))
