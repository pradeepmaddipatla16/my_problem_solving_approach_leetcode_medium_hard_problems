def function1(n):
    count=0
    for i in range(1,n+1):
        if '3' in str(i) or '4' in str(i) or '7' in str(i):
            continue
        if '2' in str(i) or '5' in str(i) or '6' in str(i) or '9' in str(i):
            count+=1
    return count

print(function1(857))