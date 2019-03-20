def function1(strings,k):
    a = list(strings)
    for i in range(0,len(a),2*k):
        #a[i:i+k] = reversed(a[i:i+k])
        a[i:i+k]=a[i:i+k][::-1]
    return "".join(a)

print(function1("abcdefg",2))

