from stackimplementation_using_list.array import Stack
s=Stack()

def func1(number,base):
    new_string=''
    while number > 0:
        rem = number%base
        s.push(rem)
        number = number//base
    while not s.is_empty():
        new_string = new_string+str(s.pop)
    return new_string


print(func1(25,2))
print(func1(25,16))

