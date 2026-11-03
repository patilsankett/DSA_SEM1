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
    def pop(self, show=True):
        if self.isempty():
            print("Stack is empty")
        else:
            temp=self.top
            if show:
                print("Poped element: ",temp.data)
            self.top=self.top.next
            return temp.data
    def print(self):
        temp=self.top
        print("Stack elements...")
        while temp:
            print(temp.data)
            temp=temp.next
    def reverse(self, other):
        temp=self.top
        while temp:
            other.push(Node(temp.data))
            temp=temp.next
 
def reverse_string(s):
    st=stack()
    for ch in s:
        st.push(Node(ch))
    result=""
    while not st.isempty():
        result+=st.pop(False)
    return result
 
st=stack()
st1=stack()
st.push(Node(10))
st.push(Node(100))
st.push(Node(45))
st.push(Node(78))
st.push(Node(90))
st.print()
st.pop()
st.print()
print("Reversed string:", reverse_string("Hello"))
st.reverse(st1)
st1.print()