def function1(number):
    ans = ""
    while number:
        number -= 1
        unitsdigit = number%26
        ans = chr(ord('A')+unitsdigit)+ans
        number=number//26
    return ans

print(function1(701))