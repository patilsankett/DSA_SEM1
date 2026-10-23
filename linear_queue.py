class Node:
    def __init__(self,value):
        self.data=value
        self.next=None
class Lqueue:
    def __init__(self):
        self.front=self.rear=None
        
    def enqueue(self,new_node):
        if self.rear:
            self.rear.next=new_node
            self.rear=new_node
        else:
            self.front=self.rear=new_node

    def dequeue(self):
        if self.front:
            temp=self.front
            self.front=self.front.next
            if self.front == None:
                self.rear=None
                print("Now Queue is Empty")
            temp=None 
        else:
            print("Queue is Empty !!")

    def print(self):
        temp=self.front
        while temp:
            print (temp.data,"->")
            temp=temp.next
        print()



que=Lqueue()
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