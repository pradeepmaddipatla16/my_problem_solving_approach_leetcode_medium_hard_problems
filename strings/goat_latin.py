def function1(strings):
    finallist=[]
    for index,each in enumerate(strings.split(" ")):
            if each[0].lower() in ['a','e','i','o','u']:
                finallist.append(each+'ma'+'a'*(index+1))
            else:
                finallist.append(each[1:]+each[0]+'ma'+'a'*(index+1))
    return ' '.join(finallist)

print(function1('I speak Goat Latin'))
print(function1('The quick brown fox jumped over the lazy dog'))