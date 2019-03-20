def function(list1):
    output = []
    buf_dict = {'up':['q','w','e','r','t','y','u','i','o','p'],
                'middle':['a','s','d','f','g','h','j','k','l'],
                'down':['z','x','c','v','b','n','m']}
    for word in list1:
        if all(ch in buf_dict['middle']for ch in word.lower()) or all(ch in buf_dict['up'] for ch in word.lower()) or all(ch in buf_dict['down'] for ch in word.lower()):output.append(word)

    return output

print(function(['Hello','Alaska','Dad','Peace']))

'''

def function1(list1):
    output = []
    buf_dict = {'up':['q','w','e','r','t','y','u','i','o','p'],
                'middle':['a','s','d','f','g','h','j','k','l'],
                'down':['z','x','c','v','b','n','m']}
    for word in list1:
        for character in word.lower():
            if character not in buf_dict['up']:break
        else:output.append(word)
        for character in word.lower():
            if character not in buf_dict['middle']:break
        else:output.append(word)
        for character in word.lower():
            if character not in buf_dict['down']:break
        else:output.append(word)
    return output

print(function1(['Hello','Alaska','Dad','peace']))

'''