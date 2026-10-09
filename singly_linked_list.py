# Linked list file

# Singly linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linked_list:
    base = None
    end = None
    def __init__(self):
        self.base = None

    def push(self, new_node : Node):
        if self.base== None:
            self.base = new_node
        else:
            temp = self.base
            while temp.next:
                temp = temp.next
            temp.next = new_node
    def insert(self,new_node,pos):
            if pos == 1:
                new_node.next=self.head
                self.head=new_node
            else: #insert node from 2nd at last Position
                p=1
                temp=self.head
                while (p!=pos-1):
                    temp=temp.next
                    p+=1
                    new_node.next=temp.next
                    temp.next=new_node

    def delete(self,value):
        temp=self.head
        if temp.data==value:
            self.head = self.head.next
        else:
            while(temp.data!=value and temp):
                prev = temp
                temp = temp.next
            if temp == None:
                print("Value is not present in the list")
                return
            prev.next = temp.next
            temp=None
    

    def print(self):
        temp = self.base
        while temp:
            print(temp.data)
            temp = temp.next

n1 = Node(0)
n2 = Node(12)
n3 = Node(90)

list1 = Linked_list()
list1.push(n1)
list1.push(n2)
list1.push(n3)

list1.print()
