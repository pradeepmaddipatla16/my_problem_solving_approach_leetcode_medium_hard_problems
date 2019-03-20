class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Linkedlist:
    def __init__(self):
        self.head = None

    def insert_starting(self,newnode):
        temporarynode = self.head
        self.head = newnode
        self.head.next = temporarynode
        del temporarynode

    def insert_ending(self,newNode):
        if self.head is None:
            self.head = newNode
        else:
            lastnode = self.head
            while True:
                if lastnode.next is None:
                    break
                lastnode = lastnode.next
            lastnode.next = newNode

    def printList(self):
        if self.head is None:
            print("list is empty")
            return
        else:
            currentnode = self.head
            while True:
                if currentnode.next is None:
                    break
                else:
                    print(currentnode.data)
                    currentnode=currentnode.next
            print(currentnode.data)
        return

firstnode = Node("John")
linkedlist = Linkedlist()
linkedlist.insert_ending(firstnode)
#linkedlist.printList()
secondnode = Node("Ben")
linkedlist.insert_ending(secondnode)
newnode = Node("Matthew")
linkedlist.insert_starting(newnode)
linkedlist.printList()





