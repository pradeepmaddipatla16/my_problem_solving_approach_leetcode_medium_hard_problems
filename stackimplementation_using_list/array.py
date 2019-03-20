class Stack:
    def __init__(self):
        self.list1=[]
    def push(self,element):
        self.list1.append(element)
    def pop(self):
        return self.list1.pop()
    def top(self):
        return self.list1[-1]
    def is_empty(self):
        if len(self.list1)==0:
            return True
        else:
            return False
    def length(self):
        return len(self.list1)


S = Stack()

'''
S.push(6)
S.push(7)
S.push(8)
S.push(9)
S.push(10)
print(S.top())
print(S.pop())
print(S.top())
print(S.is_empty())
print(S.length())
'''