def palindromepermutation(string):
    flag = False
    buf_dict = {}
    for each in string:
        if ord(each) in range(65,91) or ord(each) in range(97,123):
            if each in buf_dict:
                buf_dict[each]+=1
            else:
                buf_dict[each] = 1

    for key,value in buf_dict.items():
         if value % 2 == 1:
             if flag:return False
             flag = True

    return True

print(palindromepermutation('chirec'))