def function1(roman):
    sum = 0
    buf_dict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    for i in range(len(roman)):
        if i !=len(roman)-1:
            if buf_dict[roman[i]]>=buf_dict[roman[i+1]]:sum+=buf_dict[roman[i]]
            elif buf_dict[roman[i]]<buf_dict[roman[i+1]]:sum-=buf_dict[roman[i]]
    return sum+buf_dict[roman[-1]]

print(function1('MCMXCIV'))