class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linked_list:
    def __init__(self):
        self.head = None

    def append(self, new_node):
        if self.head == None:
            self.head = new_node          
        else:
            temp = self.head
            while (temp.next):        
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp

    def insert(self,new_node,pos):
        if pos == 1:
            new_node.next=self.head
            self.head=new_node
        else: #insert node from 2nd to last position
            p=1
            temp=self.head
            while(p!=pos-1 and temp.next):
                temp=temp.next
                p+=1
            if temp.next:     #last position
                temp.next.prev=new_node
            new_node.prev=temp
            new_node.next=temp.next
            temp.next=new_node

    def delete(self,value):
        temp=self.head
        if temp.data==value:
            self.head = self.head.next
            self.head.prev=None
        else:
            while(temp.data!=value and temp):
                temp = temp.next
                if temp == None:
                    print("Value is not present in the list")
                    return
            temp.prev.next = temp.next
            if temp.next:
                temp.next.prev = temp.prev          #Not Last Node
            temp=None

    def print(self):
            temp=self.head
            print("\nList Elements :",end=" ")
            while(temp):
                print(temp.data)
                temp=temp.next

    def printrev(self):
                temp=self.head
                print("\nList elements in reverse order:",end=" ")
                while temp.next:
                     temp=temp.next
                while(temp):
                    print(temp.data,end=" ")
                    temp=temp.prev

list1=Linked_list()

n1=Node(10)
n2=Node(20)

list1.append(n1)
list1.append(n2)
list1.append(Node(30))
list1.append(Node(40))
list1.print()
list1.insert(Node(5),200)
list1.print()
list1.delete(30)
list1.print()
list1.printrev()