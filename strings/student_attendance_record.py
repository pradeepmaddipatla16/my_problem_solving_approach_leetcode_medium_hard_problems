'''
def function1(word):
    count=0
    l_con = 0
    for letter in word:
        if letter == 'A':
            count=count+1
            l_con=0
        if letter == 'L':l_con=l_con+1
        else:l_con=0
        if count>1 or l_con>2:return False
    return True


def function1(word):
    if 'LLL' in word or word.count('A')>2:return False
    else:return True

print(function1('ALLP'))

'''

def function1(word):
    for i in range(len(word)):
        if word[i:i+2] == 'LLL':return False
        elif word.count('A')>2:return False
        else:return True