'''
one method

def function1(string):
    return string.lower()

print(function1('PRADeep'))

'''

'''
second method - ASCII method
'''

def function2(string):
    return ''.join([chr(ord(ch)+32) for ch in string])

print(function2('PRADEEP'))