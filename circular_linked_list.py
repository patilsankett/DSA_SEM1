# Singly Circular linked list

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
            new_node.next = self.head            # circular: points to itself
        else:
            temp = self.head
            while temp.next != self.head:        # stop at last node, not None
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head            # last node points back to head

    def push(self, new_node : Node):
        if self.head == None:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def insert(self, new_node, pos):
        if pos == 1:  # insert node at first position
            if self.head == None:
                self.head = new_node
                new_node.next = self.head
                return
            temp = self.head
            while temp.next != self.head:        # find last node first
                temp = temp.next
            new_node.next = self.head
            temp.next = new_node                 # last node -> new first node
            self.head = new_node
        else:  # insert node from 2nd to last position
            p = 1
            temp = self.head
            while p != pos - 1:
                temp = temp.next
                p += 1
            new_node.next = temp.next
            temp.next = new_node

    def delete(self, value):
        if self.head == None:
            print("List is empty")
            return
        temp = self.head
        prev = None
        if temp.data == value:  # deleting the first node
            if temp.next == self.head:           # only one node
                self.head = None
            else:
                last = self.head
                while last.next != self.head:
                    last = last.next
                last.next = self.head.next       # last node -> new first node
                self.head = self.head.next
        else:
            prev = temp
            temp = temp.next
            while temp != self.head and temp.data != value:
                prev = temp
                temp = temp.next
            if temp == self.head:                # went full circle, not found
                print("Value is not present in the list")
                return
            prev.next = temp.next
            temp = None

    def print(self):
        print()
        print("List elements :")
        if self.head == None:
            print("(empty)")
            return
        temp = self.head
        while (True):
            print(temp.data, end=" ")
            temp = temp.next
            if temp == self.head:
                break
        print()

n1 = Node(0)
n2 = Node(12)
n3 = Node(90)

list1 = Linked_list()
list1.push(n1)
list1.push(n2)
list1.push(n3)
list1.print()              # 0 12 90

list1.insert(Node(5), 1)
list1.insert(Node(7), 3)
list1.print()              # 5 0 7 12 90

list1.delete(5)            # delete first
list1.delete(90)           # delete last
list1.delete(100)          # not present
list1.print()              # 0 7 12