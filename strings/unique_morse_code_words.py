import string
morse_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
def function1(lists):
    #print(string.ascii_lowercase)
    buf_dict = dict(zip(string.ascii_lowercase,morse_code))
    #transformation = ""
    final_list=[]
    for each in lists:
        transformation=""
        for each_word in each:
            transformation=transformation+buf_dict[each_word]
        print(transformation)
        final_list.append(transformation)
    return len(set(final_list))
    #print(transformation)

print(function1(['gin','zen','gig','msg']))