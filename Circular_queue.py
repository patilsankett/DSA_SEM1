class Node:
    def __init__(self,value):
        self.data=value
        self.next=None
class Cqueue:
    def __init__(self):
        self.front=self.rear=None

    def enqueue(self,new_node):
        if self.rear:
            self.rear.next=new_node
            self.rear=new_node
        else:
            self.front=self.rear=new_node
        self.rear.next=self.front       # Added for circular
        return                          # Added for Circular

    def dequeue(self):
        if self.front:
            temp=self.front
            
            
            if self.front == self.rear: # Only one node in the queue
                self.front=self.rear=None
                print("Now Queue is Empty")
            else:
                self.front=self.front.next
                self.rear.next=self.front  # Added for Circular
            temp=None
        else:
            print("Queue is Empty")

    def print(self):
        temp=self.front
        while True:
            print (temp.data,end=" ")
            temp=temp.next
            if temp == self.front:
                break
        print()



que=Cqueue()
que.enqueue(Node(15))
que.enqueue(Node(67))
que.enqueue(Node(55))
que.enqueue(Node(100))
que.enqueue(Node(88))
que.print()
que.dequeue()
que.dequeue()
que.dequeue()
que.print()
que.dequeue()
que.enqueue(Node(23))
que.enqueue(Node(98))
que.print()