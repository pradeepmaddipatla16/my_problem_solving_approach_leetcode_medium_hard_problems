def function1(string):
    p = string.split(" ")
    print(p)
    return "%20".join(string.split())

print(function1("Mr John Smith "))
