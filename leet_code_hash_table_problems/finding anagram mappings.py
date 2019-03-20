def function1(a,b):
    if len(a)!=len(b):return 0
    buf_dict={}
    p=[]
    for index,key in enumerate(b):
        buf_dict[key]=index
    for each in a:
        if each in buf_dict:p.append(buf_dict[each])
    return p

print(function1([12,28,46,32,50],[50,12,32,46,28]))

def function2(a,b):
    if len(a)!=len(b):return 0
    buf_dict = {}
    p=[]
    for index,value in enumerate(b):
        buf_dict[value] = index
    for each in a:
        if each in buf_dict.keys():p.append(buf_dict[each])
    return p

print(function2([12,28,46,32,50],[50,12,32,46,28]))