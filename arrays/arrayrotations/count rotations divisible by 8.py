def function1(number):
    count = 0
    n = len(number)
    if n == 0 : return 0
    if n == 1:
        if int(number)%8 == 0:
            count+=1
            return count
    if n == 2:
        if ((int(number[0])*10+int(number[1])*1)%8==0):
            count+=1
        if ((int(number[1])*10+int(number[0])*1)%8==0):
            count+=1
        return count
    for i in range(0,n-2):
        threedigitnumber = int(number[i])*100+int(number[i+1])*10+int(number[i+2])*1
        if threedigitnumber%8==0:count+=1
    # consider the three digit number formed by last two digits and first number
    threedigitnumber1 = int(number[n-2])*100+int(number[n-1])*10+int(number[0])*1
    if threedigitnumber1%8==0:count+=1
    threedigitnumber2 = int(number[n-1]*100)+int(number[0])*10+int(number[1])*1
    if threedigitnumber2%8==0:count+=1
    return count

print(function1('43262488612'))


