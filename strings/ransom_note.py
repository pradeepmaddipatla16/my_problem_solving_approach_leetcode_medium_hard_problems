def function1(ransomNote, magazine):
    '''
    for letter in ransomNote:
        if ransomNote.count(letter)>magazine.count(letter):
            return False
    return True
    '''
    buf_dict = {}
    for each in magazine:
        if each in buf_dict:
            buf_dict[each]+=1
        else:buf_dict[each]=1
    for each in ransomNote:
        if each not in buf_dict or ransomNote.count(each)>buf_dict[each]:
            return False
    return True


print(function1('aaab','aab'))
print(function1('a','b'))
print(function1('aa','ab'))
print(function1('aa','aab'))