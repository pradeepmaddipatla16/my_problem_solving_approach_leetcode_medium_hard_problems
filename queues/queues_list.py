class queues:
    def __init__(self):
        self.list1=[]
        self.front = -1
        self.rear = -1
        self.max=100
    def is_empty(self):
        if self.front==-1 and self.rear == -1:
            return True
        else:return False
    def peek(self):
        if self.is_empty:print("the queue is empty")
        else:return self.list1[self.front]
    def enqueue(self,element):
        if (self.rear+1)%self.max == self.front:return
        elif self.is_empty():
            self.front=0
            self.rear=0
        else:self.rear = (self.rear+1)%self.max
        self.list1[self.rear]=element
    def dequeue(self):
        if self.is_empty():print("no items to delete")
        elif self.front==0 and self.rear==0:self.front,self.rear=-1
        else:self.front=(self.front+1)%self.max
q=queues()
q.enqueue(7)
q.enqueue(8)
q.enqueue(9)
q.enqueue(10)
q.dequeue()
q.dequeue()
q.peek()
q.is_empty()