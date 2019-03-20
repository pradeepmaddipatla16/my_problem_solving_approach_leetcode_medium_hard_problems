def function1(string):
    output=0
    multiply=0
    for character in string[::-1]:
        output+=(ord(character)-64)*(26**multiply)
        multiply+=1
    return output

print(function1('CZ'))