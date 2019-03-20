
def function1(strings):
    #print(strings[::-1])
    return ' '.join(each[::-1] for each in strings[::-1].split(' '))


print('name is nani')
print(function1('name is nani'))

'''
class Solution:
    def functional2(self,strings):
        k = list(strings)
        for index,each in enumerate(list(strings[::-1])):
            if each == " ":
                self.reverse(strings[::-1][:index])
        return list(strings)


    def reverse(self,strings):
        return strings[::-1]

a = Solution()
print(a.functional2("name is nani"))

'''