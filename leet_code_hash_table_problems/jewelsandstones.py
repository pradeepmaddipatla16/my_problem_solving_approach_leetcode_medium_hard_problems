'''
with dictionary

def function1(j,s):
    buf_dict={}
    counter=0
    for each in list(j):
        buf_dict[each]=1
    for each in list(s):
        if each in buf_dict:
            counter+=1
    return counter

print(function1('aA','aAAbbbb'))
'''

'''
without dictionary
'''

def function2(j,s):
    counter = 0
    for each in list(s):
        if each in list(j):
            counter=counter+1
    return counter

print(function2('aA','aAAbbbb'))
