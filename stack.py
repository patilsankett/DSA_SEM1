class node:
    def __init__(self,value):
        self.data=value
        self.next=None
class stack:
    def __init__(self):
        self.top=None
        
    def isempty(self):
        return self.top is None
    
    def push (self,new_node):
        new_node.next=self.top
        self.top=new_node

    def pop(self):
        if self.isempty():
            print("Stack is Empty")
        else:
            temp=self.top
            print("poped element :",temp.data)
            self.top=self.top.next
            temp=None

    def reverse(self):
        temp=self.top
        while temp:
            st1.push(node(temp.data))
            temp=temp.next

    def print(self):
        temp=self.top
        print("stack element :")
        while temp:
            print(temp.data)
            temp=temp.next

st=stack()
st1=stack()
st.push(node(10))
st.push(node(100))
st.push(node(45))
st.push(node(78))
st.push(node(90))
st.print()
st.pop()
st.pop()
st.reverse()
st1.print()