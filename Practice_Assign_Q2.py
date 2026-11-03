#queue using linked list
class Node:
    def __init__(self, value):
        self.data=value
        self.next=None
class stack:
    def __init__(self):
        self.top=None
    def isempty(self):
        return self.top is None
    def push(self, new_node):
        new_node.next=self.top
        self.top=new_node
    def pop(self):
        temp=self.top
        self.top=self.top.next
        return temp.data
class queue:
    def __init__(self):
        self.front=None
        self.rear=None
    def isempty(self):
        return self.front is None
    def enqueue(self, new_node):
        if self.isempty():
            self.front=self.rear=new_node
        else:
            self.rear.next=new_node
            self.rear=new_node
    def dequeue(self, show=True):
        if self.isempty():
            print("Queue is empty")
        else:
            temp=self.front
            if show:
                print("Dequeued element: ",temp.data)
            self.front=self.front.next
            if self.front is None:
                self.rear=None
            return temp.data
    def print(self):
        temp=self.front
        print("Queue elements...")
        while temp:
            print(temp.data)
            temp=temp.next
    def reverse(self):
        st=stack()
        while not self.isempty():
            st.push(Node(self.dequeue(False)))
        while not st.isempty():
            self.enqueue(Node(st.pop()))

def merge(q1, q2):
    q3=queue()
    for q in (q1, q2):
        temp=q.front
        while temp:
            q3.enqueue(Node(temp.data))
            temp=temp.next
    return q3

def identical(q1, q2):
    a=q1.front
    b=q2.front
    while a and b:
        if a.data != b.data:
            return False
        a=a.next
        b=b.next
    return a is None and b is None

q1=queue()
q2=queue()
for x in (10, 20, 30):
    q1.enqueue(Node(x))
for x in (40, 50):
    q2.enqueue(Node(x))
q1.print()
q1.dequeue()
q1.print()
q1.reverse()
q1.print()
q3=merge(q1, q2)
q3.print()
print("Identical:", identical(q1, q2))