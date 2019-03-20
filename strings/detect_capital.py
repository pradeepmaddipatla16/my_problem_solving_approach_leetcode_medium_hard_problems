def function1(word):
    if word.islower() or word.istitle() or word.isupper():return True
    else:return False

print(function1('FlaG'))