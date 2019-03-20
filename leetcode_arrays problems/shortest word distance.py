def function1(words,word1,word2):
    '''
    i1,i2=-1,-1
    mindistance = len(words)
    for i in range(len(words)):
        if words[i]==word1:
            i1=i
        elif words[i]==word2:
            i2=i
        if i1!=-1 and i2!=-1:
            mindistance = min(mindistance,abs(i1-i2))
    return mindistance
    '''


print(function1(['a','a','b','b'],"a","b"))

