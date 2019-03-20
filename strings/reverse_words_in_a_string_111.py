def function1(strings):
    return ' '.join([word[::-1] for word in strings.split(' ')])

print(function1('leet code contest'))
