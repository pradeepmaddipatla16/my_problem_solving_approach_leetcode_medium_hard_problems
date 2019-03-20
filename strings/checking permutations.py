'''
def func1(string1,string2):
    if len(string1)!=len(string2):return False
    elif sorted(string1)==sorted(string2):return True
    return False
print(func1('god','dog'))
'''

def func2(string1,string2):
    array = [0]*128
    if len(string1)!=len(string2):return False
    for each in string1:
        array[ord(each)]+=1
        #print(array)
    for each in string2:
        array[ord(each)]-=1
        print(array)
        if array[ord(each)]<0 or array[ord(each)]>0:
            return False
    return True

print(func2('godo','doag'))


